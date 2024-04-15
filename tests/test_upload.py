import os
import sys
sys.path.append(os.getenv('CAMINHO_RAIZ_PROJETO'))

from app.services import Arquivo

def main_upload():
    upload = Arquivo()
    caminho = input('Informe o caminho do arquivo: ')
    result = upload.upload_arquivo(caminho)
    
    return result

if __name__ == "__main__":
    upload = main_upload()