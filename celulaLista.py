class CelulaLista:
    def __init__(self, elemento, proxima, anterior):
        self.__elemento = elemento
        self.__proxima = proxima
        self.__anterior = anterior

    #elemento
    @property
    def elemento(self):
        return self.__elemento 
    
    #proxima
    @property
    def proxima(self):
        return self.__proxima 
    @proxima.setter
    def proxima(self, valor):
        self.__proxima = valor
    
    #anterior
    @property
    def anterior(self):
        return self.__anterior 
    @anterior.setter
    def anterior(self, valor):
        self.__anterior = valor
    


    def __str__(self):
        return self.__elemento