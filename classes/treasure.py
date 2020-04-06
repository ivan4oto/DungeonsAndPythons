from .spell import Spell
from .weapon import Weapon
from utils.verify import verify_positive, verify_types


class Treasure:

    @verify_types(value_type=str, value=str)
    def __init__(self, value_type, value, name=None):
        self.type = value_type
        if value_type == 'weapon':
            self.item = Weapon(name=name, damage=int(value))
        elif value_type == 'spell':
            self.item = Spell(name=name, damage=int(value))
        else:
            self.type = f'{value_type} potion'
            self.item = int(value)

    def __repr__(self):
        return f"{self.item}"
