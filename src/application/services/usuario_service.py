from injector import inject
from abc import ABC, abstractmethod

from domain.users.usuario import Usuario
from infrastructure.entities.usuario_dto import UsuarioDTO
from infrastructure.database.usuario_repository import IUsuarioRepository


class IUsuarioService(ABC):
    @abstractmethod
    def create(self, user: UsuarioDTO) -> Usuario:
        pass
    
@inject
class UsuarioService(IUsuarioService):
    def __init__(self,repository: IUsuarioRepository):
        self.repository = repository
    
    def create(self, user: UsuarioDTO) -> Usuario:
        user = self.repository.create(user)
        return user