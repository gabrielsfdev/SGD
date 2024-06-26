import cv2
import pytesseract
import re
import os
import PyPDF2

# Pensar se é necessário transformar a classe em estática em sprint futura
class OCR_DOCS:
    def __init__(self, img_path) -> None:
        from .convert_format import format_identificator
        # Geral
        self.path = img_path
        self.extracted = ""
        # Dados de RG
        self.img = format_identificator(img_path)
        self.name = None
        self.rg_id = None
        self.born_date = None
        self.mother_name = None
        self.place_of_birth = None
        self.attempt = 0
        self.thresh = 100
        # Dados do contrato
        self.contratante = None
        self.contratada = None
        self.num_process = None

    def _new_rg(self):
        file_path = f'app\\data\\masks\\{os.path.basename(self.path)}'
        filter = cv2.imread(f"{file_path[:-7]}_gt_segmentation.jpg")
        #filter = cv2.imread(f"{file_path[:-7]}_gt_segmentation.jpg")

        rgb = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        imagem_cinza = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
        filtro_cinza = cv2.cvtColor(filter, cv2.COLOR_BGR2GRAY)
        img_aux = imagem_cinza.copy()
        img_aux[filtro_cinza < 60] = 255
        thre = cv2.threshold(img_aux, self.thresh, 255, cv2.THRESH_BINARY)[1]

        angulacao = self.identificar_angulacao(self.img)
        # print("angulacao", angulacao)
        osd = pytesseract.image_to_osd(rgb, output_type=pytesseract.Output.DICT)
        # print("osd", osd)
        if osd['rotate'] == 90 or osd['rotate'] == 180 or osd['rotate'] == 270:
            angulacao = -osd["rotate"]
        elif angulacao > 45:
            angulacao = angulacao - 90
        # print('nova', angulacao)

        altura = largura = max(self.img.shape[:2])
        centro = (largura // 2, altura // 2)
        matriz_rotacao = cv2.getRotationMatrix2D(centro, angulacao, 1.0)
        img_aux = cv2.warpAffine(
            thre,
            matriz_rotacao,
            (largura, altura),
            borderMode=cv2.BORDER_CONSTANT,
        )
        # cv2.imshow("Imagem Rotacionada", img_aux)
        # cv2.waitKey(0)

        self.extracted = pytesseract.image_to_string(
            img_aux, lang="por", config="--psm 6"
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
    
    def _new_contract(self):
        pdf_path = self.path
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)  # Usando len() para obter o número de páginas
            for page_number in range(num_pages):
                # print("teste")
                page = reader.pages[page_number]  # Acessando a página diretamente pelo índice
                self.extracted += page.extract_text()

    def extract_contract_info(self):
        self._new_contract()

        regex_contratante = r"contratante :\s*([\w\sÀ-ÿ]+)"
        self.contratante = str(re.findall(regex_contratante, self.extracted.lower(), re.DOTALL)[0]).upper()

        regex_contratada = r"contratada :\s*([\w\sÀ-ÿ()-]+)"
        self.contratada = str(re.findall(regex_contratada, self.extracted.lower(), re.DOTALL)[0]).upper()

        regex_num_process = r"processo nº\s*([\d./-]+)"
        self.num_process = str(re.findall(regex_num_process, self.extracted.lower(), re.DOTALL)[1])

        # regex_cnpj_contratada = r"contratada :(?:.|\n)*?(\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b)"
        # cnpj_contratada = re.findall(regex_cnpj_contratada, self.extracted.lower(), re.DOTALL)
        # print(cnpj_contratada)
        
        if any(
            [
                self.extracted,
                self.contratante,
                self.contratada,
                self.num_process,
            ]
        ):
        
            dados_contrato = {
                'conteudo': self.extracted if self.extracted else '',
                'contratante': self.contratante if self.contratante else '',
                'contratada': self.contratada if self.contratada else '',
                'num_processo': self.num_process if self.num_process else ''
            }
        
            return {'success': True, 'message': 'Dados extraídos com sucesso', 'dados': dados_contrato}
        
        return {'success': False, 'message': 'Fazer modificações na imagem e tentar novamente'}


    def find_name(self):
        regex = r"nome\s*([^\n]+)"
        name = re.findall(regex, self.extracted.lower(), re.DOTALL)
        # print("nome do regex", name)
        if name:
            # print("Achou nome")
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

    def extract_rg_info(self):
        if self.attempt == 0:
            print("Carregando..")
            self._new_rg()
        if self.name is None:
            self.name = self.find_name()
        if self.rg_id is None:
            self.rg_id = self.find_rg()
        if self.born_date is None:
            self.born_date = self.find_born_date()
        if self.mother_name is None:  # Este não pode ser obrigatório
            self.mother_name = self.find_mother_name()
        if self.place_of_birth is None:
            self.place_of_birth = self.find_place_of_birth()

        if not all(
            [
                self.name,
                self.rg_id,
                self.born_date,
                self.mother_name,
                self.place_of_birth,
            ]
        ) and self.attempt < 20:
            print(f"{self.attempt * 5}%")
            self.attempt += 1
            self.thresh += 5
            self._new_rg()
            self.extract_rg_info()
        else:
            print("100%")        
        
        if not any(
            [
                self.name,
                self.rg_id,
                self.born_date,
                self.mother_name,
                self.place_of_birth,
            ]
        ):
            return {'success': False, 'message': 'Fazer modificações na imagem e tentar novamente'}
        
        dados_documento = {
            'nome_documento': self.name if self.name else '',
            'numero_rg': self.rg_id if self.rg_id else '',
            'data_nascimento': self.born_date if self.born_date else '',
            'nome_mae': self.mother_name if self.mother_name else '',
            'local_nascimento': self.place_of_birth if self.place_of_birth else ''
        }
        
        return {'success': True, 'message': 'Dados extraídos com sucesso', 'dados': dados_documento}


if __name__ == "__main__":
    ocr = OCR_DOCS("ambiente_virtual/contrato.pdf")
    ocr.extract_contract_info()
    # print(ocr.num_process)
    # print(ocr.num_process)
    '''
    Exemplo de uso
    ocr = OCR_DOCS("path")
    ocr.extract_contract_info()
    ou
    ocr.extract_rg_info()
    '''