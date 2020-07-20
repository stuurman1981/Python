'''Без использования библиотек, создать класс для представления информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд.'''


class Time:
    def __init__(self, h=0, m=0, s=0):
        self._hours = h if h in range(0, 23) else 23
        self._minutes = m if m in range(0, 59) else 59
        self._seconds = s if s in range(0, 59) else 59

    @property
    def h(self):
        return self._hours

    @h.setter
    def h(self, h):
        self._hours = h if h in range(0, 23) else 23

    @property
    def m(self):
        return self._minutes

    @m.setter
    def m(self, m):
        self._minutes = m if m in range(0, 59) else 59

    @property
    def s(self):
        return self._seconds

    @s.setter
    def s(self, s):
        self._seconds = s if s in range(0, 59) else 59

    def __repr__(self):
        return f'Time: {self._hours} hours, {self._minutes} minutes, {self._seconds} seconds'

    def __str__(self):
        return f'Time: {self._hours}:{self._minutes}:{self._seconds}'
