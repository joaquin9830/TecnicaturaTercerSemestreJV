class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self._nombre}'

    @property #Getter
    def nombre(self):
        return self._nombre

    @nombre.setter #Setter
    def nombre(self, nombre):
        self._nombre = nombre
