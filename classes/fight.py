from .HeroClass import Hero
from .EnemyClass import Enemy
from utils.verify import verify_types

class Fight:

    @verify_types(hero=Hero, enemy=Enemy)
    def __init__(self, hero, enemy):
        self.__hero = hero
        self.__enemy = enemy
        self.report = {}


    def start_fight(self):
        report = ""

        while self.__hero.is_alive() and self.__enemy.is_alive():

            if self.__hero.can_cast() and self.__hero.spell.damage > self.__hero.weapon.damage:
                self.__enemy.take_damage(self.__hero.attack(by = 'spell'))
            
                
            
        

    def get_report(self):
        pass

        





