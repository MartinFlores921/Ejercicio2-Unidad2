
import csv
from ClaseViajeroFrecuente import ViajeroFrecuente
from menu import menu_1

"""def test():
    m = ViajeroFrecuente(4783, '43.242.2424', 'mauri', 'mama', 492283)
    print(m.getmillas())
    print('su nombre es {}' .format(m.getnombrecompleto()))
    m.acumularMillas(int(input('ingrese las millas a acumular:')))
    m.canjearMillas(int(input('Ingrese las millas a canjear:')))"""
if __name__ == "__main__":
   # test()
    archivo= open("Viajeros.csv")
    reader = csv.reader(archivo, delimiter= ";")
    lista = []
    next(reader)
    for fila in reader:
        num = int(fila[0])
        dni = int(fila[1])
        nombre= str(fila[2])
        apellido= str(fila[3])
        millasAcum= int(fila[4])
        viajero = ViajeroFrecuente(num,dni,nombre, apellido, millasAcum)
        lista.append(viajero)
    archivo.close()
    menu_1(lista)