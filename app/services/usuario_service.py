from sqlalchemy.exc import IntegrityError
import bcrypt
from app.models import UsuarioBD, EnderecoBD, TelefoneBD, EmailBD
from app.database import SessionLocal

class Usuario:
    def __init__(self, login, senha, nome=None, cpf=None, datanascimento=None):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.cpf = cpf
        self.datanascimento = datanascimento

    def registrar_usuario(self, telefone, email, logradouro, numero, complemento, bairro, idcidade):
        with SessionLocal() as session:
            senha_hashed = bcrypt.hashpw(self.senha.encode(), bcrypt.gensalt())
            novo_usuario = UsuarioBD(
                nome=self.nome,
                cpf=self.cpf,
                datanascimento=self.datanascimento,
                login=self.login,
                senha=senha_hashed.decode()
            )
            session.add(novo_usuario)
            try:
                session.flush()
                
                novo_telefone = TelefoneBD(telefone=telefone, idusuario=novo_usuario.id)
                novo_email = EmailBD(email=email, idusuario=novo_usuario.id)
                novo_endereco = EnderecoBD(logradouro=logradouro, numero=numero, complemento=complemento, bairro=bairro, idcidade=idcidade, idusuario=novo_usuario.id)
                
                session.add(novo_telefone)
                session.add(novo_email)
                session.add(novo_endereco)
                
                session.commit()
                return {'message': 'Usuário cadastrado com sucesso!', 'id': novo_usuario.id}
            except IntegrityError:
                session.rollback()
                return {'message': 'Erro ao cadastrar usuário. Login ou e-mail já existente.'}