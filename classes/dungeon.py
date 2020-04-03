import pathlib

from classes.treasure import Treasure
from utils.constants import FileConstants


class Dungeon:
    def __init__(self, file_name=FileConstants.FIRST_MAP_FILE):
        self.file_name = file_name
        self.treasures = []
        self.enemies = []
        self.map = self.fill_map(file_name)
        self.hero_x = 0
        self.hero_y = 0
        self.hero_start_x = 0
        self.hero_start_y = 0

    def read_file(self, file_name):
        path = pathlib.Path(__file__).parent / file_name
        result = []
        f = open(path, "r")
        for x in f:
            x = x[:-1]
            x = x.split(",")
            result.append(x)
        f.close()
        return result

    def fill_treasures_list(self, path=FileConstants.TREASURES_FILE):
        treasures_raw = self.read_file(path)
        for treasure_raw in treasures_raw:
            self.treasures.append(Treasure(*treasure_raw))

    def fill_enemies(self, path=FileConstants.ENEMIES_FILE):
        enemies_data = self.read_file(path)
        enemies = []
        for enemy_data in enemies_data:
            enemies.append(Enemy(*enemy_data))
        self.enemies = enemies

    def fill_map(self, path=FileConstants.FIRST_MAP_FILE):
        map_list = self.read_file(path)
        self.fill_treasures_list()
        # self.fill_enemies()
        result = []
        for row in map_list:
            result.append([list(i) for i in row])
        return result

    def print_map(self):
        for row in self.map:
            print("".join(row))
        print()

    def still_in_the_map(self, x, y):
        if (x < 0 or x >= len(self.map)) or (y < 0 or y >= len(self.map[0])):
            return False
        return True

    def is_free(self, pos, start=False):
        if start is True:
            if pos == 'S':
                return True
            else:
                return False
        if pos == 'S' or pos == '.':
            return True
        if pos == '#':
            return False
        if pos == 'T':
            self.collect_treasure(self.hero)
            return True


    def collect_treasure(self, hero):
        from random import shuffle
        shuffle(self.treasures)
        # should add treasures to hero after he step over it
        self.treasures = self.treasures[1:]

    def can_place(self, x, y):
