import pygame

class Snake:
    def __init__(self) -> None:
        self.coordinates = [(5,6),(6,6),(7,6)]
        self.curr_dir = 'UP'
    
    def collision(self, x, y):
        # if snake bites itself
        if (x,y) in self.coordinates[4:]:
            return True
        
        # touches boundary
        if x > 14 or x < 0 or y > 14 or y < 0:
            return True

        return False
    

    def move(self, direction, board): 
        x, y  = self.coordinates[-1]
        
        if direction == 'UP' and self.curr_dir != 'DOWN':
            y -= 1
            self.curr_dir = 'UP'
        elif direction == 'DOWN' and self.curr_dir != 'UP':
            y += 1
            self.curr_dir = 'DOWN'
        elif direction == 'RIGHT' and self.curr_dir != 'LEFT':
            x += 1
            self.curr_dir = 'RIGHT'
        elif direction == 'LEFT' and self.curr_dir != 'RIGHT':
            x -= 1
            self.curr_dir = 'LEFT'
        

        if self.collision(x, y):
            print("Game Over")
            return
        self.coordinates.append((x,y))
        self.coordinates.pop(0)
    
    def walk(self, board):
        x, y  = self.coordinates[-1]
        if self.curr_dir == 'UP':
            y -= 1
        elif self.curr_dir == 'DOWN':
            y += 1
        elif self.curr_dir == 'RIGHT':
            x += 1
        else:
            x -= 1
        if self.collision(x, y):
            print('Game Over')
            return
        self.coordinates.append((x,y))
        self.coordinates.pop(0)
    
    def show(self, surface):
        block = pygame.image.load("resources/block.jpg")
        for i, j in self.coordinates:
            surface.blit(block, (40*i, 40*j))
        



        
    


