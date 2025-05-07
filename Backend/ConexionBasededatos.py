import mysql.connector
from mysql.connector import Error

# Definición de la clase ConexionMysql para manejar la conexión a la base de datos
class ConexionMysql:
    def __init__(self):
        try:
            # Intenta establecer la conexión a la base de datos MySQL
            self.mibasededatos = mysql.connector.connect(
                host="localhost",
                port="3306",
                user="root",
                password="",  # Cambiado de passwd a password
                database="prueba"
            )

            self.conexion = self.mibasededatos
            self.cursor = self.conexion.cursor()
            
            # Verifica si la conexión fue exitosa
            if self.mibasededatos.is_connected():
                db_Info = self.mibasededatos.get_server_info()
                print(f"Connected to MySQL Server version: {db_Info}")
            
        except Error as e: 
            # Maneja cualquier error que ocurra durante la conexión
            print(f"Error while connecting to MySQL: {e}")

    # Método para cerrar la conexión a la base de datos
    def cerrar_conexion(self):
        if self.mibasededatos.is_connected():
            self.cursor.close()
            self.conexion.close()
            print("MySQL connection is closed")

# Código de prueba para verificar la conexión
if __name__ == "__main__":
    conexion = ConexionMysql()
    conexion.cerrar_conexion()  # Añadido paréntesis para ejecutar la función