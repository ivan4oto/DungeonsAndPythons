from .BaseCharClass import BaseChar

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
            raise ValueError('Inventory is full !')
        self.items.append(item)
        return True


    