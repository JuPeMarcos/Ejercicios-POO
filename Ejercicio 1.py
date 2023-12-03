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

class Duration:

    def __init__(self, hours, minutes=None, seconds=None):
        if isinstance(hours, Duration) and (minutes, seconds) == (None, None):  # solo tiene que llegar un parámetro
            other = hours
            self.__hours, self.__minutes, self.__seconds = other.hours, other.minutes, other.seconds
        elif isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
            self.__hours, self.__minutes, self.__seconds = hours, minutes, seconds
            self.__normalize()
        else:
            raise TypeError("Un objeto Duration se construye con tres enteros o con otro objeto Duration")

    def __normalize(self):
        seconds = self.__total_seconds()
        if seconds < 0:
            raise ValueError("No puede haber duraciones de tiempo negativas")
        self.__hours = seconds // 3600
        self.__minutes = seconds % 3600 // 60
        self.__seconds = seconds % 3600 % 60

    def __total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
   
    def minutes(self):
        return self.__minutes

    def minutes(self, value: int):
        new_duration = Duration(self.hours, value, self.seconds)
        self.__hours, self.__minutes, self.__seconds = new_duration.hours, new_duration.minutes, new_duration.seconds

    def hours(self):
        return self.__hours

    def hours(self, value: int):
        new_duration = Duration(value, self.minutes, self.seconds)
        self.__hours, self.__minutes, self.__seconds = new_duration.hours, new_duration.minutes, new_duration.seconds

    def seconds(self):
        return self.__seconds

    
    def seconds(self, value: int):
        new_duration = Duration(self.hours, self.minutes, value)
        self.__hours, self.__minutes, self.__seconds = new_duration.hours, new_duration.minutes, new_duration.seconds

    def add_seconds(self, seconds: int):
        self.seconds += seconds

    def sub_seconds(self, seconds: int):
        self.seconds -= seconds

    def add_minutes(self, minutes: int):
        self.minutes += minutes

    def sub_minutes(self, minutes: int):
        self.minutes -= minutes

    def add_hours(self, hours: int):
        self.hours += hours

    def sub_hours(self, hours: int):
        self.hours -= hours

    def __str__(self):
        return f"{self.hours}h {self.minutes}m {self.seconds}s"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.hours}, {self.minutes}, {self.seconds})"

    # Sobrecarga de operadores

    def __add__(self, other: 'Duration'):
        return Duration(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def __sub__(self, other: 'Duration'):
        return Duration(self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds)

    def __eq__(self, other: 'Duration'):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __ne__(self, other: 'Duration'):
        return not self == other

    def __lt__(self, other: 'Duration'):
        return self.__total_seconds() < other.__total_seconds()

    def __le__(self, other: 'Duration'):
        return self.__total_seconds() <= other.__total_seconds()

    def __gt__(self, other: 'Duration'):
        return not self <= other

    def __ge__(self, other: 'Duration'):
        return not self < other