import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))

from app.services import Arquivo

arquivos = Arquivo()
busca = arquivos.busca_arquivo('nome_arquivo', 'hansei')

if busca:
    for arquivo in busca['arquivos']:
        print(f'ID: {arquivo.id} - Nome: {arquivo.nome_arquivo}')
    
    while True:
        opcao = int(input('Informe o ID do arquivo que deseja baixar (0 para sair.): '))
        if opcao == 0:
            break
        
        arquivo = [i for i in busca['arquivos'] if i.id == opcao]
        download = arquivos.download_arquivo(opcao, arquivo[0].nome_arquivo)
        print(download)
