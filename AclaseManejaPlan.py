from ClasePlanAhorro import PlanAhorro
import csv
class ManejadorPlan:
    def __init__(self):
        self.__ListaPlan = []
    def agregarPlan(self,unPlan):
        self.__ListaPlan.append(unPlan)
    def actualizar(self):
        for i in range(len(self.__ListaPlan)):
            print('Codigo del plan:%d'%self.__ListaPlan[i].cod)
            print('Modelo del Vehiculo:%s'%self.__ListaPlan[i].modelo)
            print('Version del vehiculo:%s'%self.__ListaPlan[i].version)
            print('Valor Actual del vehiculo:%f'%self.__ListaPlan[i].valor)
            self.__ListaPlan[i].valor=float(input('Ingrese el nuevo valor del vehiculo'))
            print('Nuevo valor del vehiculo: %f'%self.__ListaPlan[i].valor)

    def mostrarDatos(self,i):
        for j in range(len(self.__ListaPlan)):
            if (self.__ListaPlan[j].valor<=1):
                print('Codigo del plan:%d'%self.__ListaPlan[j].cod)
                print('Modelo del Vehiculo:%s'%self.__ListaPlan[j].modelo)
                print('Version del vehiculo:%s'%self.__ListaPlan[j].version)

    def mostarMonto(self):
        for i in range(len(self.__ListaPlan)):
            print('El monto que debe haber pagado para licitar el vehiculo es: %f'%(self.__ListaPlan[i].CantCuoLic*((self.__ListaPlan[i].valor/self.__ListaPlan[i].CantCuotas)-self.__ListaPlan[i].valor)))

    def modificarCantLicitar(self,i):
        PlanAhorro.CantCuoLic = i







