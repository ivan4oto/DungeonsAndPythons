import unittest
from classes.treasure import Treasure

class TestTreasureClass(unittest.TestCase):
    def test_potions(self):
        hp = Treasure('health', '30')
        mp = Treasure('mana', '30')

        self.assertEqual(hp.type, 'health potion')
        self.assertEqual(mp.type, 'mana potion')




if __name__ == "__main__":
    unittest.main()