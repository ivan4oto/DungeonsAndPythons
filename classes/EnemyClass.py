from .BaseCharClass import BaseChar

class Enemy(BaseChar):
    def __init__(self, health = 100, mana = 100, damage = 20):
        super().__init__(health = health, mana = mana)
        self.base_damage = damage

    