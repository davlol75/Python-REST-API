from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 

# Definición de la clase User que hereda de UserMixin
class User(UserMixin):
    # Método constructor de la clase User
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id  # Identificador del usuario
        self.name = name  # Nombre del usuario
        self.email = email  # Correo electrónico del usuario
        # Genera un hash de la contraseña proporcionada
        self.password = generate_password_hash(password)
        self.is_admin = is_admin  # Indica si el usuario es administrador

    # Método para establecer una nueva contraseña
    def set_password(self, password):
        # Genera un hash de la nueva contraseña y la asigna al atributo password
        self.password = generate_password_hash(password)

    # Método para verificar la contraseña proporcionada
    def check_password(self, password):
        # Compara la contraseña proporcionada con el hash almacenado
        return check_password_hash(self.password, password)
    
    # Método para representar el objeto User como una cadena
    def __repr__(self):
        # Devuelve una representación en cadena del usuario
        return '<user {}>'.format(self.email)
