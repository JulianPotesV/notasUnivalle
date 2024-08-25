# main.py

from mysql_connection import MySQLConnection


db = MySQLConnection('config.json')
# Conectar a la base de datos
db.connect()
# Insertar datos en la tabla SEMESTRE
insert_query = "INSERT INTO SEMESTRE (Id_Semestre) VALUES (%s)"
db.execute_query(insert_query, ("2026A",))
db.execute_query(insert_query, ("2026B",))

# Obtener todos los semestres
select_query = "SELECT * FROM SEMESTRE"
resultados = db.fetch_all(select_query)
print(resultados)  # Imprimir todos los registros en la tabla SEMESTRE

# Cerrar la conexión a la base de datos
db.close()