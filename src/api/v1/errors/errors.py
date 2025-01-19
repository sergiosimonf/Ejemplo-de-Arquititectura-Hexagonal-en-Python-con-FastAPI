from pydantic import BaseModel

class APIErrorMessage(BaseModel): # Modelo para estructurar y validar mensajes de error en APIs.
    type: str
    message: str