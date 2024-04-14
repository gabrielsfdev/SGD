## Models: Diretório onde será estruturado todo o código relacionado à conexão e comunicação com o Banco de Dados.
# Centralização das dependencias do módulo "models" para importação
from .usuario import UsuarioBD
from .endereco import EnderecoBD
from .cidade import CidadeBD
from .telefone import TelefoneBD
from .email import EmailBD
from .setor import SetorBD
from .escritorio import EscritorioBD
from .arquivo import ArquivoBD
from .arquivoblob import ArquivoBlobBD

__all__ = [
        'UsuarioBD',
        'EnderecoBD',
        'CidadeBD',
        'TelefoneBD',
        'EmailBD',
        'SetorBD',
        'EscritorioBD',
        'ArquivoBD',
        'ArquivoBlobBD'
        ]