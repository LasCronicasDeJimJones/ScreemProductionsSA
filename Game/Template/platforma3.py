import pygame
import constantes

from funciones_spritesheet import SpriteSheet

BLOQUE = (0,0,10,600)

class Plataforma3(pygame.sprite.Sprite):
    """ Clase que define las caracteristicas de la plataforma del juego. """

    def __init__(self, sprite_sheet_data):
        """ Plataforma constructor."""
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheet("imagenes/bloque_blanco.png")
        # Grab the image for this platform
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
