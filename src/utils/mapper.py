from domain.users.usuario import Usuario
from infrastructure.entities.usuario_dto import UsuarioDTO

def map_usuario_dto_to_usuario(dto: UsuarioDTO) -> Usuario:
    return Usuario(nombre=dto.nombre)