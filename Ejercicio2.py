"""
Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numeratorerador y denominatorominador.
 Ejemplo: f = Fraction(2, 3)
Ojo!!! No se puede tener un denominatorominador cero.
Las fracciones puedenominator operar entre sí.
Sumar, multiplicar, dividir, restar.
Ojo!!! esto se puede hacer: f + 1, 5 * f
Las fracciones se puedenominator comparar.
==, <, <=, >, >=, !=
Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
Ojo!!! esto se puede hacer 1 < 1/2
"""
import math
from typeguard import typechecked

@typechecked
class Fraction:

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("Una fracción no puede tener 0 como denominatorominador.")
        gcd = math.gcd(numerator, denominator)
        self.__numerator = numerator // gcd
        self.__denominator = denominator // gcd

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numerator, self.__denominator})"

    def result(self):
        return self.__numerator / self.__denominator

    def __mul__(self, other: (int, 'Fraction')):
        if isinstance(other, int):
            return Fraction(self.__numerator * other, self.__denominator)
        return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return self * -1

    def __add__(self, other: 'Fraction'):
        return Fraction(self.__numerator * other.__denominator + self.__denominator * other.__numerator, self.__denominator * other.__denominator)

    def __sub__(self, other: 'Fraction'):
        return self - other

    def __truediv__(self, other: 'Fraction'):
        return Fraction(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __eq__(self, other: 'Fraction'):
        return (self.__numerator, self.__denominator) == (other.__numerator, other.__denominator)

    def __ne__(self, other: 'Fraction'):
        return not (self == other)

    def __lt__(self, other: 'Fraction'):
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator

    def __le__(self, other: 'Fraction'):
        return self < other or self == other

    def __gt__(self, other: 'Fraction'):
        return not (self <= other)

    def __ge__(self, other: 'Fraction'):
        return not (self < other)