import unittest
from DungeonClass import Dungeon
from classes.HeroClass import Hero



class TestDungeonClass(unittest.TestCase):
    def test_spawning_hero(self):
        h = Hero('Ivan', 'Mountain goat')
        d = Dungeon('level_test_spawn.txt')
        result1 = d.spawn(h)
        result2 = d.map[1][7]

        self.assertEqual(result2, 'H')
        self.assertTrue(result1)

    def test_move_hero(self):
        h = Hero('Ivan', 'Mountain goat')
        d = Dungeon('level_test_spawn.txt')
        d.spawn(h)
        result1 = d.move_hero('up')
        result2 = d.map[0][7]
        result3 = d.map[1][7]

        self.assertTrue(result1)
        self.assertEqual(result2, 'H')
        self.assertEqual(result3, '.')
      
    def test_move_hero_out_of_map_returns_false(self):
        h = Hero('Ivan', 'Mountain goat')
        d = Dungeon('level_test_spawn.txt')
        d.spawn(h)
        result1 = d.move_hero('up')
        result2 = d.move_hero('up')

        self.assertTrue(result1)
        self.assertFalse(result2)


if __name__ == '__main__':
    unittest.main()
