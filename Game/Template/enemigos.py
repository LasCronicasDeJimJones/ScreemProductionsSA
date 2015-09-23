import pygame
from funciones_spritesheet import *
import jugador
from jugador import Player

PINCHO           = (21,532, 652, 58)


class Pincho(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheet("imagenes/pinchito.png")
        
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],sprite_sheet_data[1],sprite_sheet_data[2],sprite_sheet_data[3])
        self.image = pygame.transform.scale(self.image, (217, 19))
        #self.image.set_colorkey(constantes.NEGRO)
        
        self.rect = self.image.get_rect()    
        
        
        
                   
        
        