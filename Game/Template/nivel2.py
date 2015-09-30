import pygame
import constantes
import platforma
from nivel import Level

#Clase que define el segundo nivel.

class Level_02(Level):
    ''' Clase que define el primer nivel.
    Se debe definir el fondo, las plataformas y los enemigos que aparezcan.'''

    def __init__(self, jugador):
        """ Metodo que crea el nivel 2 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)
        
        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/Fondolevel2.png").convert()
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -10000

        #Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [platforma.PLATAFORMA6, 500, 550],
                 [platforma.PLATAFORMA6, 570, 550],
                  [platforma.PLATAFORMA6, 640, 550],
                  [platforma.PLATAFORMA6, 800, 400],
                  [platforma.PLATAFORMA6, 870, 400],
                  [platforma.PLATAFORMA6, 940, 400],
                  [platforma.PLATAFORMA6, 1000, 500]]
        
        #Se busca en la lista anterior creada y se le agregan las plataformas al jugador.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)

        # Se agrega una plataforma en movimiento.
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA3)
        bloque.rect.x = 1500
        bloque.rect.y = 300
        bloque.limite_superior = 100
        bloque.limite_inferior = 550
        bloque.mover_y = -1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)