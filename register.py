import sqlite3
from getpass import getpass
from cryptography.fernet import Fernet

conexion = sqlite3.connect("database.db")

cursor = conexion.cursor()

Usuario = input("Username: ")
firsAttempPassword = getpass("Password: ")
secondAttempPassword = getpass("Verify Password: ")

if firsAttempPassword != secondAttempPassword:
  print("las contraseñas no coinciden")
  exit

clave = b'D-Ynfqjk9zMEtmQXZFor6BIVTdstax4VViyvgMq0n4o='
cipher_suite = Fernet(clave)

encriptPassword = cipher_suite.encrypt(secondAttempPassword.encode("utf-8"))

cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)",(Usuario,encriptPassword))
conexion.commit()