import pygame
from pygame.locals import *
from pygame.sprite import Sprite, RenderUpdates
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

numLinhas = 8 # A tabela tem 8 linhas
numColunas = 5 # A tabela tem 5 colunas
flag = False
p=0
r=1
Tab = [[[100*i,100*j] for j in range(numColunas)] for i in range(numLinhas)] 

# inicia a linha e coluna dum circulo que inicialmente está seleccionado
xSele=0
ySele=0

# inicia a linha e coluna do circulo onde está o cursor do rato
xPre=0
yPre=0
# existe um circulo seleccionado  
Selected = True

class Quad(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.cenas=True
        
        self.rect = self.image.get_rect()
##    def render(self):
##        screen.blit(self.image,(self.x, self.y)) #render da sprite no ecra

##        self.onMouseClick = self.image.fill(red)
class Seta(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        
# Inicia Pygame
pygame.init()

# Define o ecrã
size=[800,500]
screen=pygame.display.set_mode(size)

# escreve titulo da janela 
pygame.display.set_caption("Grid - 0.0")


##quad_list = pygame.sprite.Group()
##seta_list = pygame.sprite.Group()
##all_sprites_list = pygame.sprite.Group()

# Create a red player block
seta = Seta(red, 5, 5)
##quad_list.add(seta)
##all_sprites_list.add(seta)

squareR = Quad(red, 60, 60)
squareW = Quad(white, 60, 60)


#Para entrar em loop, até que a janela seja fechada.
done=False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


for i in range(numLinhas):
        for j in range(numColunas):
            x = Tab[i][j][0]
            y = Tab[i][j][1]
            squareW = Quad(white, 60, 60)

            squareW.rect.x = x+20
            squareW.rect.y = y+20

            #screen.blit(squareW , (squareW.rect.x,squareW.rect.y))
            
##            quad_list.add(squareW)
##            all_sprites_list.add(squareW)
# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # Clear the screen
    screen.fill(black)

    #coordenadas do rato
    pos = pygame.mouse.get_pos()
    
    #posição do rato
    xR=pos[0]
    yR=pos[1]

    # Set the player object to the mouse location
    seta.rect.x = pos[0]
    seta.rect.y = pos[1]

    for i in range(numLinhas):
        for j in range(numColunas):
            x = Tab[i][j][0]
            y = Tab[i][j][1]
            
            if xR>x and xR<x+100 and yR>y and yR<y+100:
                xPre=j
                yPre=i

                
    mousestat= pygame.mouse.get_pressed() #teclas do rato
    # Selecciona o circulo onde o cursor está posicionado
    if mousestat[0]:
        xSele=xPre
        ySele=yPre

        ValX = Tab[ySele][xSele][0]
        ValY = Tab[ySele][xSele][1]
        
        
        if squareW.cenas == True:
            print ('red')
            if intersect(seta,squareW):
                ##
                
            
##            quad_hit_list = pygame.sprite.spritecollide(seta, quad_list, squareW.cenas)

                
                squareR.rect.x = ValX+20
                squareR.rect.y = ValY+20

                screen.blit(squareR , (squareR.rect.x,squareR.rect.y))
            
##            quad_list.add(squareR)
##            all_sprites_list.add(squareR)

                squareW.cenas = False
                squareR.cenas = True
            
        elif squareR.cenas == True: 
            print("white")

          

##            quad_hit_list = pygame.sprite.spritecollide(seta, quad_list, squareR.cenas)

            squareW.rect.x = ValX+20
            squareW.rect.y = ValY+20

            screen.blit(squareW , (squareW.rect.x,squareW.rect.y))
##            quad_list.add(squareW)
##            all_sprites_list.add(squareW)

            squareR.cenas = False
            squareW.cenas = True
            
        else:
            print("NOP")

            
            
##    print mousestat
##    print xSele
##    print ySele

        
    
     # Caso esteja seleccionado um circulo, desenha quadrado
    # vermelho que o envolva          
##    if Selected:
##        p = p+1
##        print(p)
##        ValX = Tab[ySele][xSele][0]
##        ValY = Tab[ySele][xSele][1]        
##
##        pygame.draw.rect(screen,red,[ValX,ValY,100,100],4)
                
    # Draw all the spites
##    all_sprites_list.draw(screen)        
  
    # Limit to 20 frames per second
    clock.tick(15)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
      
pygame.quit()
