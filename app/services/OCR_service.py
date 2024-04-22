import cv2
import pytesseract
import re
from convert_format import format_identificator

# Pensar se é necessário transformar a classe em estática em sprint futura
class OCR_DOCS:
    def __init__(self, img_path) -> None:
        self.path = img_path
        self.img = format_identificator(img_path)
        self.extracted = ""
        self.name = ""
        self.rg_id = ""
        self.born_date = ""
        self.mother_name = ""
        self.place_of_birth = ""

    def new_rg(self):
        filter = cv2.imread(f"{self.path[:-7]}_gt_segmentation.jpg")

        rgb = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        imagem_cinza = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
        filtro_cinza = cv2.cvtColor(filter, cv2.COLOR_BGR2GRAY)
        img_aux = imagem_cinza.copy()
        img_aux[filtro_cinza < 50] = 255
        thre = cv2.threshold(img_aux, 165, 255, cv2.THRESH_BINARY)[1]

     
        cv2.imshow("apos_mudancas", thre)
        # cv2.imshow("sem rgb", image2)
        cv2.waitKey(0)

        print("shape1", rgb.shape)
        # cv2.imshow("Imagem Cinza", imagem_cinza)
        # cv2.waitKey(0)

        angulacao = self.identificar_angulacao(self.img)
        print("angulacao", angulacao)
        if angulacao > 45:
            angulacao = angulacao - 90
            print('nova', angulacao)

        altura = largura = max(self.img.shape[:2])
        centro = (largura // 2, altura // 2)
        matriz_rotacao = cv2.getRotationMatrix2D(centro, -angulacao, 1.0)
        imagem_rotacionada = cv2.warpAffine(
            thre,
            matriz_rotacao,
            (largura, altura),
            borderMode=cv2.BORDER_CONSTANT,
        )
        cv2.imshow("Imagem Rotacionada", imagem_rotacionada)
        cv2.waitKey(0)

        self.extracted = pytesseract.image_to_string(
            imagem_rotacionada, lang="por", config="--psm 6"
        )

    def identificar_angulacao(self, img):
        imagem_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bordas = cv2.Canny(imagem_cinza, 50, 150, apertureSize=3)

        contornos, _ = cv2.findContours(
            bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        retangulo = cv2.minAreaRect(contornos[0])
        angulacao = retangulo[2]
        return angulacao
    
    def find_name(self):
        regex = r"nome\s*([^\n]+)"
        name = re.findall(regex, self.extracted.lower(), re.DOTALL)
        print("nome do regex", name)
        if name:
            return name[0].upper()

    def find_rg(self):
        regex = r"(\d{2}[.]\d{3}[.]\d{3}[-]\d{2})"
        rg = re.findall(regex, self.extracted.lower(), re.DOTALL)
        # print("rg do regex", rg)  # Apenas para debug
        if rg:
            return rg[0]
        else:
            regex = r"(\d{2}[.]\d{3}[.]\d{3}[-]\d{1})\b"
            rg = re.findall(regex, self.extracted.lower(), re.DOTALL)
            if rg:
                return rg[0]

    def find_born_date(self):
        regex = r"nascimento.*?\s*(\d{2}[/]\d{2}[/]\d{4})"
        born_date = re.findall(regex, self.extracted.lower(), re.DOTALL)
        # print("nascimento do regex", born_date)  # Apenas para debug
        if born_date:
            return born_date[0]

    def find_mother_name(self):
        regex = r"filiação.*?\s*\n(.+)"
        mother_name = re.findall(regex, self.extracted.lower())
        # print("nome da mãe", mother_name)  # Apenas para debug
        if mother_name:
            return mother_name[0].upper()

    def find_place_of_birth(self):
        regex = r"naturalidade.*?\n([^\s]+) "
        place_of_birth = re.findall(regex, self.extracted.lower())
        if place_of_birth:
            return place_of_birth[0].upper()

    def extract_info(self):
        if self.name == "":
            self.name = self.find_name()
        if self.rg_id == "":
            self.rg_id = self.find_rg()
        if self.born_date == "":
            self.born_date = self.find_born_date()
        if self.mother_name == "":  # Este não pode ser obrigatório
            self.mother_name = self.find_mother_name()
        if self.place_of_birth == "":
            self.place_of_birth = self.find_place_of_birth()

        if not all(
            [
                self.name,
                self.rg_id,
                self.born_date,
                self.mother_name,
                self.place_of_birth,
            ]
        ):
            return "Fazer modificações na imagem e tentar novamente"


if __name__ == "__main__":
    ocr = OCR_DOCS("ambiente_virtual/00025928_in.jpg")
    ocr.new_rg()
    ocr.extract_info()
    print(ocr.extracted)

    
    
