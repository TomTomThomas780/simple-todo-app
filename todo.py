import pygame
import sys

pygame.init() 

class Text:
    def __init__(self,ai_game,text,color):
        self.text = text
        self.font = pygame.font.SysFont('SimSun', 48)
        self.text_color = color 
        self.rect = pygame.Rect(0,0,200,300)
        self.screen = ai_game.screen
        
    def _prep_msg(self):
        self.msg_image = self.font.render(self.text, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

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
        
        #add texts
        self.welcome_text = Text(self,'Welcome to Todo', (0,0,0))
        self.welcome_text.rect.center = self.screen.get_rect().center
        self.welcome_text._prep_msg()
        
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
    def _prep_text(self):
        self.welcome_text.rect.center = self.screen.get_rect().center
        self.welcome_text._prep_msg()
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.welcome_text.draw()
        pygame.display.flip()
        

    
    def main(self):
        while True:
            self._prep_text()
            self._check_events()
            self._update_screen()
            
            
if __name__ == '__main__':
    t=Todo()
    t.main()