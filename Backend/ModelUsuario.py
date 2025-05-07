from ConexionBasededatos import ConexionMysql

# Definición de la clase ModelUsuarios para interactuar con la base de datos
class ModelUsuarios:
    # Método constructor de la clase ModelUsuarios
    def __init__(self):
        # Inicializa la conexión a la base de datos
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    # Método para obtener la conexión a la base de datos
    def obtener_conexion(self):
        return self.mibasededatos
    
    # Método para obtener un usuario por su ID
    def obtener_usuario(self, id):
        self.cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    # Método para obtener todos los usuarios
    def obtener_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()
    
    # Método para insertar un nuevo usuario
    def insertar_usuario(self, nombre, email, contrasena):
        val = (nombre, email, contrasena)
        sql = "INSERT INTO usuarios (nombre, email, contrasena) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    # Método para actualizar un usuario existente
    def actualizar_usuario(self, id, nombre, email, contrasena):
        val = (nombre, email, contrasena, id)
        sql = "UPDATE usuarios SET nombre = %s, email = %s, contrasena = %s WHERE id = %s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    # Método para eliminar un usuario por su ID
    def eliminar_usuario(self, id):
        val = (id,)
        sql = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    # Método para cerrar la conexión a la base de datos
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

    # Método para verificar las credenciales de un usuario
    def verificarUsuario(self, email, password):
        val = (email, password)
        sql = "SELECT email, contrasena FROM usuarios WHERE email = %s AND contrasena = %s"
        self.cursor.execute(sql, val)
        user = self.cursor.fetchone()
        if user:
            return "index"
        else:
            return "contraseña incorrecta"