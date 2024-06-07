import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='32893064',
    host='localhost',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Digite un número para el id_persona: ')
            cursor.execute(sentencia, (id_persona,))
            registro = cursor.fetchall()
            print(registro)
except Exception as e:
    print(f'Salió mal por este motivo: {e}')
finally:
    conexion.close()

cursor.close()
conexion.close()