from injector import inject, Injector, Module, singleton
from application.services.usuario_service import (UsuarioService, IUsuarioService)
from application.use_case.crear_usuario import (ICrearUsuario, CrearUsuario)
from infrastructure.database.usuario_repository import (IUsuarioRepository, UsuarioRepository)

class AppModule(Module):
    def configure(self, binder):
        binder.bind(IUsuarioService, to=UsuarioService, scope=singleton)
        binder.bind(ICrearUsuario, to=CrearUsuario, scope=singleton)
        binder.bind(IUsuarioRepository, to=UsuarioRepository, scope=singleton)
        
injector = Injector(AppModule)