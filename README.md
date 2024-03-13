# Proyecto Mercado Liebre

Este proyecto es una versión cómica de Mercado Libre, desarrollada con Django, un framework web de Python.

## Descripción del Proyecto

El objetivo de este proyecto es crear una plataforma similar a Mercado Libre, pero con un toque humorístico. La aplicación permitirá a los usuarios ver una lista de productos, buscar productos en la base de datos, ver detalles de productos individuales, y agregar nuevos productos, categorías y vendedores.

## Estructura del Proyecto

El proyecto sigue la estructura típica de un proyecto Django:

- `nuevoproyecto`: Carpeta principal del proyecto Django.
- `mercado_liebre`: Aplicación principal que contiene la lógica del proyecto.
  - `models.py`: Define los modelos de la base de datos.
  - `views.py`: Contiene las vistas de Django para manejar las solicitudes del usuario.
  - `forms.py`: Define los formularios de Django para la entrada de datos del usuario.
  - `urls.py`: Configura las URL de la aplicación.
  - `templates/`: Carpeta que contiene las plantillas HTML para renderizar las páginas.
- `README.md`: Este archivo que proporciona información sobre el proyecto.

## Funcionalidades Implementadas

- Herencia de HTML: Las plantillas HTML se heredan para mantener una estructura común en todas las páginas.
- Tres clases en `models.py`: Se han definido las clases Producto, Categoria y Vendedor en `models.py`.
- Formularios para insertar datos: Se han creado formularios para agregar nuevos productos, categorías y vendedores.
- Formulario para buscar: Se ha implementado un formulario de búsqueda para buscar productos en la base de datos.
