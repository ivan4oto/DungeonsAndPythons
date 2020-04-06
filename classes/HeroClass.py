from .BaseCharClass import BaseChar
from .treasure import Treasure

class Hero(BaseChar):
    MAX_ITEMS = 6

    def __init__(self, name = "", title = "", health = 100, mana = 100, mana_regeneration_rate = 2):
        super().__init__(health = 100, mana = 100)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.items = []

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def add_item(self, item):
        if len(self.items) == self.MAX_ITEMS:
            print('Inventory is full !')
        self.items.append(item)
        return True


    def drink_potion(self, potion_type = str):
        if len(self.items) == 0:
            print("Inventory is empty !")
            return False
        for x in self.items:
            if isinstance(x, Treasure):
                if x.type == 'health potion' and potion_type == 'health':
                    self.take_healing(x.item)
                    return True
                elif x.type == 'mana potion' and potion_type == 'mana':
                    self.take_mana(x.item)

    # def attack(self, by = str, dungeon):

    #     super().attack(by = str)
                
        