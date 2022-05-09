class PlanAhorro:
    CantCuotas = 12
    CantCuoLic = 6

    def __init__(self, cod=1, modelo='', version= '', valor=0.0):
        self.__cod = cod
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
    def __str__(self,):
        return 'Datos del Plan del Vehiculo: Codigo del plan: %d Modelo : %s Version: %s Valor: %f Cantidad de Cuotas: %d Cantidad de cuotas para licitar el vehiculo %d '%(self.__cod, self.__modelo, self.__valor, self.getCantCuotas(), self.__getCantCuoLic())

    #METODOS DE INSTANCIA
    def getCod(self):
        return self.__cod
    def getMod(self):
        return self.__modelo
    def getVer(self):
        return self.__version
    def getValor(self):
        return self.__valor
    #METODOS DE CLASE
    @classmethod
    def getCantCuotas(cls):
        return cls.CantCuotas
    def getCantCuoLic(cls):
        return cls.CantCuoLic



