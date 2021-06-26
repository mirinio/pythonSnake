from random import randint
import pygame
from settings import *

class Snake:
    """Schlangenklasse mit all den bildern und der bewegungslogik """

    def __init__(self, parent_screen, length = 3):
        self.parent_screen = parent_screen
        
        self.head_img_right = pygame.image.load("resources/snake_head_right.png")
        self.head_img_left = pygame.image.load("resources/snake_head_left.png")
        self.head_img_up = pygame.image.load("resources/snake_head_up.png")
        self.head_img_down = pygame.image.load("resources/snake_head_down.png")

        self.body_img_left = pygame.image.load("resources/snake_body_left.png")
        self.body_img_right = pygame.image.load("resources/snake_body_right.png")
        self.body_img_up = pygame.image.load("resources/snake_body_up.png")
        self.body_img_down = pygame.image.load("resources/snake_body_down.png")

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
        
        self.x = [randint(0, 18) * BLOCK_SIZE] * length
        self.y = [randint(0, 12) * BLOCK_SIZE] * length
 
        self.x[1] = self.x[0] - 1
        self.x[2] = self.x[1] - 1
        

    def draw(self):
        """Zeichnet die Schlange jenach bewegungsrichtung anders"""
        self.update_head_img()
        self.update_tail_img()
        for i in range(self.length):
            block_rect = pygame.rect.Rect(self.x[i], self.y[i], 128, 128)            
            
            if i == 0:
                self.parent_screen.blit(self.head_img, block_rect)  
                continue
            if i == self.length - 1:
                self.parent_screen.blit(self.tail_img, block_rect)  
                continue
            else:
                previous_x = self.x[i-1] - self.x[i]
                next_x = self.x[i+1] - self.x[i]
                previous_y = self.y[i-1] - self.y[i]
                next_y = self.y[i+1] - self.y[i]
                
                if previous_x == next_x:
                    self.parent_screen.blit(self.body_img_up, block_rect)
                    continue
                elif previous_y == next_y:
                    self.parent_screen.blit(self.body_img_right, block_rect)
                    continue
                elif previous_x == -BLOCK_SIZE and next_y == -BLOCK_SIZE or previous_y == -BLOCK_SIZE and next_x == -BLOCK_SIZE:
                    self.parent_screen.blit(self.curve_img_up_left, block_rect)  
                    continue
                elif previous_x == BLOCK_SIZE and next_y == -BLOCK_SIZE or previous_y == -BLOCK_SIZE and next_x == BLOCK_SIZE:
                    self.parent_screen.blit(self.curve_img_up_right, block_rect)
                    continue
                elif previous_x == -BLOCK_SIZE and next_y == BLOCK_SIZE or previous_y == BLOCK_SIZE and next_x == -BLOCK_SIZE:
                    self.parent_screen.blit(self.curve_img_down_left, block_rect)
                    continue
                elif previous_x == BLOCK_SIZE and next_y == BLOCK_SIZE or previous_y == BLOCK_SIZE and next_x == BLOCK_SIZE:
                    self.parent_screen.blit(self.curve_img_down_right, block_rect)
                    continue
        

    def update_head_img(self):
        """stellt fest in welche richtung der kopf schauen soll"""
        if self.x[0] > self.x[1]:
            self.head_img = self.head_img_right  
        elif self.x[0] < self.x[1]:
            self.head_img = self.head_img_left
        elif self.y[0] > self.y[1]:
            self.head_img = self.head_img_down
        elif self.y[0] < self.y[1]:
            self.head_img = self.head_img_up

    def update_tail_img(self):
        """stellt fest in welche richtung der Schwanz schauen soll"""
        if self.x[self.length-2] > self.x[self.length-1]:
            self.tail_img = self.tail_img_right
        elif self.x[self.length-2] < self.x[self.length-1]:
              self.tail_img = self.tail_img_left
        elif self.y[self.length-2] > self.y[self.length-1]:
            self.tail_img = self.tail_img_down
        elif self.y[self.length-2] < self.y[self.length-1]:
            self.tail_img = self.tail_img_up


    def move_left(self):
        """bewegt die schlange nach links"""
        if self.x[0] < BLOCK_SIZE:
            self.x[0] = SCREEN_WIDTH - BLOCK_SIZE
        else:
            self.x[0] -= BLOCK_SIZE

    def move_right(self):
        """bewegt die schlange nach rechts"""
        if self.x[0] > SCREEN_WIDTH - BLOCK_SIZE:
            self.x[0] = 1
        else:
            self.x[0] += BLOCK_SIZE

    def move_up(self):
        """bewegt die schlange nach oben"""
        if self.y[0] < BLOCK_SIZE:
            self.y[0] = SCREEN_HEIGHT - BLOCK_SIZE
        else:
            self.y[0] -= BLOCK_SIZE

    def move_down(self):
        """bewegt die schlange nach unten"""
        if self.y[0] > SCREEN_HEIGHT - BLOCK_SIZE:
            self.y[0] = 0
        else:
            self.y[0] += BLOCK_SIZE

    def move(self):
        """bewegt die schlange"""
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
        """macht die schlange grösser"""
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_direction_check(self, direction):
        """stellt fest das man nicht rückwerts in sich selbst bewegen kann"""
        if  direction == "UP" and not self.move_direction == "DOWN" or \
        direction == "DOWN" and not self.move_direction == "UP" or \
        direction == "LEFT" and not self.move_direction == "RIGHT" or \
        direction == "RIGHT" and not self.move_direction == "LEFT":
            self.move_direction = direction