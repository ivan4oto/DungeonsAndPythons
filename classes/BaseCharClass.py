class BaseChar():
    def __init__(self, health = 100, mana = 100):
        self._max_health = health
        self._max_mana = mana

        self.health = health
        self.mana = mana

        self.base_damage = 0
        self.weapon = None
        self.spell = None
    
    def get_health(self):
        return self.health
    
    
    def get_mana(self):
        return self.mana
    
    def is_alive(self):
        return self.get_health() > 0

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def can_cast(self):
        return self.get_mana() >= self.spell.mana_cost
            

    def take_damage(self, damage_points):
        if self.get_health() <= damage_points:
            self.health = 0
        else:
            self.health = self.get_health() - int(damage_points)
        

    def take_healing(self, healing_points):
        if self.get_health() == 0:
            return 'Character is already dead !'
        elif self.get_health() > 0:
            self.health += int(healing_points)
            if self.health > self._max_health:
                self.health = self._max_health
    

    def take_mana(self, mana_points):
        if self.get_mana() + int(mana_points) > self._max_mana:
            self.mana = self._max_mana
        else:
            self.mana += int(mana_points)

    def attack(self, by = ""):
        if by == "weapon":
            if self.weapon != None:
                return self.weapon.damage
            else:
                return self.base_damage

        elif by == "spell":
            if self.spell != None:
                if self.get_mana() >= self.spell.mana_cost:
                    self.mana -= self.spell.mana_cost
                    return self.spell.damage
            else:
                return self.base_damage

    

