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
        nivel = [ [platforma.PLATAFORMA1, 500, 500],
                  [platforma.PLATAFORMA2, 600, 400],
                  [platforma.PLATAFORMA3, 650, 300],
                  [platforma.PLATAFORMA4, 1045, 300],
                  [platforma.PLATAFORMA5, 1600, 300],
                  [platforma.PLATAFORMA6, 1900, 300],
                  [platforma.PLATAFORMA6, 2300, 500],
                  [platforma.PLATAFORMA6, 2550, 400],
                  [platforma.PLATAFORMA6, 2700, 300],
                  [platforma.PLATAFORMA6, 2950, 400],
                  [platforma.PLATAFORMA6, 3300, 400],
                  [platforma.PLATAFORMA6, 3650, 300],
                  [platforma.PLATAFORMA6, 3900, 200],
                  [platforma.PLATAFORMA6, 4300, 300],
                  [platforma.PLATAFORMA6, 4800, 300],
                  [platforma.PLATAFORMA6, 5300, 500],
                  [platforma.PLATAFORMA6, 5800, 400],
                  [platforma.PLATAFORMA6, 7200, 300],
                  [platforma.PLATAFORMA6, 7500, 200],
                  [platforma.PLATAFORMA6, 7900, 200],
                  [platforma.PLATAFORMA6, 8800, 300],
                  [platforma.PLATAFORMA6, 9200, 200],
                  [platforma.PLATAFORMA6, 9500, 500],
                  [platforma.PLATAFORMA6, 9900, 400],
                  [platforma.PLATAFORMA6, 10200, 300],
                  [platforma.PLATAFORMA6, 10500, 200],
                  [platforma.PLATAFORMA6, 10700, 300],
                  [platforma.PLATAFORMA6, 11000, 400],
                  [platforma.PLATAFORMA6, 11300, 500],
                  [platforma.PLATAFORMA6, 11500, 400],
                  [platforma.PLATAFORMA6, 11800, 400],
                  [platforma.PLATAFORMA6, 12000, 300],
                  [platforma.PLATAFORMA6, 12800, 200],
                  [platforma.PLATAFORMA6, 13100, 100],
                  [platforma.PLATAFORMA6, 13400, 200],
                  [platforma.PLATAFORMA6, 13800, 300],
                  [platforma.PLATAFORMA6, 14100, 300],
                  [platforma.PLATAFORMA6, 14400, 400],
                  [platforma.PLATAFORMA6, 14800, 500],
                  [platforma.PLATAFORMA6, 15100, 400],
                  [platforma.PLATAFORMA6, 15400, 400],
                  [platforma.PLATAFORMA6, 16500, 500],
                  [platforma.PLATAFORMA6, 16800, 600],
                  [platforma.PLATAFORMA6, 17100, 600],
                  [platforma.PLATAFORMA6, 17400, 500],
                  [platforma.PLATAFORMA6, 17700, 400],
                  [platforma.PLATAFORMA6, 18000, 300],
                  [platforma.PLATAFORMA6, 18300, 300],
                  [platforma.PLATAFORMA6, 18600, 300],
                  [platforma.PLATAFORMA6, 18900, 200],
                  [platforma.PLATAFORMA6, 19300, 300],
                  [platforma.PLATAFORMA6, 20400, 400],
                  [platforma.PLATAFORMA6, 20700, 500],
                  [platforma.PLATAFORMA6, 21300, 500],
                  [platforma.PLATAFORMA6, 21600, 400],
                  [platforma.PLATAFORMA6, 21900, 400],
                  [platforma.PLATAFORMA6, 22200, 300],
                  [platforma.PLATAFORMA6, 22500, 200],
                  [platforma.PLATAFORMA6, 22800, 100],
                  [platforma.PLATAFORMA6, 23100, 100],
                  [platforma.PLATAFORMA6, 23300, 400],
                  [platforma.PLATAFORMA6, 23600, 500],
                  [platforma.PLATAFORMA6, 23900, 600],
                  [platforma.PLATAFORMA6, 24300, 500],
                  [platforma.PLATAFORMA6, 24600, 400],
                  [platforma.PLATAFORMA6, 24900, 400],
                  [platforma.PLATAFORMA6, 25300, 300],
                  [platforma.PLATAFORMA6, 25600, 200],
                  [platforma.PLATAFORMA6, 25900, 100],
                  [platforma.PLATAFORMA6, 26800, 200],
                  [platforma.PLATAFORMA6, 27100, 300],
                  [platforma.PLATAFORMA6, 27400, 300],
                  [platforma.PLATAFORMA6, 27700, 400],
                  [platforma.PLATAFORMA6, 28000, 400],
                  [platforma.PLATAFORMA6, 28300, 500],
                  [platforma.PLATAFORMA6, 28600, 600],
                  [platforma.PLATAFORMA6, 28900, 500],
                  [platforma.PLATAFORMA6, 29200, 500],
                  [platforma.PLATAFORMA6, 29500, 400],
                  [platforma.PLATAFORMA6, 30400, 400],
                  [platforma.PLATAFORMA6, 30700, 500],
                  [platforma.PLATAFORMA6, 31000, 400],
                  [platforma.PLATAFORMA6, 31300, 300],
                  [platforma.PLATAFORMA6, 31600, 300],
                  [platforma.PLATAFORMA6, 31900, 200],
                  [platforma.PLATAFORMA6, 32200, 200],
                  [platforma.PLATAFORMA6, 32500, 300],
                  [platforma.PLATAFORMA6, 32800, 400],
                  
                  
                ]

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
        """
        puntos = platforma.PlataformaConMovimiento(platforma.PLATAFORMA2 )
        puntos.rect.x = 350
        puntos.rect.y = 280
        puntos.limite_izquierdo = 350
        puntos.limite_derecho = 1000
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_de_cosas_con_puntitos.add(puntos)
        """

        # Se agrega una plataforma en movimiento.
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA3)
        bloque.rect.x = 1350
        bloque.rect.y = 300
        bloque.limite_izquierdo = 1350
        bloque.limite_derecho = 1600
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA6)
        bloque.rect.x = 6200
        bloque.rect.y = 400
        bloque.limite_izquierdo = 6200
        bloque.limite_derecho = 6500
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA6)
        bloque.rect.x = 6700
        bloque.rect.y = 400
        bloque.limite_izquierdo = 6700
        bloque.limite_derecho = 7400
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA6)
        bloque.rect.x = 8200
        bloque.rect.y = 300
        bloque.limite_izquierdo = 8200
        bloque.limite_derecho = 8500
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA6)
        bloque.rect.x = 12300
        bloque.rect.y = 300
        bloque.limite_izquierdo = 12300
        bloque.limite_derecho = 12600
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA6)
        bloque.rect.x = 13400
        bloque.rect.y = 100
        bloque.limite_izquierdo = 13400
        bloque.limite_derecho = 13700
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA6)
        bloque.rect.x = 15800
        bloque.rect.y = 300
        bloque.limite_izquierdo = 15800
        bloque.limite_derecho = 16200
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA6)
        bloque.rect.x = 19800
        bloque.rect.y = 300
        bloque.limite_izquierdo = 19800
        bloque.limite_derecho = 20100
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA6)
        bloque.rect.x = 19800
        bloque.rect.y = 300
        bloque.limite_izquierdo = 19800
        bloque.limite_derecho = 20100
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        bloque = platforma.PlataformaConMovimiento(platforma.PLATAFORMA6)
        bloque.rect.x = 29800
        bloque.rect.y = 400
        bloque.limite_izquierdo = 29800
        bloque.limite_derecho = 30100
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
                
        
        
        
        