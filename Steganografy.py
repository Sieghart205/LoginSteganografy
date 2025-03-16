from cryptography.fernet import Fernet
import sqlite3
from getpass import getpass
from stegano import lsb

# Solicitar credenciales al usuario
user = input("Usuario: ")
password = getpass("Contraseña: ")

conexion = sqlite3.connect("database.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM Users WHERE Username = ?", (user,))
data = cursor.fetchall()

if not data:
    print("Usuario no encontrado.")
    exit()

clave = b'D-Ynfqjk9zMEtmQXZFor6BIVTdstax4VViyvgMq0n4o='
cipher_suite = Fernet(clave)

try:
    password_encriptada = data[0][2]  # Suponiendo que la contraseña está en la segunda columna
    password_desencriptada = cipher_suite.decrypt(password_encriptada).decode('utf-8')

    if password_desencriptada == password:
        print("Sesión iniciada.")
        
        data = input("dime el mensaje que deseas ocultar: ")
        image = input("dame el nombre de la imagen que deseas usar: ")
        newImageName = input("dame el nombre de la nueva imagen: ")

        image = lsb.hide(image,data)
        image.save(newImageName)
    else:
        print("Contraseña incorrecta.")
        exit()

except Exception as e:
    print(f"Error al desencriptar: {e}")
    exit()

finally:
    conexion.close()