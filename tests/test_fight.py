import unittest

from classes.HeroClass import Hero
from classes.EnemyClass import Enemy
from classes.fight import Fight
from classes.spell import Spell
from classes.weapon import Weapon


class MyTestCase(unittest.TestCase):
    def test_choose_fighting_tools_when_hero_does_not_have_spec_ability_return_damage_zero(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy()

        create_fight = Fight(hero, enemy)

        result = create_fight.choose_fighting_tools(hero, False)

        self.assertEqual(result, [0])

    def test_choose_fighting_tools_when_hero_has_spec_ability_return_damage_from_weapon(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy()
        weapon = Weapon("shodow", 100)
        hero.equip(weapon)

        create_fight = Fight(hero, enemy)

        result = create_fight.choose_fighting_tools(hero, True)

        self.assertEqual(result, [100, weapon])

    def test_choose_fighting_tools_when_hero_has_spec_ability_but_enemy_is_not_in_range_return_zero(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy()
        weapon = Weapon("shodow", 100)
        hero.equip(weapon)

        create_fight = Fight(hero, enemy)

        result = create_fight.choose_fighting_tools(hero, False)

        self.assertEqual(result, [0])

    def test_choose_fighting_tools_when_hero_has_spec_ability_weapon_and_spell_return_spell(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy()
        weapon = Weapon("shodow", 100)
        spell = Spell("bla", 150)
        hero.equip(weapon)
        hero.learn(spell)
        create_fight = Fight(hero, enemy)

        result = create_fight.choose_fighting_tools(hero, False)

        self.assertEqual(result, [150, spell])

    def test_choose_fighting_tools_when_hero_has_not_got_spell_and_enemy_is_not_at_same_position_return_zero(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy()
        weapon = Weapon("shodow", 100)
        hero.equip(weapon)
        create_fight = Fight(hero, enemy)

        result = create_fight.choose_fighting_tools(hero, False)

        self.assertEqual(result, [0])

    def test_choose_fighting_tools_when_hero_has_not_got_weapon_and_enemy_is_at_same_position_return_weapon(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy()
        weapon = Weapon("shodow", 100)
        hero.equip(weapon)
        create_fight = Fight(hero, enemy, "weapon")

        result = create_fight.choose_fighting_tools(hero, True)

        self.assertEqual(result, [100, weapon])

    def test_round_fight_when_hero_hits_return_enemy_gone(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy()
        weapon = Weapon("shodow", 100)
        hero.equip(weapon)
        create_fight = Fight(hero, enemy)

        hero_result = create_fight.choose_fighting_tools(hero, True)
        enemy_result = create_fight.choose_fighting_tools(enemy, True)

        result = create_fight.round_fight(hero_result, enemy_result)
        self.assertEqual(result, False)

    def test_round_fight_when_hero_hits_and_enemy_is_not_gone_return_enemy_strike_back(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy(health=200)
        weapon = Weapon("shodow", 100)
        hero.equip(weapon)
        create_fight = Fight(hero, enemy)

        hero_result = create_fight.choose_fighting_tools(hero, True)
        enemy_result = create_fight.choose_fighting_tools(enemy, True)

        result = create_fight.round_fight(hero_result, enemy_result)

        self.assertEqual(hero.get_health(), 80)
        self.assertEqual(enemy.get_health(), 100)

    def test_round_fight_when_hero_hits_and_with_spell_enemy_is_not_gone_return_enemy_move_to_hero(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy(health=200)
        weapon = Weapon("shodow", 100)
        hero.equip(weapon)
        spell = Spell("Abraka", 120)
        hero.learn(spell)
        create_fight = Fight(hero, enemy)

        hero_result = create_fight.choose_fighting_tools(hero, False)
        enemy_result = create_fight.choose_fighting_tools(enemy, True)

        result = create_fight.round_fight(hero_result, enemy_result, True)

        self.assertEqual(hero.get_health(), 100)
        self.assertEqual(enemy.get_health(), 80)

    def test_round_fight_when_hero_hits_and_with_spell_enemy_return_enemy_kills_hero(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy(health=200, damage=300)
        weapon = Weapon("shodow", 100)
        hero.equip(weapon)
        spell = Spell("Abraka", 120)
        hero.learn(spell)
        create_fight = Fight(hero, enemy)

        hero_result = create_fight.choose_fighting_tools(hero, True)
        enemy_result = create_fight.choose_fighting_tools(enemy, True)

        result = create_fight.round_fight(hero_result, enemy_result)

        self.assertEqual(result, False)
        self.assertEqual(hero.get_health(), 0)
        self.assertEqual(enemy.get_health(), 80)

    def test_start_fight_when_both_are_in_same_pas_return_loser_our_hero(self):
        hero = Hero("Pesho", "Padawan")
        enemy = Enemy(health=200, damage=10)
        weapon = Weapon("shodow", 10)
        hero.equip(weapon)
        spell = Spell("Abraka", 10)
        hero.learn(spell)
        create_fight = Fight(hero, enemy, "weapon")

        result = create_fight.start_fight(0)

        self.assertEqual(result, hero)

    def test_start_fight_when_hero_strike_from_distance_enemy_return_dead_hero(self):
        hero = Hero("Pesho", "Padawan", health=100)
        enemy = Enemy(health=200, damage=10)
        weapon = Weapon("shodow", 40)
        spell = Spell("Abraka", 40)
        hero.learn(spell)
        create_fight = Fight(hero, enemy)

        result = create_fight.start_fight(1)

        self.assertEqual(result, hero)

    def test_start_fight_when_hero_strike_after_mana_is_gone_switch_to_weapon_return_dead_enemy(self):
        hero = Hero("Pesho", "Padawan", health=100)
        enemy = Enemy(health=200, damage=10)
        weapon = Weapon("shodow", 40)
        hero.equip(weapon)
        spell = Spell("Abraka", 40)
        hero.learn(spell)
        create_fight = Fight(hero, enemy)

        result = create_fight.start_fight(1)

        self.assertEqual(result, enemy)


if __name__ == '__main__':
    unittest.main()
