from AclaseManejaPlan import ManejadorPlan
from ClasePlanAhorro import PlanAhorro

import csv
def crear(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                cod=fila[0]
                modelo=fila[1]
                version=fila[2]
                valor=fila[3]
                CantCuotas=fila[4]
                CantCuoLic=fila[5]
                unPlan=PlanAhorro(cod,modelo,version,valor,CantCuotas,CantCuoLic)
                self.agregarPlan(unPlan)
        archivo.close()
def menu():
    i=0
    while(i!=5):
        print('Ingrese el numero:')
        print('1 Actualizar el valor del vehiculo de cada plan')
        print('2 Mostrar vehiculo de menor valor al ingreso')
        print('3 Monto de licitar un vehiculo')
        print('4 Modificar cantidad de cuota para licitar un Vehiculo')

        i=int(input())

    if(i==1):
        m.actualizar()
    if(i==2):
        i=float(input('ingrese el valor'))
        m.mostrarDatos(i)
    if(i==3):
        m.mostarMonto()
    if(i==4):
        i=int(input('Ingrese el codigo de plan'))
        m.modificarCantLicitar(i)
        i=0
if __name__ == '__main__':
    m=ManejadorPlan()
    m.crear()



