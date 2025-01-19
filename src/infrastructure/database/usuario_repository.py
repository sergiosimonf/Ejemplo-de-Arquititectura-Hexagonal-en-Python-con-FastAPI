from abc import ABC, abstractmethod
from domain.users.usuario import Usuario
from infrastructure.entities.usuario_dto import UsuarioDTO


class IUsuarioRepository(ABC):
    @abstractmethod
    def create(self, user: UsuarioDTO) -> Usuario:
        pass
    

class UsuarioRepository(IUsuarioRepository):
    def __init__(self) -> None:
        self._userRepo = []
    
    def create(self, user: UsuarioDTO) -> Usuario:
        # Mapping de usuario DTO a usuario de dominio
        usuario = Usuario(nombre=user.nombre)
        self._userRepo.append(usuario)
        return usuario  # Devolver el objeto Usuario creado
    
    def __str__(self) -> str:
        # Representación en cadena para depurar el repositorio
        return f"UsuarioRepository(con {len(self._userRepo)} usuarios)"