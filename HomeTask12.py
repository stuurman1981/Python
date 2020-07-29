'''
Написать консольную игру Морской бой.
Игра поддерживает поочередные ходы 2 игроков.
Каждому игроку принадлежит по 8 однотрубных.
Игроки не расставляют свои корабли. Вместо этого они располагаются на полях случайным образом.

Старт программы:

Генерация 2 наборов из 2 полей: поле 10х10 с кораблями игрока, поле 10х10 с попытками попадания во вражеские корабли
(~ - символ пустой клетки, о - символ клетки активного корабля, х - символ клетки подбитого корабля, * - символ клетки
промаха). Каждое поле - лист листов, пример поля 3х3: [[~, ~, ~], [~, ~, ~], [~, ~, ~]].
Генерация кораблей на первом поле для каждого игрока
Старт основного цикла

Основной цикл программы для одного игрока:

Отрисовка первого поля (корабли активного игрока)
Отрисовка второго поля (выстрелы активного игрока)
Ожидание ввода координат (два числа от 1 до 10 через запятую)
Проверка валидности введенных координат (повторный ввод в случае ошибки)
Проверка первого поля ожидающего игрока (попал ли активный игрок в корабль ожидающего игрока)
Обновление второго поля активного игрока (замена символов)
Конец цикла

Описание сущностей:

Игра - главный класс, который имеет основной цикл, вспомогательные методы (генерация поля, проверка координат на
указанном поле) и атрибуты (например, поля игроков).

Опционально:

Очистка консоли в конце цикла, чтобы при переходе хода скрыть от следующего игрока поле предыдущего игрока.
'''

import os

from random import randint

class Game:
    def __init__(self):
        self.player1 = input('Please enter first player name >>>')
        self.player2 = input('Please enter second player name >>>')
        self.count1 = 1
        self.count2 = 1
        self.player1_own = [['~' for _ in range(10)] for _ in range(10)]
        self.player1_enemy = [['~' for _ in range(10)] for _ in range(10)]
        self.player2_own = [['~' for _ in range(10)] for _ in range(10)]
        self.player2_enemy = [['~' for _ in range(10)] for _ in range(10)]
        self.player1_own_field = []
        self.player1_enemy_field = []
        self.player2_own_field = []
        self.player2_enemy_field = []
        self.active_player = self.player1
        self.player1_ships = []
        self.player2_ships = []
        self.x = None
        self.y = None


    def player_field(self, active_player):
        if active_player == self.player1:
            used_coords = []
            i = 0
            while i < 8:
                x, y = randint(0, 9), randint(0, 9)
                if (x, y) not in used_coords:
                    self.player1_own[x][y] = 'o'
                    self.player1_ships.append((x, y))
                    used_coords.append((x, y))
                    used_coords.append((x, y + 1))
                    used_coords.append((x, y - 1))
                    used_coords.append((x + 1, y))
                    used_coords.append((x - 1, y))
                    used_coords.append((x + 1, y + 1))
                    used_coords.append((x + 1, y - 1))
                    used_coords.append((x - 1, y + 1))
                    used_coords.append((x - 1, y - 1))
                    i += 1
            return self.player1_own, self.player1_ships
        else:
            used_coords = []
            i = 0
            while i < 8:
                x, y = randint(0, 9), randint(0, 9)
                if (x, y) not in used_coords:
                    self.player2_own[x][y] = 'o'
                    self.player2_ships.append((x, y))
                    used_coords.append((x, y))
                    used_coords.append((x, y + 1))
                    used_coords.append((x, y - 1))
                    used_coords.append((x + 1, y))
                    used_coords.append((x - 1, y))
                    used_coords.append((x + 1, y + 1))
                    used_coords.append((x + 1, y - 1))
                    used_coords.append((x - 1, y + 1))
                    used_coords.append((x - 1, y - 1))
                    i += 1
            return self.player2_own, self.player2_ships


    def print_fields(self, active_player, player1_enemy, player2_enemy):
        os.system('cls')
        print(f'     Own Field\t\t\t    Enemy Field')
        if active_player == self.player1:
            for i in range(10):
                print(f"{' '.join(self.player1_own[i])}\t\t{' '.join(self.player1_enemy[i])}")
        else:
            for i in range(10):
                print(f"{' '.join(self.player2_own[i])}\t\t{' '.join(self.player2_enemy[i])}")
        print(f'Turn of player {active_player}')
        self.x = int(input('Please enter coordinate x from 0 to 9 >>>'))
        self.y = int(input('Please enter coordinate y from 0 to 9 >>>'))
        return self.x, self.y


    def update_enemy(self):
        if self.active_player == self.player1:
            if (self.x, self.y) in self.player2_ships:
                self.player1_enemy[self.x][self.y] = 'x'
                self.count1 += 1
                return self.player1_enemy, self.count1
            else:
                self.player1_enemy[self.x][self.y] = '*'
                self.active_player = self.player2
                return self.player1_enemy, self.active_player
        else:
            if (self.x, self.y) in self.player1_ships:
                self.player2_enemy[self.x][self.y] = 'x'
                self.count2 += 1
                return self.player2_enemy, self.count2
            else:
                self.player2_enemy[self.x][self.y] = '*'
                self.active_player = self.player1
                return self.player2_enemy, self.active_player


    def run(self):
        self.player_field(self.player1)
        self.player_field(self.player2)
        self.print_fields(self.active_player, self.player1_enemy, self.player2_enemy)
        while self.count1 < 8 and self.count2 < 8:
            while 0 <= self.x < 10 and 0 <= self.y < 10:
                self.update_enemy()
                self.print_fields(self.active_player, self.player1_enemy, self.player2_enemy)
                if self.count1 == 8:
                    print(f'Player {self.player1} won the game')
                    exit(0)
                if self.count2 == 8:
                    print(f'Player {self.player2} won the game')
                    exit(0)
            else:
                print('Incorrect entry')
                self.x = int(input('Please enter coordinate x from 0 to 9 >>>'))
                self.y = int(input('Please enter coordinates y from 0 to 9 >>>'))


a = Game()
a.run()
