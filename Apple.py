import pygame
import random
from settings import *


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg")
        self.parent_screen = parent_screen
        self.x = BLOCK_SIZE * 3
        self.y = BLOCK_SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move_random(self):
        self.x = random.randint(0, 12) * BLOCK_SIZE
        self.y = random.randint(0, 7) * BLOCK_SIZE