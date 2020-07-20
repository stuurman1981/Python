'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и переопределения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

        @property
        def unit_name(self):
            return self._unit_name
        @unit_name.setter
        def unit_setter(self, value):
            self._unit_name = value
        @property
        def mac_address(self):
            return self._mac_address
        @mac_address.setter
        def mac_address(self, value):
            self._mac_address = value
        @property
        def ip_address(self):
            return self._ip_address
        @ip_address.setter
        def ip_address(self, value):
            self._ip_address = value
        @property
        def login(self):
            return self._login
        @login.setter
        def login(self, value):
            self._login = value
        @property
        def password(self):
            return self._login
        @password.setter
        def password(self, value):
            self._password = value
