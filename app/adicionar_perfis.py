import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
from sqlalchemy.orm import sessionmaker
from app import engine
from app.models import PerfilBD

Session = sessionmaker(bind=engine)
session = Session()

def insere_perfis():
    perfis = [{'nome': 'Admin'},{'nome': 'Operador'},{'nome': 'Usuario'}]

    for perfil_info in perfis:
        perfil = PerfilBD(nome_perfil=perfil_info['nome'])
        session.add(perfil)

    session.commit()
    session.close()