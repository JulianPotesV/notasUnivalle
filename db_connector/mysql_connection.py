import mysql.connector
import json

class MySQLConnection:
    def __init__(self, config_file):
        self.config = self._load_config(config_file)
        self.connection = None

    def _load_config(self, config_file):
        """Carga la configuración desde un archivo JSON."""
        with open(config_file, 'r') as file:
            return json.load(file)

    def connect(self):
        """Conecta a la base de datos utilizando la configuración proporcionada."""
        try:
            self.connection = mysql.connector.connect(
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.config['database']
            )
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")

    def execute_query(self, query, params=None):
        """Ejecuta una consulta en la base de datos."""
        if self.connection is None:
            print("No estás conectado a ninguna base de datos.")
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            if cursor.with_rows:
                results = cursor.fetchall()  # Leer todos los resultados si existen
            else:
                results = None
            self.connection.commit()
            print("Consulta ejecutada exitosamente.")
            return results
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return None
        finally:
            cursor.close()

    def fetch_all(self, query, params=None):
        """Ejecuta una consulta y devuelve todos los resultados."""
        return self.execute_query(query, params)

    def fetch_one(self, query, params=None):
        """Ejecuta una consulta y devuelve el primer resultado."""
        results = self.execute_query(query, params)
        if results:
            return results[0] if results else None
        return None

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")