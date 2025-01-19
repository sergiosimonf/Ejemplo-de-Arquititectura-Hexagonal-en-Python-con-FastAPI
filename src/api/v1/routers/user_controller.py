from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from api.v1.errors.errors import APIErrorMessage
from infrastructure.entities.usuario_dto import UsuarioDTO
from domain.users.usuario import Usuario
from application.use_case.crear_usuario import (ICrearUsuario, CrearUsuario)
from config.di.di import injector

router = APIRouter()

@router.post(
    "/user",
    response_model=UsuarioDTO,
    responses={400: {"model": APIErrorMessage}, 500: {"model": APIErrorMessage}},
    tags=["clients"],
)
async def create_client(
    request: Usuario, 
    service: CrearUsuario = Depends(lambda: injector.get(ICrearUsuario))
) -> JSONResponse:
    result = service.create(request)
    return JSONResponse(content=result.nombre, status_code=status.HTTP_201_CREATED)