import pygame
import constantes
import platforma
from nivel import Level

class Level_01(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)

        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/Fondolevel1.png").convert()
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -33095
        
        sonido = pygame.mixer.Sound("sonido/Playa.ogg")
        sonido.play()
        

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [platforma.GRASS_LEFT, 500, 500],
                  [platforma.GRASS_LEFT, 600, 400],
                  [platforma.GRASS_LEFT, 650, 300],
                  [platforma.GRASS_LEFT, 1045, 300],
                  [platforma.GRASS_LEFT, 1600, 300],
                  [platforma.GRASS_LEFT, 1900, 300],
                  [platforma.GRASS_LEFT, 2050, 400],
                  [platforma.GRASS_LEFT, 2300, 500],
                  ]

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)

        puntos = platforma.PlataformaConMovimiento(platforma.GRASS_LEFT )
        puntos.rect.x = 350
        puntos.rect.y = 280
        puntos.limite_izquierdo = 350
        puntos.limite_derecho = 1000
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_de_cosas_con_puntitos.add(puntos)

        # Se agrega una plataforma en movimiento.
        bloque = platforma.PlataformaConMovimiento(platforma.GRASS_LEFT)
        bloque.rect.x = 1350
        bloque.rect.y = 300
        bloque.limite_izquierdo = 1350
        bloque.limite_derecho = 1600
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)