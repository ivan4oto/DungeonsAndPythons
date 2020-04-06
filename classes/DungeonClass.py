from random import shuffle
from .EnemyClass import Enemy
from .HeroClass import Hero
from .spell import Spell
from .weapon import Weapon
from .treasure import Treasure
    
class Dungeon:
    def __init__(self, map = str):
        with open(map) as f:
            self.map = f.readlines()
        self.map = [list(x.strip()) for x in self.map]
        self.treasures = []
        self.enemies = []
        self.hero_position = dict()

    def fill_treasures_list(self, treasures = 'str'):
        with open(treasures) as f:
            self.treasures = f.readlines()
        self.treasures = [x.strip() for x in self.treasures]
        self.treasures = [x.split(',') for x in self.treasures]
        self.treasures = [Treasure(*x) for x in self.treasures]

    def fill_enemies_list(self, enemies = 'str'):
        with open(enemies) as f:
            self.enemies = f.readlines()
        self.enemies = [x.strip() for x in self.enemies]
        self.enemies = [x.split(',') for x in self.enemies]
        self.enemies = [list(map(int, results)) for results in self.enemies]
        self.enemies = [Enemy(*x) for x in self.enemies]

    def print_map(self):
        print([''.join(x) for x in self.map])

    def spawn(self, new_hero):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 'S':
                    self.hero_position['y'] = y
                    self.hero_position['x'] = x
                    self.map[y][x] = 'H'
                    return True
        return False

    def move_hero(self, direction, hero):
        if direction == 'up':
            if self.hero_position['y']-1 < 0 or self.map[self.hero_position['y']-1][self.hero_position['x']] == '#':
                return False
            else:
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['y'] -= 1
                #pickup treasure
                if self.map[self.hero_position['y']][self.hero_position['x']] == 'T':
                    shuffle(self.treasures)
                    hero.add_item(self.treasures.pop())

                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True

        elif direction == 'down':
            if self.hero_position['y']+1 > len(self.map)-1 or self.map[self.hero_position['y']+1][self.hero_position['x']] == '#':
                return False
            else:
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['y'] += 1
                #pickup treasure
                if self.map[self.hero_position['y']][self.hero_position['x']] == 'T':
                    shuffle(self.treasures)
                    hero.add_item(self.treasures.pop())

                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True

        elif direction == 'right':
            if self.hero_position['x']+1 > len(self.map[0])-1 or self.map[self.hero_position['y']][self.hero_position['x']+1] == '#':
                return False
            else:
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['x'] += 1
                #pickup treasure
                if self.map[self.hero_position['y']][self.hero_position['x']] == 'T':
                    shuffle(self.treasures)
                    hero.add_item(self.treasures.pop())

                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True
        
        elif direction == 'left':
            if self.hero_position['x']-1 < 0 or self.map[self.hero_position['y']][self.hero_position['x']-1] == '#':
                return False
            else:
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['x'] -= 1
                #pickup treasure
                if self.map[self.hero_position['y']][self.hero_position['x']] == 'T':
                    shuffle(self.treasures)
                    hero.add_item(self.treasures.pop())

                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True

    def scan(self, scanrange):
        foundEnemies = []
        #Searches the Y axis
        for y in range((self.hero_position['y']-scanrange), self.hero_position['y']+scanrange+1):
            if y > 0 and y < len(self.map)-1:
                if self.map[y][self.hero_position['x']] == 'E':
                    #appends enemy coordinates and enemy distance from hero
                    foundEnemies.append([(y, self.hero_position['x']), abs(self.hero_position['y']-y)])
        #Searches the X axis
        for x in range((self.hero_position['x']-scanrange), self.hero_position['x']+scanrange+1):
            if x > 0 and x < len(self.map[self.hero_position['y']-1]):
                if self.map[self.hero_position['y']][x] == 'E':
                    #appends enemy coordinates and enemy distance from hero
                    foundEnemies.append([(self.hero_position['y'], x),abs(self.hero_position['x']-x)])

        return foundEnemies
