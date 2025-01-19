from pydantic import BaseModel

class UsuarioDTO(BaseModel):
    nombre: str

    def __str__(self):
        return f"UsuarioDTO(nombre={self.nombre})"