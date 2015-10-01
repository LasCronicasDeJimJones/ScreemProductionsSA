import pygame
import constantes
from funciones_spritesheet import SpriteSheet

rama1 = (0, 0, 213, 202)
rama2 = (279, 18, 137, 184)
rama3 = (446, 43,265,139)
 
class Provision (pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("imagenes/Objetoslevel2.png")
        # Grab the image for this platform
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect()