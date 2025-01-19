from injector import inject
from abc import ABC, abstractmethod

from application.services.usuario_service import IUsuarioService
from infrastructure.entities.usuario_dto import UsuarioDTO
from domain.users.usuario import Usuario

class ICrearUsuario(ABC):
    @abstractmethod
    def create(self, input_dto: UsuarioDTO) -> Usuario:
        pass

@inject
class CrearUsuario:
    def __init__(self, usuario_service: IUsuarioService):
        self.usuario_service = usuario_service
        
    def create(self, input_dto: UsuarioDTO) -> Usuario:
        usuario = self.usuario_service.create(input_dto)
        return usuario