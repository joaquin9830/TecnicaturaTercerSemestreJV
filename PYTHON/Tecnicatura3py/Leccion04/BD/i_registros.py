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
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'carlitos@mail.com')
            cursor.execute(sentencia, valores)
            #conexion.commit()
            registros_insetados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insetados}')
except Exception as e:
    print(f'Salió mal por este motivo: {e}')
finally:
    conexion.close()

cursor.close()
conexion.close()