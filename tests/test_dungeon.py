import unittest

from classes.dungeon import Dungeon


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pass

    def test_fill_treasures_list_without_given_path_return_correctly(self):
        d = Dungeon()

        self.assertEqual(len(d.treasures), 10)

    def test_fill_map_without_given_path_return_correctly(self):
        d = Dungeon()
        self.assertEqual(type(d.map), list)


if __name__ == '__main__':
    unittest.main()
