from sqlalchemy.exc import IntegrityError
import bcrypt
from app.models import UsuarioBD, EnderecoBD, TelefoneBD, EmailBD, CidadeBD, PerfilUsuarioBD
from app.database import SessionLocal

class Usuario:
    def __init__(self, login, senha, nome=None, cpf=None, datanascimento=None):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.cpf = cpf
        self.datanascimento = datanascimento

    def registrar_usuario(self, telefone, email, cep, logradouro, numero, complemento, bairro, cidade, idperfil=3):
        with SessionLocal() as session:
            senha_hashed = bcrypt.hashpw(self.senha.encode(), bcrypt.gensalt())
            novo_usuario = UsuarioBD(
                nome_usuario=self.nome,
                cpf_usuario=self.cpf,
                datanascimento=self.datanascimento,
                login=self.login,
                senha=senha_hashed.decode()
            )
            session.add(novo_usuario)
            try:
                session.flush()
                
                id_cidade = session.query(CidadeBD).filter(CidadeBD.nome_cidade == cidade).first()
                
                novo_telefone = TelefoneBD(numero_telefone=telefone, idusuario=novo_usuario.id)
                novo_email = EmailBD(email=email, idusuario=novo_usuario.id)
                novo_endereco = EnderecoBD(cep=cep, logradouro=logradouro, numero=numero, complemento=complemento, bairro=bairro, idcidade=id_cidade.id, idusuario=novo_usuario.id)
                novo_perfilusuario = PerfilUsuarioBD(idusuario=novo_usuario.id, idperfil=idperfil)
                
                session.add(novo_telefone)
                session.add(novo_email)
                session.add(novo_endereco)
                session.add(novo_perfilusuario)
                
                session.commit()
                return {'message': 'Usuário cadastrado com sucesso!', 'id': novo_usuario.id}
            except IntegrityError:
                session.rollback()
                return {'message': 'Erro ao cadastrar usuário. Login ou e-mail já existente.'}


    def login_usuario(self):
        session = SessionLocal()
        
        try:
            if '@' in self.login:
                usuario = (session.query(UsuarioBD)
                            .join(EmailBD, UsuarioBD.id == EmailBD.idusuario)
                            .filter(EmailBD.email == self.login)
                            .first())
            else:
                usuario = session.query(UsuarioBD).filter(UsuarioBD.login == self.login).first()
            
            if usuario:
                if bcrypt.checkpw(self.senha.encode('utf-8'), usuario.senha.encode('utf-8')):
                    from app.services import Sessao
                    sessao = Sessao()
                    sessao.registra_sessao(usuario)
                    return {'success': True, 'message': 'Login realizado com sucesso.', 'usuario': usuario}
                else:
                    return {'success': False, 'message': 'Senha incorreta.'}
            else:
                return {'success': False, 'message': 'Usuário não encontrado.'}
        finally:
            session.close()
            
