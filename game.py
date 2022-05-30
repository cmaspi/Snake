import pygame
from pygame.locals import *
from snake import Snake
import time

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((600,600))
        self.background = pygame.image.load("resources/background-resized.jpg")
        self.surface.blit(self.background, (0,0))
        self.snake = Snake()
        self.snake.show(self.surface)
        pygame.display.update()
    
    def run(self):
        running = True
        turn = 1
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            key = pygame.key.get_pressed()                
            if key[K_ESCAPE]:
                running = False
            elif key[K_RIGHT]:
                self.snake.move('RIGHT', None)
            elif key[K_LEFT]:
                self.snake.move('LEFT', None)
            elif key[K_UP]:
                self.snake.move('UP', None)
            elif key[K_DOWN]:
                self.snake.move('DOWN', None)
            self.surface.blit(self.background, (0,0))
            self.snake.show(self.surface)
            pygame.display.update()
            time.sleep(0.2)
            if turn == 1:
                self.snake.walk(None)
                turn -= 4
            turn += 1
            
