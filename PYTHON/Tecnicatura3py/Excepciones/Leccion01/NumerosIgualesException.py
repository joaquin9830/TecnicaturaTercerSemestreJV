class NumerosIgualesException(Exception): #Extiende de la clase
    def __init__(self, mensaje):
        self.messagee = mensaje