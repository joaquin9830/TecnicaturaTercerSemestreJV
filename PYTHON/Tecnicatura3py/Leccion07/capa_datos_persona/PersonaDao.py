class PersonaDAO:
    """
    DAO-> Data Access Object
    CRUD-> Create > Insertar
           Read > Seleccionar
           Update > Actualizar
           Delete > Eliminar
    """

    _SELECCIONAR = 'SELECT * FROM persona Order by id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
    