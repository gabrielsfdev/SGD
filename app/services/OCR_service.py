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
        self.place_of_birth = ""
        

    def new_rg(self):
        rgb = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        imagem_cinza = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
        bilateral = cv2.bilateralFilter(imagem_cinza, 20, 75, 75)
        cv2.imshow("bilateral", bilateral)
        margin = cv2.Canny(bilateral, 50, 100, apertureSize=3) # Apenas em desenvolvimento (não é necessário para o OCR)
        cv2.imshow("img", margin) # Apenas em desenvolvimento
        cv2.waitKey(0)

        self.extracted = pytesseract.image_to_string(imagem_cinza, lang='por', config='--psm 6')
    
    def find_name(self):
        regex = rf"nome (.+)"
        name = re.findall(regex, self.extracted.lower())
        # print("nome do regex", name)
        if name:
            return name[0].upper()
    
    def find_rg(self):
        regex = r"registro (\d{2}[.]\d{3}[.]\d{3}[-]\d{2})"
        rg = re.findall(regex, self.extracted.lower(), re.DOTALL)
        print("rg do regex", rg) # Apenas para debug
        if rg:
            return rg[0]
        else:
            regex = r"registro (\d{2}[.]\d{3}[.]\d{3}[-]\d{1})\b"
            rg = re.findall(regex, self.extracted.lower(), re.DOTALL)
            if rg:
                return rg[0]
            
    def find_born_date(self):
        regex = r"nascimento.*?\s*(\d{2}[/]\d{2}[/]\d{4})"
        born_date = re.findall(regex, self.extracted.lower(), re.DOTALL)
        print("nascimento do regex", born_date) # Apenas para debug
        if born_date:
            return born_date[0]
        
    def find_mother_name(self):
        regex = r"filiação.*?\s*\n(.+)"
        mother_name = re.findall(regex, self.extracted.lower())
        print("nome da mãe", mother_name) # Apenas para debug
        if mother_name:
            return mother_name[0].upper()
    
    def find_place_of_birth(self):
        regex = r"naturalidade.*?\n([^\s]+) "
        place_of_birth = re.findall(regex, self.extracted.lower())
        return place_of_birth[0].upper()

    def extract_info(self):
        if self.name == "":
            self.name = self.find_name()
        if self.Rg_id == "":
            self.Rg_id = self.find_rg()
        if self.born_date == "":
            self.born_date = self.find_born_date()
        if self.mother_name == "": # Este não pode ser obrigatório
            self.mother_name = self.find_mother_name()
        if self.place_of_birth == "":
            self.place_of_birth = self.find_place_of_birth()

        if not all([self.name, self.Rg_id, self.born_date, self.mother_name, self.place_of_birth]):
            return "Fazer modificações na imagem e tentar novamente"
