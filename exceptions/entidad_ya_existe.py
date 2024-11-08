class EntidadYaExiste(Exception):
    
    def __init__(self,descripcion):
        self.__descripcion = descripcion
        super().__init__(self.__descripcion)