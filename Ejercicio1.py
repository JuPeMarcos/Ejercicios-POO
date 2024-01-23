"""
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable. Debe permitir:

Crear duraciones de tiempos.
Ejemplo: t = Duration(10,20,56)
Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
Si no indico la hora, minuto o segundo estos valores son cero:
Duration() --> (0, 0, 0)
Duration(34) --> (34, 0, 0)
Duration(34, 15) --> (34, 15, 0)
Duration(34, 61) --> (35, 1, 0)
Las duraciones de tiempo se pueden comparar.
A las duraciones de tiempo les puedo sumar y restar segundos.
Las duraciones de tiempo se pueden sumar y restar. 
"""

from typeguard import typechecked

@typechecked
class Duration:

    def __init__(self, h, m=None, s=None):
        if isinstance(h, Duration) and (m, s) == (None, None):  # solo tiene que llegar un parámetro
            other = h
            self.__h, self.__m, self.__s = other.h, other.m, other.s
        elif isinstance(h, int) and isinstance(m, int) and isinstance(s, int):
            self.__h, self.__m, self.__s = h, m, s
            self.__normalize()
        else:
            raise TypeError("Un objeto Duration se construye con tres enteros o con otro objeto Duration")

    def __normalize(self):
        s = self.__to_s()
        if s < 0:
            raise ValueError("No puede haber duraciones de tiempo negativas")
        self.__h = s // 3600
        self.__m = s % 3600 // 60
        self.__s = s % 3600 % 60

    def __to_s(self):
        return self.h * 3600 + self.m * 60 + self.s
   
    @property
    def h(self):
        return self.__h
    
    @property
    def m(self):
        return self.__m

    @property
    def s(self):
        return self.__s

    @h.setter
    def h(self, value: int):
        new_duration = Duration(value, self.m, self.s)
        self.__h, self.__m, self.__s = new_duration.h, new_duration.m, new_duration.s

    @m.setter
    def m(self, value: int):
        new_duration = Duration(self.h, value, self.s)
        self.__h, self.__m, self.__s = new_duration.h, new_duration.m, new_duration.s

    @s.setter
    def s(self, value: int):
        new_duration = Duration(self.h, self.m, value)
        self.__h, self.__m, self.__s = new_duration.h, new_duration.m, new_duration.s

    def add_h(self, h: int):
            self.h += h

    def sub_h(self, h: int):
        self.h -= h

    def add_m(self, m: int):
        self.m += m

    def sub_m(self, m: int):
        self.m -= m

    def add_s(self, s: int):
        self.s += s

    def sub_s(self, s: int):
        self.s -= s
    
    def __str__(self):
        return f"{self.h}h {self.m}m {self.s}s"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.h}, {self.m}, {self.s})"

    # Sobrecarga de operadores

    def __add__(self, other: 'Duration'):
        return Duration(self.h + other.h, self.m + other.m, self.s + other.s)

    def __sub__(self, other: 'Duration'):
        return Duration(self.h - other.h, self.m - other.m, self.s - other.s)

    def __eq__(self, other: 'Duration'):
        return (self.h, self.m, self.s) == (other.h, other.m, other.s)

    def __ne__(self, other: 'Duration'):
        return not self == other

    def __lt__(self, other: 'Duration'):
        return self.__to_s() < other.__to_s()

    def __le__(self, other: 'Duration'):
        return self.__to_s() <= other.__to_s()

    def __gt__(self, other: 'Duration'):
        return not self <= other

    def __ge__(self, other: 'Duration'):
        return not self < other
    
