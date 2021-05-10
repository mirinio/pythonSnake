import pygame
import time
from settings import *

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert_alpha()
        self.move_direction = ""
        
        self.length = length
        self.x = [BLOCK_SIZE] * length
        self.y = [BLOCK_SIZE] * length

    def draw(self):
  
        for i in range(self.length):
            self.parent_screen.blit(self.block, pygame.rect.Rect(self.x[i], self.y[i],128,128))
        pygame.display.flip()

    def move_left(self):
        self.x[0] -= BLOCK_SIZE
    def move_right(self):
        self.x[0] += BLOCK_SIZE
    def move_up(self):
        self.y[0] -= BLOCK_SIZE
    def move_down(self):
        self.y[0] += BLOCK_SIZE

    def move(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.move_direction == "UP":
            self.move_up()
        elif self.move_direction == "DOWN":
            self.move_down()
        elif self.move_direction == "RIGHT":
            self.move_right()
        elif self.move_direction == "LEFT":
            self.move_left()
        self.draw()

    def grow(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)