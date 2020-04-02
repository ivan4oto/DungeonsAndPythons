from .BaseCharClass import BaseChar
class Hero(BaseChar):
    def __init__(self, name = "", title = "", health = 100, mana = 100, mana_regeneration_rate = 2):
        super().__init__(health = 100, mana = 100)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

x = Hero()
print(x.base_damage)