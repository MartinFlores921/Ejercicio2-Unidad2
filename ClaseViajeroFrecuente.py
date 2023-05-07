class ViajeroFrecuente:
    __num_viajero = 0
    __dni = 0
    __nombre= ""
    __apellido= ""
    __millas_acum= 0
    def __init__(self, num, dni, nombre, apellido, millasAcum):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millasAcum
    def cantidadTotaldeMillas (self):
        return self.__millas_acum
    def acumularMillas(self, cant):
         self.__millas_acum += cant
         return self.__millas_acum
    def canjearMillas(self, cant_canje):
       if cant_canje <= self.__millas_acum:
           self.__millas_acum -= cant_canje
           return self.__millas_acum
       else: print("No se pudo realizar el canje \n")
   
    def getNumViajero(self):
        return self.__num_viajero