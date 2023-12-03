"""
Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numerador y denominador.
 Ejemplo: f = Fraction(2, 3)
Ojo!!! No se puede tener un denominador cero.
Las fracciones pueden operar entre sí.
Sumar, multiplicar, dividir, restar.
Ojo!!! esto se puede hacer: f + 1, 5 * f
Las fracciones se pueden comparar.
==, <, <=, >, >=, !=
Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
Ojo!!! esto se puede hacer 1 < 1/2
"""
import math

class Fraction:

    def __init__(self, num: int, den: int):
        if den == 0:
            raise ZeroDivisionError("Una fracción no puede tener 0 como denominador.")
        mcd = math.gcd(num, den)
        self.__num = num // mcd
        self.__den = den // mcd

   
    def num(self):
        return self.__num


    def den(self):
        return self.__den

    def __str__(self):
        return f"{self.__num}/{self.__den}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__num, self.__den})"

    def result(self):
        return self.__num / self.__den

    def __mul__(self, other: (int, 'Fraction')):
        if isinstance(other, int):
            return Fraction(self.__num * other, self.__den)
        return Fraction(self.__num * other.__num, self.__den * other.__den)

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return self * -1

    def __add__(self, other: 'Fraction'):
        return Fraction(self.__num * other.__den + self.__den * other.__num, self.__den * other.__den)

    def __sub__(self, other: 'Fraction'):
        return self - other

    def __truediv__(self, other: 'Fraction'):
        return Fraction(self.__num * other.__den, self.__den * other.__num)

    def __eq__(self, other: 'Fraction'):
        return (self.__num, self.__den) == (other.__num, other.__den)

    def __ne__(self, other: 'Fraction'):
        return not (self == other)

    def __lt__(self, other: 'Fraction'):
        return self.__num * other.__den < other.__num * self.__den

    def __le__(self, other: 'Fraction'):
        return self < other or self == other

    def __gt__(self, other: 'Fraction'):
        return not (self <= other)

    def __ge__(self, other: 'Fraction'):
        return not (self < other)