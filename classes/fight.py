class Fight:

    @verify_types(hero=Hero, enemy=Enemy)
    def __init__(self, hero, enemy):
        self.__hero = hero
        self.__enemy = enemy
