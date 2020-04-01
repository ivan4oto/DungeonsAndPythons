from utils.verify import verify_positive, verify_types


class Treasure:

    @verify_positive
    @verify_types(value_type=str)
    def __init__(self, value_type, value, name=None):
        self.type = value_type
        if value_type == 'weapon':
            self.item = Weapon(name=name, damage=value)
        elif value_type == 'spell':
            self.item = Spell(name=name, damage=value)
        else:
            self.type += ' potion'
            self.item = value

    def __repr__(self):
        return f"{self.item}"