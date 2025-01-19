# Arquitectura hexagonal con Python y FastAPI

## Índice

- [Arquitectura hexagonal con Python y FastAPI](#arquitectura-hexagonal-con-python-y-fastapi)
  - [Índice](#índice)
  - [Estructura de directorios](#estructura-de-directorios)
    - [**api/**](#api)
    - [**aplicacion/**](#aplicacion)
    - [**dominio/**](#dominio)
    - [**infraestructura/**](#infraestructura)
    - [**config**](#config)
    - [Diagrama de Dependencias](#diagrama-de-dependencias)
  - [Principios Clave](#principios-clave)
  - [Prueba la Demo](#prueba-la-demo)

Nuestro objetivo con la arquitectura hexagonal es cumplir los siguientes objetivos:

1. **Desacoplar el código**: Asegurar que las diferentes partes de la aplicación sean independientes y que los cambios en una capa no impacten directamente a otra.
2. **Facilitar la lectura y el mantenimiento**: Promover un código organizado y fácil de entender, permitiendo que nuevos desarrolladores puedan contribuir con rapidez.
3. **Fomentar un desarrollo limpio siguiendo los principios SOLID**:
    - **S**ingle Responsibility Principle (Responsabilidad única)
    - **O**pen/Closed Principle (Abierto/Cerrado)
    - **L**iskov Substitution Principle (Sustitución de Liskov)
    - **I**nterface Segregation Principle (Segregación de Interfaces)
    - **D**ependency Inversion Principle (Inversión de Dependencias)
4. **Capacidad de cambiar los servicios sin modificar el código central**: Permitir que los cambios en la infraestructura o servicios externos no afecten las capas centrales de la aplicación.

## Estructura de directorios

En esta arquitectura, separamos los componentes principales de la aplicación en directorios específicos, siguiendo el patrón de la arquitectura hexagonal:

### **api/**
Este directorio se encarga de definir los puntos de entrada de la aplicación. Aquí se gestionan los endpoints que exponen las funcionalidades a través de HTTP. Está organizado de la siguiente manera:

- **v[x]/**: Subcarpeta para manejar versiones de la API. Esto permite mantener múltiples versiones de la aplicación en producción de manera simultánea si fuese necesario.
  - **routers/**: Contiene el código de los endpoints o rutas de la aplicación. Cada endpoint es responsable de delegar la lógica a los casos de uso definidos en la capa de la aplicación.
  - **errors**: Contiene las definiciones y manejadores de errores específicos para las respuestas de los endpoints. Estos errores incluyen excepciones personalizadas, respuestas de error estándar y el formato de los mensajes de error para el cliente.

### **aplicacion/**
Contiene la lógica central de la aplicación. Esta capa agrupa los casos de uso y los servicios necesarios para implementar las funcionalidades del negocio.

- **use_case/**: Define los casos de uso de la aplicación. Un caso de uso es una acción específica del negocio que usa los servicios para cumplir su propósito. Aquí no hay lógica relacionada con infraestructura.
- **service/**: Define los servicios específicos que encapsulan la lógica del dominio, interactuando con la capa de infraestructura según sea necesario.

### **dominio/**
Hace referencia a la capa de dominio, la cual define los modelos centrales y las reglas de negocio. Aquí se almacenan:

- **Modelos de datos**: Representan las entidades principales de la aplicación (por ejemplo, `Usuario`, `Pedido`, etc.).
- **Reglas de negocio**: Métodos o validaciones que son intrínsecos al dominio.

Esta capa no tiene dependencias con la infraestructura ni con frameworks específicos.

### **infraestructura/**
Contiene las implementaciones específicas de los servicios necesarios por la aplicación. Aquí se define cómo la aplicación interactúa con herramientas externas como bases de datos, APIs externas, sistemas de mensajería, etc.

- **Base de datos**: Código relacionado con la interacción con bases de datos, como configuraciones de ORM o consultas SQL directas.
- **Servicios externos**: Implementaciones para consumir APIs externas, conectarse a colas de mensajes, almacenamiento en la nube, etc.
- **Entities**: La capa de Entities se encarga de gestionar los objetos DTO (Data Transfer Objects), los cuales funcionan como contenedores para transferir datos entre las diferentes capas de la aplicación. Su propósito principal es desacoplar los modelos de dominio de las capas externas, permitiendo una clara separación de responsabilidades. Estos objetos facilitan la validación, transformación y transporte de datos, asegurando que la lógica de negocio no dependa directamente de la estructura de los datos provenientes de fuentes externas o de otras capas. Un caso de uso típico sería cuando los datos recibidos de una solicitud o un servicio externo contienen información adicional que no será almacenada en la base de datos. En este escenario, los DTOs permiten estructurar, filtrar y transformar esos datos antes de ser procesados o enviados a otras partes de la aplicación.

### **config**
Este directorio contiene los archivos de configuración de la aplicación, organizados de la siguiente manera:

- **settings.py**: Archivo que define las configuraciones generales, como variables de entorno, conexiones a bases de datos y otros ajustes globales de la aplicación.
- **di**: Carpeta con la configuración de la inyección de dependencias. Aquí se definen los contenedores de dependencias que permiten instanciar las clases necesarias y resolver las dependencias requeridas por las capas.

### Diagrama de Dependencias
```plaintext
api -> aplicacion -> dominio <- infraestructura
```

## Principios Clave
1. **Inversión de dependencias**: La capa de dominio no debe depender de la infraestructura; en su lugar, la infraestructura depende del dominio.
2. **Separación de responsabilidades**: Cada capa tiene una responsabilidad clara y no se mezcla lógica de diferentes capas.
3. **Testabilidad**: Al estar desacopladas, las capas permiten realizar pruebas unitarias y de integración fácilmente, aislando dependencias externas.

## Prueba la Demo

Desde src ejecuta el siguiente comando

`````cmd
uvicorn app:app --reload
`````

Y acede al swagger de la aplicación para hacer tus pruebas con los endpoints en [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs#/)