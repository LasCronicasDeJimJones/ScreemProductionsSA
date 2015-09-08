import pygame
import constantes
from funciones_spritesheet import SpriteSheet



'''
import pygame

from funciones_spritesheet import *
import jugador
from jugador import Player
pinchos            = (0, 0, 264, 89)


class Enemigo(pygame.sprite.Sprite):
   
    avance_jugador = 132

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        #sprite_sheet = SpriteSheet("imagenes/pinchos.png")
       
        self.image = pygame.image.load("imagenes/pinchoshd.png").convert()
        self.rect = self.image.get_rect()    


        self.image.set_colorkey(constantes.BLANCO)

'''
botella = (0, 0, 264, 89)

class Provision (pygame.sprite.Sprite):    
     
    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/botellasprite.jpg.png").convert()
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()   
        
        self.image.set_colorkey(constantes.BLANCO)
        
        
                   
        
        