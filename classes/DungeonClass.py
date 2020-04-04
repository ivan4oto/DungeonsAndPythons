from EnemyClass import Enemy
from HeroClass import Hero
from spell import Spell
from weapon import Weapon
from treasure import Treasure



class Dungeon:
    def __init__(self, map = str):
        with open(map) as f:
            self.map = f.readlines()
        self.map = [list(x.strip()) for x in self.map]
        self.hero_position = dict()
        self.treasures = []
        self.enemies = []
        self.hero = []

    def fill_treasures_list(self, treasures = str):
        with open(treasures) as f:
            treasures_raw = f.readlines()
        self.treasures = [list(x.strip()) for x in treasures_raw]


    def fill_enemies(self, enemies = str):
        with open(enemies) as f:
            enemies_raw = f.readlines()
        self.enemies = [list(x.strip()) for x in enemies_raw]

    def print_map(self):
        print([''.join(x) for x in self.map])

    def spawn(self, hero):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 'S':
                    self.hero_position['y'] = y
                    self.hero_position['x'] = x
                    self.map[y][x] = 'H'
                    self.hero.append(hero)
                    return True
        return False

    def collect_treasure(self, hero):
        from random import shuffle
        shuffle(self.treasures)
        # should add treasures to hero after he step over it
        self.treasures = self.treasures[1:]

    def move_hero(self, direction):

        if direction == 'up':
            #checks if next position is out of map or is an obstacle
            if self.hero_position['y']-1 < 0 or self.map[self.hero_position['y']-1][self.hero_position['x']] == '#':
                return False

            else:
                # makes last hero position '.'
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['y'] -= 1
                #  if there is treasure picks is up
                if self.map[self.hero_position['y']][self.hero_position['x']] == 'T':
                    self.collect_treasure(self.hero[0])
                # moves hero
                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True

        elif direction == 'down':
            #checks if next position is out of map or is an obstacle
            if self.hero_position['y']+1 > len(self.map)-1 or self.map[self.hero_position['y']+1][self.hero_position['x']] == '#':
                return False

            else:
                # makes last hero position '.'
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['y'] += 1
                #  if there is treasure picks is up
                if self.map[self.hero_position['y']][self.hero_position['x']] == 'T':
                    self.collect_treasure(self.hero[0])                
                # moves hero
                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True

        elif direction == 'right':
            #checks if next position is out of map or is an obstacle
            if self.hero_position['x']+1 > len(self.map)-1 or self.map[self.hero_position['y']][self.hero_position['x']+1] == '#':
                return False

            else:
                # makes last hero position '.'
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['x'] += 1
                #  if there is treasure picks is up
                if self.map[self.hero_position['y']][self.hero_position['x']] == 'T':
                    self.collect_treasure(self.hero[0])
                # moves hero
                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True
        
        elif direction == 'left':
            #checks if next position is out of map or is an obstacle
            if self.hero_position['x']-1 < 0 or self.map[self.hero_position['y']][self.hero_position['x']-1] == '#':
                return False

            else:
                # makes last hero position '.'
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['x'] -= 1
                #  if there is treasure picks is up
                if self.map[self.hero_position['y']][self.hero_position['x']] == 'T':
                    self.collect_treasure(self.hero[0])
                # moves hero
                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True


    def scan(self):
        #scans area around hero for potential enemies
        pass
        



tez = Dungeon('level1.txt')