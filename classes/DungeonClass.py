from pprint import pprint
from classes.EnemyClass import Enemy
from classes.HeroClass import Hero
from classes.spell import Spell
from classes.weapon import Weapon
    
class Dungeon:
    def __init__(self, map = str):
        with open(map) as f:
            self.map = f.readlines()
        self.map = [list(x.strip()) for x in self.map]

        self.hero_position = dict()

    def print_map(self):
        print([''.join(x) for x in self.map])

    def spawn(self, hero):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 'S':
                    self.hero_position['y'] = y
                    self.hero_position['x'] = x
                    self.map[y][x] = 'H'
                    return True
        return False

    def move_hero(self, direction):
        if direction == 'up':
            if self.hero_position['y']-1 < 0 or self.map[self.hero_position['y']-1][self.hero_position['x']] == '#':
                return False
            else:
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['y'] -= 1
                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True

        elif direction == 'down':
            if self.hero_position['y']+1 > len(self.map)-1 or self.map[self.hero_position['y']+1][self.hero_position['x']] == '#':
                return False
            else:
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['y'] += 1
                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True

        elif direction == 'right':
            if self.hero_position['x']+1 > len(self.map)-1 or self.map[self.hero_position['y']][self.hero_position['x']+1] == '#':
                return False
            else:
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['x'] += 1
                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True
        
        elif direction == 'left':
            if self.hero_position['x']-1 < 0 or self.map[self.hero_position['y']][self.hero_position['x']-1] == '#':
                return False
            else:
                self.map[self.hero_position['y']][self.hero_position['x']] = '.'
                self.hero_position['x'] -= 1
                self.map[self.hero_position['y']][self.hero_position['x']] = 'H'
                return True


    def scan(self):
        #scans area around hero for potential enemies
        pass
        
    