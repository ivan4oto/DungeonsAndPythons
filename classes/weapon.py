from utils.verify import verify_positive, verify_types


class Weapon:

    @verify_positive
    @verify_types(name=str, damage=int)
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name}: damage {self.damage}"

    def __gt__(self, other):
        return self.damage > other.damage
