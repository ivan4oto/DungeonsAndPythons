import unittest
from classes.BaseCharClass import BaseChar

class TestBase(unittest.TestCase):
    def test_base_init(self):
        x = BaseChar()

        self.assertEqual(x.base_damage, 0)
        self.assertEqual(x.get_health(), 100)
        self.assertEqual(x.get_mana(), 100)

if __name__ == '__main__':
    unittest.main()
