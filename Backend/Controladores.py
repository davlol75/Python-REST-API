from ModelUsuario import ModelUsuarios
from ModelProducto import ModelProductos
from flask_login import LoginManager
from flask import Flask, jsonify, request
from flask_cors import CORS

# Inicializa la aplicación Flask
app = Flask(__name__)
# Configuración de la clave secreta para la aplicación Flask
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

# Habilita CORS para permitir solicitudes desde otros dominios
CORS(app)

# Instancias de los modelos para manejar usuarios y productos
usuarios = ModelUsuarios()
productos = ModelProductos()

#****************************************************************
# Rutas relacionadas con los usuarios

# Ruta para el inicio de sesión de usuario
@app.route('/login', methods=['POST'])
def loginUsuario():
    # Obtiene las credenciales del cuerpo de la solicitud
    email = request.json['email']
    contrasena = request.json['contrasena']
    # Verifica las credenciales del usuario
    resultado = usuarios.verificarUsuario(email, contrasena)
    return jsonify({"mensaje": resultado})

# Ruta para listar todos los usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    # Devuelve la lista de todos los usuarios
    return jsonify(usuarios.obtener_usuarios())

# Ruta para listar un usuario por su ID
@app.route('/usuario/<int:id>', methods=['GET'])
def listar_usuario(id):
    # Devuelve los datos de un usuario específico
    return jsonify(usuarios.obtener_usuario(id))

# Ruta para crear un nuevo usuario
@app.route('/nuevo_usuario', methods=['POST'])
def crear_usuario():
    # Obtiene los datos del nuevo usuario del cuerpo de la solicitud
    nombre = request.json['nombre']
    email = request.json['email']
    contrasena = request.json['contrasena']
    # Inserta el nuevo usuario en la base de datos
    usuarios.insertar_usuario(nombre, email, contrasena)
    return jsonify({"mensaje": "Usuario creado exitosamente"})

# Ruta para actualizar un usuario existente
@app.route('/actualizar_usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    # Obtiene los datos a actualizar del cuerpo de la solicitud
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    contrasena = data.get('contrasena')
    
    # Verifica si se han proporcionado datos para actualizar
    if nombre is None and email is None and contrasena is None:
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400
    
    # Verifica si el usuario existe
    usuario_existente = usuarios.obtener_usuario(id)
    
    if usuario_existente:
        # Actualiza los datos del usuario
        usuarios.actualizar_usuario(id, nombre, email, contrasena)
        return jsonify({"mensaje": "Usuario actualizado correctamente"})
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

# Ruta para eliminar un usuario por su ID
@app.route('/eliminar_usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    # Verifica si el usuario existe antes de eliminarlo
    if usuarios.obtener_usuario(id):
        usuarios.eliminar_usuario(id)
        return jsonify({"mensaje": "Usuario eliminado correctamente"})
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

#****************************************************************
# Rutas relacionadas con los productos

# Ruta para listar todos los productos
@app.route('/productos', methods=['GET'])
def listar_productos():
    # Devuelve la lista de todos los productos
    return jsonify(productos.obtener_productos())

# Ruta para listar un producto por su ID
@app.route('/producto/<int:id>', methods=['GET'])
def listar_producto(id):
    # Devuelve los datos de un producto específico
    return jsonify(productos.obtener_producto(id))

# Ruta para crear un nuevo producto
@app.route('/nuevo_producto', methods=['POST'])
def crear_producto():
    # Obtiene los datos del nuevo producto del cuerpo de la solicitud
    nombre = request.json['nombre']
    precio = request.json['precio']
    # Inserta el nuevo producto en la base de datos
    productos.insertar_producto(nombre, precio)
    return jsonify({"mensaje": "Producto creado exitosamente"})

# Ruta para actualizar un producto existente
@app.route('/actualizar_producto/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    # Obtiene los datos a actualizar del cuerpo de la solicitud
    data = request.json
    nombre = data.get('nombre')
    precio = data.get('precio')
    
    # Verifica si se han proporcionado datos para actualizar
    if nombre is None and precio is None:
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400
    
    # Verifica si el producto existe
    producto_existente = productos.obtener_producto(id)
    
    if producto_existente:
        # Actualiza los datos del producto
        productos.actualizar_producto(id, nombre, precio)
        return jsonify({"mensaje": "Producto actualizado correctamente"})
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

# Ruta para eliminar un producto por su ID
@app.route('/eliminar_producto/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    # Verifica si el producto existe antes de eliminarlo
    if productos.obtener_producto(id):
        productos.eliminar_producto(id)
        return jsonify({"mensaje": "Producto eliminado correctamente"})
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

#****************************************************************
# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Ejecuta la aplicación en modo de depuración
    app.run(debug=True)