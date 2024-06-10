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
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan Carlos', 'Roldan', 'rcarlos@email.com', 3),
                ('Romina', 'Ayala', 'rominatumamurri@email.com', 2)
            )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')
except Exception as e:
    print(f'Salió mal por este motivo: {e}')
finally:
    conexion.close()

cursor.close()
conexion.close()