from ConexionBasededatos import ConexionMysql

# Definición de la clase Modelproductos para interactuar con la base de datos
class ModelProductos:
    # Método constructor de la clase Modelproductos
    def __init__(self):
        # Inicializa la conexión a la base de datos
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    # Método para obtener la conexión a la base de datos
    def obtener_conexion(self):
        return self.mibasededatos
    
    # Método para obtener un producto por su ID
    def obtener_producto(self, id):
        self.cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    # Método para obtener todos los productos
    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()
    
    # Método para insertar un nuevo producto
    def insertar_producto(self, nombre, precio):
        val = (nombre, precio)
        sql = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    # Método para actualizar un producto existente
    def actualizar_producto(self, id, nombre, precio):
        val = (nombre, precio, id)
        sql = "UPDATE productos SET nombre = %s, precio = %s WHERE id = %s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    # Método para eliminar un producto por su ID
    def eliminar_producto(self, id):
        val = (id,)
        sql = "DELETE FROM productos WHERE id = %s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    # Método para cerrar la conexión a la base de datos
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()