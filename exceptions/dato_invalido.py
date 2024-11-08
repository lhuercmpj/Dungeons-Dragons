class DatoInvalido(Exception):
    def __init__(self, mensaje):
        self.__mensaje = mensaje
        super().__init__(self.__mensaje)