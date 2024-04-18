import cv2
import pytesseract
import re
from convert_format import format_identificator

# Pensar se é necessário transformar a classe em estática em sprint futura
class OCR_DOCS:
    def __init__(self, img_path) -> None:
        self.img = format_identificator(img_path)
        self.extracted = ""
        self.name = ""
        self.Rg_id = ""
        self.born_date = ""
        self.mother_name = ""
        self.father_name = ""
        self.place_of_birth = ""
        self.date_of_issue = ""
        

    def new_rg(self):
        rgb = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        imagem_cinza = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
        bilateral = cv2.bilateralFilter(imagem_cinza, 20, 75, 75)
        cv2.imshow("bilateral", bilateral)
        margin = cv2.Canny(bilateral, 50, 100, apertureSize=3) # Apenas em desenvolvimento (não é necessário para o OCR)
        cv2.imshow("img", margin) # Apenas em desenvolvimento
        cv2.waitKey(0)

        self.extracted = pytesseract.image_to_string(imagem_cinza, lang='por', config='--psm 6')
    
    def find_info(self, info):
        regex = rf"{info} .+\n(.+)\b" # Exemplo de regex para buscar informação na linha de baixo
        info_catched = re.findall(regex, self.extracted)
        if info_catched:
            return info_catched[0]
        else:
            return "Não encontrado"
if __name__ == "__main__":
    # Colocar Testagem em outro lugar em próxima sprint
    teste = OCR_DOCS("ambiente_virtual/rg_verso.jpg")
    teste.new_rg()

    print(teste.extracted)
    print('------------------------------------')
    # teste.extract_info()
    print(teste.mother_name)