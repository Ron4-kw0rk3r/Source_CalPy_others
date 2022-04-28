#!/usr/bin/env python3.8

#import py
#from curses import KEY_SUSPEND
#from curses.textpad import rectangle
import pygame
from pygame import *
import sys 

pygame.init()
SCREENH=1000
SCREENW =720
colors = [ '#000000' , '#f1f1f1', '#f4f422' ] 

def calc_gui():

    screen = pygame.display.set_mode((SCREENW, SCREENH),32)
    pygame.display.set_caption('title')
    
        

    ron = True
    while ron:
        from objects import rectA , rectB, rectC, rectD, rectE, rectF, rectG
        from objects import rectOn1 , rectOn2, rectOn3 , rectOn4 , rectOn5, rectOn6, rectOn7
        from objects import rect11Ran ,rect1TAn ,rect2TAn , rect3TAn, rect4TAn, rect5TAn, rect6TAn
        from objects import rectFunX , rectF0nX , rectF1unX , rectF2unX , rectF3unX , rectF4unX , rectF5unX
        pygame.display.init()
        screen.fill(colors[1])
        pygame.draw.rect(screen , (colors[0]), rectA, 1  )
        pygame.draw.rect(screen , (colors[0]), rectB, 1  )
        pygame.draw.rect(screen , (colors[0]), rectC, 1  )
        pygame.draw.rect(screen , (colors[0]), rectD, 1  )
        pygame.draw.rect(screen , (colors[0]), rectE, 1  )
        pygame.draw.rect(screen , (colors[0]), rectF, 1  )
        pygame.draw.rect(screen , (colors[0]), rectG, 1  )
        pygame.draw.rect(screen ,  (colors[0]), rectOn1, 1)
        pygame.draw.rect(screen ,  (colors[0]), rectOn2, 1)
        pygame.draw.rect(screen ,  (colors[0]), rectOn3, 1)
        pygame.draw.rect(screen ,  (colors[0]), rectOn4, 1)
        pygame.draw.rect(screen ,  (colors[0]), rectOn5, 1)

        pygame.draw.rect(screen ,  (colors[0]), rectOn6, 1)
        pygame.draw.rect(screen ,  (colors[0]), rectOn7, 1)

        pygame.draw.rect(screen , (colors[0]), rect11Ran , 1 )
        pygame.draw.rect(screen , (colors[0]), rect1TAn , 1)
        pygame.draw.rect(screen , (colors[0]), rect2TAn , 1)
        pygame.draw.rect(screen , (colors[0]), rect3TAn , 1)
        pygame.draw.rect(screen , (colors[0]), rect4TAn , 1)
        pygame.draw.rect(screen , (colors[0]), rect5TAn , 1)
        pygame.draw.rect(screen , (colors[0]), rect6TAn , 1)

        pygame.draw.rect(screen , (colors[0]), rectFunX, 1 )
        pygame.draw.rect(screen , (colors[0]), rectF0nX, 1 )
        pygame.draw.rect(screen , (colors[0]), rectF1unX, 1 )
        pygame.draw.rect(screen , (colors[0]), rectF2unX, 1 )
        pygame.draw.rect(screen , (colors[0]), rectF3unX, 1 )
        pygame.draw.rect(screen , (colors[0]), rectF4unX, 1 )
        pygame.draw.rect(screen , (colors[0]), rectF5unX, 1 )
        for axiss in pygame.event.get():
            if axiss.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            key = pygame.key.get_pressed()

            if axiss.type == pygame.KEYUP:
                if axiss.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    calc_gui()
