import unittest
from classes.DungeonClass import Dungeon
from classes.HeroClass import Hero
from classes.EnemyClass import Enemy



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

    def test_move_hero_into_obstacle(self):
        h = Hero('Ivan', 'Mountain goat')
        d = Dungeon('level_test_spawn.txt')
        d.spawn(h)
        result1 = d.move_hero('left')

        self.assertFalse(result1)    

    def test_fill_treasures_list_fills_correctly(self):
        d = Dungeon('files/first_map.txt')
        d.fill_treasures_list('files/treasures.txt')
        self.assertEqual(len(d.treasures), 10)

    def test_fill_enemies_list_fills_correctly(self):
        d = Dungeon('files/first_map.txt')
        d.fill_enemies_list('files/enemies.txt')
        boolist = [isinstance(x, Enemy) for x in d.enemies]
        self.assertEqual(len(d.enemies), 6)
        self.assertTrue(all(boolist))


if __name__ == '__main__':
    unittest.main()
