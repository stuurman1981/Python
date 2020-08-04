import unittest

from lesson.game import Room, Game


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.x = 5
        self.y = 4
        self.name = "Test room"
        self.description = "Ready for test"
        self.exits = ['This way', 'That way']
        self.room = Room(self.x, self.y, self.name, self.description, self.exits)

    def test_str(self):
        expected = f'{self.name}\n{self.description}'
        result = self.room.__str__()
        self.assertEqual(expected, result)

    def test_check_exit_positive(self):
        result = self.room._check_exit('This way')
        self.assertTrue(result)

    def test_check_exit_negative(self):
        result = self.room._check_exit('north')
        self.assertFalse(result)


class TestGame(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(0, 0, "Main room", '', ["north"])
        self.room2 = Room(0, -1, 'Second room', '', ['south'])
        map = {(self.room1.x, self.room1.y): self.room1,
               (self.room2.x, self.room2.y): self.room2
               }
        self.game = Game(map)

    def test_move_positive(self):
        self.game._move(0, -1)
        self.assertEqual(self.game.player_x, 0)
        self.assertEqual(self.game.player_y, -1)
        self.assertEqual(self.game.current_room, self.room2)

    def test_get_room_positive(self):
        result = self.game._get_room(0, -1)
        self.assertIsInstance(result, Room)
        self.assertEqual(result, self.room2)

    def test_get_room_negative(self):
        result = self.game._get_room(0, -2)
        self.assertIsNone(result)

    def test_parse(self):
        result = self.game._parse('go north')
        self.assertEqual(result, (0, -1))

    def test_run(self):
        self.assertFalse(self.game.run)


if __name__ == '__main__':
    unittest.main()
