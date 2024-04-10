## Models: Diretório onde será estruturado todo o código relacionado à conexão e comunicação com o Banco de Dados.
# Centralização das dependencias do módulo "models" para importação
from .usuario import UsuarioBD
from .endereco import EnderecoBD
from .cidade import CidadeBD
from .telefone import TelefoneBD
from .email import EmailBD

__all__ = ['UsuarioBD', 'EnderecoBD', 'CidadeBD', 'TelefoneBD', 'EmailBD']