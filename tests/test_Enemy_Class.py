import unittest
from classes.EnemyClass import Enemy
from classes.weapon import Weapon
from classes.spell import Spell

class TestEnemyClass(unittest.TestCase):
    def test_enemy_init(self): 
        saruman = Enemy(100, 100)
        result = saruman.attack()
        saruman.take_damage(30)
        saruman.take_healing(20)

        self.assertTrue(saruman.is_alive())
        self.assertEqual(result, 20)
        self.assertEqual(saruman.get_health(), 90)
        
    def test_enemy_use_weapon(self):
        sauron = Enemy(100, 100)
        sword = Weapon('Big fat sword', 30)
        sauron.equip(sword)

        self.assertEqual(sauron.attack(by = 'weapon'), 30)

    def test_hero_use_spell(self):
        sauron = Enemy(100, 100)
        fireball = Spell('Fireball', 40, 15, 2)
        sauron.learn(fireball)

        result = sauron.attack(by = 'spell')

        self.assertTrue(sauron.can_cast())
        self.assertEqual(result, 40)
        self.assertEqual(sauron.get_mana(), 85)

        
if __name__ == "__main__":
    unittest.main()