import unittest

from classes.spell import Spell


class MyTestCase(unittest.TestCase):

    def test_create_new_spell_return_correctly(self):
        new_spell = Spell("New  Spell", 123, 12, 1)

        self.assertEqual(new_spell.mana_cost, 12)
        self.assertEqual(new_spell.name, "New  Spell")
        self.assertEqual(new_spell.damage, 123)
        self.assertEqual(new_spell.cast_range, 1)

    def test_create_new_spell_when_given_negative_cast_spell_return_ec(self):
        with self.assertRaises(ValueError):
            new_spell = Spell("New  Spell", 123, 12, -1)

    def test_create_new_spell_when_given_negative_mana_return_ec(self):
        with self.assertRaises(ValueError):
            new_spell = Spell("New  Spell", 123, -12, 1)

    def test_create_new_spell_when_given_negative_demage_return_ec(self):
        with self.assertRaises(ValueError):
            new_spell = Spell("New  Spell", -123, 12, 1)

    def test_create_new_spell_when_given_negative_all_value_return_ec(self):
        with self.assertRaises(ValueError):
            new_spell = Spell("New  Spell", -123, -12, -1)

    def test_check_when_two_spells_is_given_return_bigger_one(self):
        one_spell = Spell("New  Spell", 1230, 12, 1)
        two_spell = Spell("New  Spell", 123, 10, 1)

        self.assertTrue(one_spell > two_spell)

    def test_check_when_two_spells_are_equals_return_bigger_one(self):
        one_spell = Spell("New  Spell", 1230, 12, 1)
        two_spell = Spell("New  Spell", 1230, 12, 1)

        self.assertFalse(one_spell < two_spell)

    def test_when_give_wrong_input_type(self):
        with self.assertRaises(ValueError):
            new_spell = Spell(13.3, 123, 12, -1)

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
