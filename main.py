import pygame
import time 
from pygame.locals import *


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/Block.PNG").convert()
        self.x = 100
        self.y = 100
    

    def draw(self):
        self.parent_screen.fill((110,110,5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((110,110,5))
        pygame.display.flip()
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running == False
                    if event.key == K_UP:
                        self.snake.y -= 10
                    if event.key == K_DOWN:
                        self.snake.y += 10
                    if event.key == K_LEFT:
                        self.snake.x -= 10
                    if event.key == K_RIGHT:
                        self.snake.x += 10
                    self.snake.draw()
                elif event.type == QUIT:
                    running = False

if __name__ == "__main__":
    
    game = Game()
    game.run()