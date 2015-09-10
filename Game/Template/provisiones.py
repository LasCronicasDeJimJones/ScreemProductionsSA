import pygame
import constantes
from funciones_spritesheet import SpriteSheet
#import pygame

#from funciones_spritesheet import *
#import jugador
#from jugador import Player
#pinchos            = (0, 0, 264, 89)


#class Enemigo(pygame.sprite.Sprite):
   
   
    #avance_jugador = 132

    #def __init__(self, sprite_sheet_data):

        #pygame.sprite.Sprite.__init__(self)
        #sprite_sheet = SpriteSheet("imagenes/pinchos.png")
        #self.rect = self.image.get_rect()    


        #self.image.set_colorkey(constantes.BLANCO)

botiquin = (44, 180, 165, 140)
banana = (232, 160, 280, 230)
botella = (510, 200,150,80)
 
"""
class Provision (pygame.sprite.Sprite):
        
     def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("imagenes/Objetoslevel1.png")
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        #self.image = pygame.transform.scale(self.image, (40, 80))
        #self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        
        self.image.set_colorkey(constantes.BLANCO)
"""        
class Provision (pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("imagenes/Objetoslevel1.png")
        # Grab the image for this platform
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect()
        
                