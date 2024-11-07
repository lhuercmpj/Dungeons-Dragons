class EntidadNoExiste(Exception):
    
    def __init__(self,descripcion):
        self.__descripcion = descripcion
        super().__init__(descripcion)