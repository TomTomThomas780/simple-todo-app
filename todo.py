import pygame
import sys

pygame.init() 

class Text:
    def __init__(self,ai_game,text,color):
        self.text = text
        self.font = pygame.font.SysFont('SimSun', 48)
        self.text_color = color 
        self.rect = pygame.Rect(0,0,100,100)
        self.screen = ai_game.screen
        
    def _prep_msg(self):
        self.msg_image = self.font.render(self.text, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
class ColoredText(Text):
    def __init__(self,ai_game,text,color,backgroundcolor):
        super().__init__(ai_game,text,color)
        self.font = pygame.font.SysFont('Maple Mono NF CN', 10)
        self.bg_color = backgroundcolor
        
    def _prep_msg(self,rect):
        self.msg_image = self.font.render(self.text, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = rect.center
        self.msg_image_rect.left = rect.left

    def draw(self):
        self.screen.fill(self.bg_color,self.rect)
        if self.bg_color[0]+10>255:
            r=self.bg_color[0]
        else:
            r=self.bg_color[0]+10
        if self.bg_color[1]+10>255:
            g=self.bg_color[1]
        else:
            g=self.bg_color[1]+10
        if self.bg_color[2]+10>255:
            b=self.bg_color[2]
        else:
            b=self.bg_color[2]+10
        
        color = pygame.Color(r,g,b,128)
        pygame.draw.rect(self.screen,color,self.rect,1)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class TodoItem:
    def __init__(self,priority,title):
        self.priority = priority # 0-5(0 is highest)
        self.title = title # string
        
    def __repr__(self):
        return f'TodoItem({self.priority},{self.title})' #reproduc a same object



class Todo:
    def __init__(self):
        # Initialize the game
        self.screen = pygame.display.set_mode((300,300),pygame.RESIZABLE)
        self.todo_items = []
        self.todo_items_rects=[]
        self.check_for_mouse=True
        try:
            with open('todo.txt') as f:
                for line in f:
                    try:
                        title,priority = line.split(',')
                        self.todo_items.append(TodoItem(int(priority),title))
                    except:
                        try:
                            self.todo_items.append(TodoItem(self.todo_items[-1].priority,'We\'ve got some error reading todo.txt.'))
                            self.todo_items.append(TodoItem(self.todo_items[-1].priority,'Please check todo.txt.'))
                            self.todo_items.append(TodoItem(self.todo_items[-1].priority,'Make sure you are following the format.'))
                            self.todo_items.append(TodoItem(self.todo_items[-1].priority,'Format: title,priority'))
                        except:
                            self.todo_items.append(TodoItem(0,'We\'ve got some error reading todo.txt.'))
                            self.todo_items.append(TodoItem(0,'Please check todo.txt.'))
                            self.todo_items.append(TodoItem(0,'Make sure you are following the format.'))
                            self.todo_items.append(TodoItem(0,'Format: title,priority'))
        except FileNotFoundError:
            self.todo_items.append(TodoItem(0,'Pleas add your tasks in todo.txt.'))
            self.todo_items.append(TodoItem(1,'Format: title,priority'))
            self.todo_items.append(TodoItem(2,'Priority is 0-5.(0 is highest)'))
            self.check_for_mouse=False
        except:
            self.todo_items.append(TodoItem(0,'We\'ve got some error here.'))
            self.todo_items.append(TodoItem(1,'Please check todo.txt.'))
            self.todo_items.append(TodoItem(2,'Problem still occurs? Please contact thomasjinzihao@icloud.com through email.'))
        self.todo_items=sorted(self.todo_items,key=lambda x:x.priority)
        self.bg_color = (255,255,255)
        pygame.display.set_caption('Todo')
        #add texts
        self.welcome_text = Text(self,'TODO', (0,0,0))
        self.welcome_text.rect.center = self.screen.get_rect().center
        self.welcome_text.rect.top = self.screen.get_rect().top
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    for i in range(0,len(self.todo_items)):
                        item=self.todo_items_rects[i]
                        if item.collidepoint(mouse_pos) and self.check_for_mouse:
                            todo_item_item=self.todo_items[i]
                            self.todo_items.remove(todo_item_item)
                            if len(self.todo_items)==0:
                                self.todo_items=[TodoItem(0,'You'),TodoItem(1,'have'),TodoItem(2,'finished'),TodoItem(3,'all'),TodoItem(4,'your'),TodoItem(5,'tasks!')]
                                self.check_for_mouse=False
                                self.welcome_text.text='CONGRATULATIONS!'
                            break
                        
    def _prep_text(self):
        self.welcome_text.rect.center = self.screen.get_rect().center
        self.welcome_text.rect.top = self.screen.get_rect().top
        self.welcome_text._prep_msg()
        self.welcome_text.draw()
        
        last_rect = self.welcome_text.rect
        self.todo_items_rects=[]
        for item in self.todo_items:
            if item.priority==0:
                color_this = (245,0,0)
            elif item.priority==1:
                color_this = (245,135,0)
            elif item.priority==2:
                color_this = (245,245,0)
            elif item.priority==3:
                color_this = (135,245,0)
            elif item.priority==4:
                color_this = (0,245,0)
            elif item.priority==5:
                color_this = (0,245,245)
            button_this = ColoredText(self,item.title,(0,0,0),color_this)
            button_this.rect = pygame.Rect(0,0,self.screen.get_rect().width,(self.screen.get_rect().height-100)/(len(self.todo_items)))
            button_this.rect.top = last_rect.bottom
            last_rect = button_this.rect
            self.todo_items_rects.append(button_this.rect)
            button_this._prep_msg(button_this.rect)
            button_this.draw()
                
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self._prep_text()
        pygame.display.flip()
        
    
    def main(self):
        while True:
            self._check_events()
            self._update_screen()
            
            
if __name__ == '__main__':
    t=Todo()
    t.main()