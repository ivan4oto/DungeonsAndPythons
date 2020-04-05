import unittest
from classes.HeroClass import Hero
from classes.weapon import Weapon
from classes.spell import Spell
from classes.treasure import Treasure

class TestHeroClass(unittest.TestCase):
    def test_hero_init(self):
        ivan = Hero('Ivan', 'Bug maker !', 100, 100, 2)

        self.assertEqual(ivan.known_as(), 'Ivan the Bug maker !')
        self.assertEqual(ivan.get_mana(), 100)
        self.assertEqual(ivan.get_health(), 100)
        self.assertEqual(ivan.base_damage, 0)

    def test_hero_use_weapon(self):
        ivan = Hero('Ivan', 'Import Failure', 100,100, 2)
        sword = Weapon('Trouble maker', 30)
        ivan.equip(sword)

        self.assertEqual(ivan.attack(by = 'weapon')[0], 30)

    def test_hero_use_spell(self):
        ivan = Hero('Ivan', 'Import Failure')
        fireball = Spell('Fireball', 40, 15, 2)
        ivan.learn(fireball)

        result = ivan.attack(by = 'spell')

        self.assertTrue(ivan.can_cast())
        self.assertEqual(result[0], 40)
        self.assertEqual(ivan.get_mana(), 85)

    def test_hero_take_dmg(self):
        brusli = Hero('brusli', 'brat mu')
        brusli.take_damage(35)

        self.assertEqual(brusli.get_health(), 65)
    
    def test_hero_take_healing(self):
        bratmu = Hero('Bratmu', 'boro')
        bratmu.take_damage(40)
        bratmu.take_healing(35)

        self.assertEqual(bratmu.get_health(), 95)

    def test_hero_drinks_potions(self):
        leeroy = Hero('Leeroy', 'Jenking', 100, 100)
        leeroy.take_damage(50)
        leeroy.mana -= 50
        hp = Treasure('health', '30')
        mp = Treasure('mana', '10')
        leeroy.add_item(hp)
        leeroy.add_item(mp)

        leeroy.drink_potion('health')
        leeroy.drink_potion('mana')
        
        self.assertEqual(leeroy.get_mana(), 60)
        self.assertEqual(leeroy.get_health(), 80)  

        

if __name__ == '__main__':
    unittest.main()
