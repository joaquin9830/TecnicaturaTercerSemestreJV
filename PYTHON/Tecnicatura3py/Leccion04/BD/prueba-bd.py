import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='32893064',
    host='localhost',
    port='5432',
    database='test_bd'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registro = cursor.fetchall()
print(registro)

cursor.close()
conexion.close()