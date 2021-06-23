import pygame
import random

from pygame.display import init
from settings import *


class Item:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image_names = ["coffee.png", "bottle.png","dose.png", "garbage.png", "mask.png", "plastic_big.png", "plastic_small.png", "straw.png"]
        self.image_name = self.image_names[random.randint(0,7)]
        self.move_random()
        


    def draw(self):
        self.parent_screen.blit(pygame.image.load("resources/"+ self.image_name), (self.x, self.y))

    def move_random(self):
        self.x = random.randint(0, 28) * BLOCK_SIZE
        self.y = random.randint(0, 17) * BLOCK_SIZE


class ItemManager:

    def __init__(self, game):
        self.game = game
        randomItem1 = Item(self.game.screen)
        randomItem2 = Item(self.game.screen)
        randomItem3 = Item(self.game.screen)
        randomItem4 = Item(self.game.screen)

        self.items = []
        self.items.append(randomItem1)
        self.items.append(randomItem2)
        self.items.append(randomItem3)
        self.items.append(randomItem4)

    def draw_all(self):
        for item in self.items:
            item.draw()
