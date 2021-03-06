from . import weapon
from .HeroClass import Hero
from .EnemyClass import Enemy
from utils.verify import verify_types
from .treasure import Treasure


class Fight:

    @verify_types(hero=Hero, enemy=Enemy, default=str)
    def __init__(self, hero, enemy, default="spell"):
        self.hero = hero
        self.enemy = enemy
        self.default = default
        self.report = []

    def start_fight(self, range_from_enemy=0):
        is_enemy_at_same_position = True
        move_enemy = False
        if range_from_enemy > 0:
            move_enemy = True
            is_enemy_at_same_position = False
        hero_damage = self.choose_fighting_tools(self.hero, is_enemy_at_same_position)
        if hero_damage == 0:
            return False
        enemy_damage = self.choose_fighting_tools(self.enemy)

        to_be_continues = True
        while to_be_continues:
            if range_from_enemy != 0:
                move_enemy = True
                range_from_enemy -= 1
            else:
                move_enemy = False
            to_be_continues = self.round_fight(hero_damage, enemy_damage, move_enemy)

        if self.hero.is_alive():
            print(f"Our Enemy is died")
            return self.enemy
        else:
            print(f"Our Hero {self.hero.known_as()} is died")
            return self.hero

    def check_for_add_mana(self):
        if self.hero.mana < self.hero._max_mana:
            for tre in self.hero.items:
                if tre.type == "mana potion":
                    result = self.hero.mana + tre.item
                    added = tre.item
                    if result > self.hero._max_mana:
                        remainder = result - self.hero._max_mana
                        added = tre.item - remainder
                        self.hero.take_mana(tre.item)
                        treasure = Treasure("mana", str(remainder))
                        self.hero.add_item(treasure)
                    print(f"Hero took mana {added}")
                    self.hero.items.remove(tre)
                    return

    def check_for_add_health(self):
        if self.hero.health < self.hero._max_health:
            for tre in self.hero.items:
                if tre.type == "health potion":
                    result = self.hero.health + tre.item
                    added = tre.item
                    if result > self.hero._max_health:
                        remainder = result - self.hero._max_health
                        added = tre.item - remainder
                        self.hero.take_healing(tre.item)
                        treasure = Treasure("health", str(remainder))
                        self.hero.add_item(treasure)
                    print(f"Hero took health {added}")
                    self.hero.items.remove(tre)
                    return

    def round_fight(self, hero_attack, enemy_attack, move_enemy=False):

        self.check_for_add_mana()
        self.check_for_add_health()

        if hero_attack[1].__class__.__name__ == "Weapon":
            attack_type = "attacks with"
            self.enemy.take_damage(hero_attack[0])
            print(
                f"Hero {attack_type} {hero_attack[1].name}, hits enemy for {hero_attack[0]} dmg. " +
                f"Enemy health is {self.enemy.get_health()}")
        else:
            attack_type = "casts"
            if self.hero.mana > 0:

                self.enemy.take_damage(hero_attack[0])
                self.hero.mana -= hero_attack[1].mana_cost
                print(
                    f"Hero {attack_type} {hero_attack[1].name}, hits enemy for {hero_attack[0]} dmg. " +
                    f"Enemy health is {self.enemy.get_health()}")
            else:
                if self.hero.weapon is not None:
                    self.enemy.take_damage(self.hero.weapon.damage)
                    print(
                        f"Here attacks with {self.hero.weapon.name}, hits enemy for {self.hero.weapon.damage}"
                        + f" dmg. Enemy health is {self.enemy.get_health()}")
                else:
                    print(f"Hero does not have mana for another {hero_attack[1].name}")

        if not self.enemy.is_alive():
            return False
        if move_enemy:
            print("Enemy moves one square in order to get to the hero. This is his move.")
        else:
            self.hero.take_damage(enemy_attack[0])
            print(f"Enemy hits hero for {enemy_attack[0]} dmg. Hero health is {self.hero.get_health()}")
        if not self.hero.is_alive():
            return False
        return True

    def choose_fighting_tools(self, character, is_enemy_at_same_position=True):

        if not is_enemy_at_same_position and character.__class__.__name__ == "Hero":
            by_spell = character.attack(self.default)
            if by_spell is None:
                print(f"Your hero {self.hero.known_as()} has no spell.")
                return 0
            return by_spell

        by_weapon = character.attack("weapon")
        by_spell = character.attack("spell")

        if by_weapon[0] is None and by_spell[0] is None:
            if character.__class__.__name__ == "Hero":
                print(f"Your hero {self.hero.known_as()} has no spell and weapon.")
            return 0
        if by_weapon[0] is None and character.can_cast():
            return by_spell
        if by_spell[0] is None and is_enemy_at_same_position:
            return by_weapon
        if by_weapon[0] <= by_spell[0] and character.can_cast():
            return by_spell
        elif is_enemy_at_same_position:
            return by_weapon
