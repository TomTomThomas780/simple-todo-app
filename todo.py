import pygame
import sys

pygame.init() 

class TodoItem:
    def __init__(self,priority,title,description,completed=False):
        self.completed = completed # True or False
        self.priority = priority # 0-5(0 is highest)
        self.title = title # string
        self.description = description # string
        
    def __repr__(self):
        return f'TodoItem({self.priority},{self.title},{self.description},{self.completed})' #reproduc a same object

class Todo:
    def __init__(self):
        # Initialize the game
        self.screen = pygame.display.set_mode((500,800),pygame.RESIZABLE)
        self.todo_items = []
        self.bg_color = (255,255,255)
        pygame.display.set_caption('Todo')
        
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()
    
    def main(self):
        while True:
            self._check_events()
            self._update_screen()
            
            
if __name__ == '__main__':
    t=Todo()
    t.main()