from Ejercicio1 import Duration
from Ejercicio2 import Fraction

def main():
    pruebaEjercicio2()

def pruebaEjercicio1():
    d = Duration(10, 100, -200)
    print(d)
    d.add_h(10)
    d.sub_m(10)
    d.sub_s(10)
    print(d)

    d2 = Duration(10, 10, 10)
    print(d - d2)

def pruebaEjercicio2():
    f = Fraction(10, 20)
    print(f.result())


main()