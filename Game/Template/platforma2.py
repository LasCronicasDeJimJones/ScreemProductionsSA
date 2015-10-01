import pygame
import constantes

from funciones_spritesheet import SpriteSheet

# Estas contantes definen el tipo de plataforma.
#   Nombre del archivo.
#   Posicion X del sprite
#   Posicion Y del sprite
#   Ancho del sprite
#   Alto del sprite

PLATAFORMA7           = (0, 7, 156, 54)
PLATAFORMA8           = (175, 0, 239, 61)
PLATAFORMA9           = (445, 0, 220, 61)
PLATAFORMA10          = (688, 0, 231, 61)

class Plataforma2(pygame.sprite.Sprite):
    """ Clase que define las caracteristicas de la plataforma del juego. """

    def __init__(self, sprite_sheet_data):
        """ Plataforma constructor."""
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheet("imagenes/platformalevel2.png")
        # Grab the image for this platform
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
        
    """
    def update(self):
        Metodo que actualiza la posicion de la plataforma
            Si el jugador esta en el camino, mueve al jugador con la plataforma.    

        # Movimiento izquierda/derecha
        self.rect.x += self.mover_x

        # Se verifica si la plataforma colisiona con el jugador
        hit = pygame.sprite.collide_rect(self, self.jugador)
        if hit:
            # Si entramos es porque la plataforma colisiono con el jugador.

            # Si nos movemos hacia la derecha dejamos la plataforma a la derecha del jugador lo mismo si nos movemos a la izquierda
            if self.mover_x < 0:
                self.jugador.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.jugador.rect.left = self.rect.right

        # Movimiento sube/baja
        self.rect.y += self.mover_y

        # Verificamos si chocamos con el jugador.
        hit = pygame.sprite.collide_rect(self, self.jugador)
        if hit:
            if self.mover_y < 0:
                self.jugador.rect.bottom = self.rect.top
            else:
                self.jugador.rect.top = self.rect.bottom

        # Verificamos los limietes definidos en la plataforma y vemos si tenemos que pegar la vuelta.

        if self.rect.bottom > self.limite_inferior or self.rect.top < self.limite_superior:
            self.mover_y *= -1

        cur_pos = self.rect.x - self.nivel.posicion_jugador_nivel
        if cur_pos < self.limite_izquierdo or cur_pos > self.limite_derecho:
            self.mover_x *= -1
        """