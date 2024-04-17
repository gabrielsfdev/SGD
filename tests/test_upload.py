import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))

from app.services import Arquivo

def main_upload():
    upload = Arquivo()
    caminho = input('Informe o caminho do arquivo: ')
    result = upload.upload_arquivo(caminho)
    
    return result

if __name__ == "__main__":
    upload = main_upload()