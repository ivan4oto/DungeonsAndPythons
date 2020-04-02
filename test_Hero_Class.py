import unittest
from classes.HeroClass import Hero

class TestHeroClass(unittest.TestCase):
    def test_hero_init(self):
        ivan = Hero('Ivan', 'Bug maker !')

        self.assertEqual(ivan.known_as(), 'Ivan the Bug maker !')
        self.assertEqual(ivan.get_mana(), 100)
        self.assertEqual(ivan.get_health(), 100)
        self.assertEqual(ivan.base_damage, 0)

if __name__ == '__main__':
    unittest.main()
