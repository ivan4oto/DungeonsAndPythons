from BaseCharClass import BaseChar

class Enemy(BaseChar):
    def __init__(self, health = 100, mana = 100, damage = 20):
        super().__init__(health = 100, mana = 100)
        self.base_damage = damage

    