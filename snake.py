import pygame
import time
import numpy as np

class Snacke(object):
    def __init__(self,screen,length):
        self.length=length
        self.screen=screen
        self.x=[40]*self.length
        self.y=[40]*self.length
        self.direction='down'
        self.block=pygame.image.load('resources/block.jpg')
        
    def render_background(self):
        background=pygame.image.load('resources/background.jpg')
        self.screen.blit(background,(0,0))
        pygame.display.flip()
    def draw(self):
        self.render_background()
        for i in range(len(self.x)):
            self.screen.blit(self.block,(self.x[i],self.y[i]))
    def move_up(self):
        if self.y[0]-40==self.y[1] and self.x[0]==self.x[1] :
            return
        self.direction='up'
    def move_down(self):
        if self.y[0]+40==self.y[1] and self.x[0]==self.x[1] :
            return
        self.direction='down'
    def move_left(self):
        if self.y[0]==self.y[1] and self.x[0]-40==self.x[1] :
            return
        self.direction='left'
    def move_right(self):
        if self.y[0]==self.y[1] and self.x[0]+40==self.x[1] :
            return
        self.direction='right'
    
    def walke(self):
        for i in range(len(self.x)-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
            
        if self.direction=='up':
            self.y[0]-=40
            if self.y[0]<0:
                self.y[0]=600
        elif self.direction=='down':
            self.y[0]+=40
            if self.y[0]>600:
                self.y[0]=0
        elif self.direction=='left':
            self.x[0]-=40
            if self.x[0]<0:
                self.x[0]=1000
        elif self.direction=='right':
            self.x[0]+=40
            if self.x[0]>1000:
                self.x[0]=0
        
        self.draw()
      
      
      
        
#Apple class
class Apple(object):
    def __init__(self,screen):
        self.screen=screen
        self.x=np.random.randint(0,1000-2)
        self.y=np.random.randint(0,600-2)
        self.apple=pygame.image.load('resources/apple.jpg')
    def Draw(self):
        self.screen.blit(self.apple,(self.x,self.y))
        




# Game classe
class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play()
        self.snacke=Snacke(self.screen,3)
        self.apple=Apple(self.screen)
        
    def Game_over(self):
        pygame.mixer_music.pause()
        self.screen.fill((0,0,0))
        font=pygame.font.SysFont('arial',30,True)
        gameOver=font.render(f'Game Over Your Score is: {self.snacke.length} ',True,(255,255,255))
        line1=font.render('To play again press enter. to exite press escape',True,(255,255,255))
        self.screen.blit(gameOver,(1000/2-200,600/2-100))
        self.screen.blit(line1,(1000/2-300,600/2-50))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                    if event.key==pygame.K_RETURN:
                        pygame.mixer_music.unpause()
                        self.__init__()
                        return
            
    
    def display_score(self):
        font=pygame.font.SysFont('arial',30,True)
        score=font.render(f'the score: {self.snacke.length}',True,(255,255,255))
        self.screen.blit(score,(800,10))
    def is_collision(self,x1,y1,x2,y2):
        apple_d=pygame.Rect(x2,y2,40,40)
        snacke_d=pygame.Rect(x1,y1,40,40)
        if apple_d.colliderect(snacke_d):
            return True
        
    
    def play(self):
        self.snacke.walke()
        if self.is_collision(self.snacke.x[0],self.snacke.y[0],self.apple.x,self.apple.y):
            sound=pygame.mixer.Sound('resources/ding.mp3')
            pygame.mixer.Sound.play(sound)
            self.apple.x=np.random.randint(0,1000-2)
            self.apple.y=np.random.randint(0,600-2)
            self.snacke.x.append(self.snacke.x[self.snacke.length-1])
            self.snacke.y.append(self.snacke.y[self.snacke.length-1])
            self.snacke.length+=1
        
        for i in range(1,self.snacke.length):
            if self.is_collision(self.snacke.x[0],self.snacke.y[0],self.snacke.x[i],self.snacke.y[i]):
                crach=pygame.mixer.Sound('resources/crash.mp3')
                pygame.mixer.Sound.play(crach)
                raise 'game over'
            
        self.apple.Draw()
        self.display_score()
        pygame.display.flip()

        
    def run(self):
        self.running =True
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        self.snacke.move_up()
                    elif event.key==pygame.K_DOWN:
                        self.snacke.move_down()
                    elif event.key==pygame.K_LEFT:
                        self.snacke.move_left()
                    elif event.key==pygame.K_RIGHT:
                       self.snacke.move_right()
            try:
                self.play()
            except :
                self.Game_over()
            time.sleep(0.3)
         
    
        







gn=Game()
gn.run()


        