import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
from sqlalchemy.orm import sessionmaker
from app import engine
from app.models import CidadeBD
import json

Session = sessionmaker(bind=engine)
session = Session()

def popula_tabela_cidade():
    with open('app/data/cidades.json', 'r', encoding='utf-8') as file:
        dados = json.load(file)
        for info in dados:
            cidade = CidadeBD(nome_cidade=info['nome'], uf=info['uf'])
            session.add(cidade)

    session.commit()
    session.close()

