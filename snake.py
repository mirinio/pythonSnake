from random import randint
import pygame
from settings import *

class Snake:
    def __init__(self, parent_screen, length = 3):
        self.parent_screen = parent_screen
        
        self.head_img_right = pygame.image.load("resources/snake_head_right.png")
        self.head_img_left = pygame.image.load("resources/snake_head_left.png")
        self.head_img_up = pygame.image.load("resources/snake_head_up.png")
        self.head_img_down = pygame.image.load("resources/snake_head_down.png")

        self.body_img_left = pygame.image.load("resources/snake_body_left.png")
        self.body_img_right = pygame.image.load("resources/snake_body_right.png")
        self.body_img_up = pygame.image.load("resources/snake_body_up.png")

        self.tail_img_down = pygame.image.load("resources/snake_tail_down.png")
        self.tail_img_up = pygame.image.load("resources/snake_tail_up.png")
        self.tail_img_left = pygame.image.load("resources/snake_tail_left.png")
        self.tail_img_right = pygame.image.load("resources/snake_tail_right.png")

        self.curve_img_down_left = pygame.image.load("resources/snake_curve_down_left.png")
        self.curve_img_down_right = pygame.image.load("resources/snake_curve_down_right.png")
        self.curve_img_up_left = pygame.image.load("resources/snake_curve_up_left.png")
        self.curve_img_up_right = pygame.image.load("resources/snake_curve_up_right.png")

        self.move_direction = ""

        if length < 3:
            self.length = 3
        else:
            self.length = length
        
        self.x = [randint(0, 28) * BLOCK_SIZE] * length
        self.y = [randint(0, 17) * BLOCK_SIZE] * length
 
        self.x[1] = self.x[0] - 1
        self.x[2] = self.x[1] - 1
        

    def draw(self):
        if self.x[0] > self.x[1]:
            self.parent_screen.blit(self.head_img_right, pygame.rect.Rect(self.x[0], self.y[0], 128, 128))
            self.parent_screen.blit(self.tail_img_right, pygame.rect.Rect(self.x[self.length-1], self.y[self.length-1], 128, 128))
        elif self.x[0] < self.x[1]:
            self.parent_screen.blit(self.head_img_left, pygame.rect.Rect(self.x[0], self.y[0], 128, 128))
            self.parent_screen.blit(self.tail_img_left, pygame.rect.Rect(self.x[self.length-1], self.y[self.length-1], 128, 128))
        elif self.y[0] > self.y[1]:
            self.parent_screen.blit(self.head_img_down, pygame.rect.Rect(self.x[0], self.y[0], 128, 128))
            self.parent_screen.blit(self.tail_img_down, pygame.rect.Rect(self.x[self.length-1], self.y[self.length-1], 128, 128))
        elif self.y[0] < self.y[1]:
            self.parent_screen.blit(self.head_img_up, pygame.rect.Rect(self.x[0], self.y[0], 128, 128))
            self.parent_screen.blit(self.tail_img_up, pygame.rect.Rect(self.x[self.length-1], self.y[self.length-1], 128, 128))
        
        for i in range(self.length):
            if not i == 0 and not i == self.length-1:
                if self.x[i] > self.x[i+1] and self.y[i] > self.y[i+1]:
                    self.parent_screen.blit(self.curve_img_up_right, pygame.rect.Rect(self.x[i], self.y[i], 128, 128))  
                elif self.x[i] < self.x[i+1] and self.y[i] > self.y[i+1]:
                    self.parent_screen.blit(self.curve_img_up_left, pygame.rect.Rect(self.x[i], self.y[i], 128, 128))
                elif self.x[i] < self.x[i+1] and self.y[i] < self.y[i+1]:
                    self.parent_screen.blit(self.curve_img_down_left, pygame.rect.Rect(self.x[i], self.y[i], 128, 128))
                elif self.x[i] > self.x[i+1] and self.y[i] < self.y[i+1]:
                    self.parent_screen.blit(self.curve_img_down_right, pygame.rect.Rect(self.x[i], self.y[i], 128, 128))
                elif self.x[i] > self.x[i+1]:
                    self.parent_screen.blit(self.body_img_right, pygame.rect.Rect(self.x[i], self.y[i], 128, 128))
                elif self.x[i] < self.x[i+1]:
                    self.parent_screen.blit(self.body_img_left, pygame.rect.Rect(self.x[i], self.y[i], 128, 128))
                else:
                    self.parent_screen.blit(self.body_img_up, pygame.rect.Rect(self.x[i], self.y[i], 128, 128))
        

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

    def move_direction_check(self, direction):
        if  direction == "UP" and not self.move_direction == "DOWN" or \
        direction == "DOWN" and not self.move_direction == "UP" or \
        direction == "LEFT" and not self.move_direction == "RIGHT" or \
        direction == "RIGHT" and not self.move_direction == "LEFT":
            self.move_direction = direction