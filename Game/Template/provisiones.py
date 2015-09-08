import pygame
import constantes



#from funciones_spritesheet import SpriteSheet


class Provisiones (pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
       

        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheet("imagenes/botellasprite.jpg.png")
        
        # Grab the image for this platform
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()