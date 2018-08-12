# Importamos la clase 
import sqlite3

# Establecer la conexion 

con = sqlite3.connect('armando.db')

# ruta
# con = sqlite3.connect('c:\user\usuario1\desktop\armando.db')

# Crear Cursor 

cursor = con.cursor()

# Crear Tablas 

cursor.execute(
	''' 
		CREATE TABLE USUARIO (
			ID INT PRIMARY KEY NOT NULL,
			NOMBRE TEXT NOT NULL
		) 

	'''
	)