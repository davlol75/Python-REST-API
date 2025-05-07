# API RESTful con Flask - CRUD de Productos y Usuarios

Este proyecto es una API REST desarrollada en Python con Flask, que permite gestionar productos y usuarios mediante operaciones CRUD. La interfaz web está hecha en HTML y conecta con la API para realizar las operaciones.

## 🧰 Tecnologías utilizadas

- Python 3
- Flask
- HTML / CSS
- Bootstrap
- MySQL / SQLite

## 📁 Estructura del proyecto

- `Backend/`: Contiene la lógica del servidor y conexión a la base de datos.
- `Frontend/`: Contiene los archivos HTML y CSS del panel.
- `DB/`: Script SQL para generar la base de datos.
- `requirements.txt`: Lista de dependencias.

## 🚀 Funcionalidades

- Crear, leer, actualizar y eliminar productos.
- Crear, leer, actualizar y eliminar usuarios.
- Autenticación básica (login).
- Panel web con conexión al backend.

## 💻 Cómo ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/davlol75/Python-REST-API
cd api-crud-flask

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la app
python Backend/Userlogin.py  # O el archivo que contenga app.run()
