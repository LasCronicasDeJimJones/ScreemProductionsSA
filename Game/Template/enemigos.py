import pygame
from funciones_spritesheet import *
import jugador
from jugador import Player

PINCHO           = (0,0, 499, 39)
PINCHO2          = (1,126,498,42)   
PINCHO3          = (1,240,498,42)
PINCHO4          = (1,372,499,41)

class Pincho(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheet("imagenes/pinchito.png")
        
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],sprite_sheet_data[1],sprite_sheet_data[2],sprite_sheet_data[3])
        self.image = pygame.transform.scale(self.image, (249, 19))
        #self.image.set_colorkey(constantes.NEGRO)
        
        self.rect = self.image.get_rect()    
        
        
        
                   
        
        