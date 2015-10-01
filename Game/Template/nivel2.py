import pygame
import constantes
import provisiones2
import platforma
import platforma2
from nivel import Level
from enemigos import Pincho,PINCHO,PINCHO2,PINCHO3,PINCHO4
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
        self.limite_nivel = -40095
        
    
        self.sonido = pygame.mixer.Sound("sonido/Bosque.ogg")
        #sonido.play(-1)
        #nivel_puntos = 

        #Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [platforma2.PLATAFORMA10, 500, 550],
                  [platforma2.PLATAFORMA7, 640, 550],
                  [platforma2.PLATAFORMA8, 800, 550],
                  [platforma2.PLATAFORMA9, 940, 400],
                  [platforma2.PLATAFORMA10, 1200,600]]
        
        
        enemigos = [[PINCHO,3000,545],
                    [PINCHO,1250,545],
                    [PINCHO,1600,545],
                    [PINCHO,3500,545],
                    [PINCHO,4600,545],
                    [PINCHO,5500,545],
                    [PINCHO,6300,545],
                    [PINCHO,7500,545],
                    [PINCHO,9000,545],
                    [PINCHO,9700,545],
                    [PINCHO,10100,545],
                    [PINCHO,12000,545],
                    [PINCHO,14500,545],
                    [PINCHO,15000,545],
                    [PINCHO,16000,545],
                    [PINCHO,17500,545],
                    [PINCHO,18000,545],
                    [PINCHO,19600,545],
                    [PINCHO,22000,545],
                    [PINCHO,22200,545],
                    [PINCHO,22500,545],
                    [PINCHO,22800,545],
                    [PINCHO,23100,545],
                    [PINCHO,23500,545],
                    [PINCHO,23900,545],
                    [PINCHO,24300,545],
                    [PINCHO,24600,545],
                    [PINCHO,24900,545],
                    [PINCHO,25400,545],
                    [PINCHO,25800,545],
                    [PINCHO,26100,545],
                    [PINCHO,27000,545],
                    [PINCHO,27300,545],
                    [PINCHO,27600,545],
                    [PINCHO,27900,545],
                    [PINCHO,28300,545],
                    [PINCHO,28600,545],
                    [PINCHO,28900,545]
                    ]
        
        objetos_puntos = [[provisiones2.rama1, 500, 100],
                          [provisiones2.rama2, 500, 75],
                          [provisiones2.rama3, 500, 50],
                        ]
        #Se busca en la lista anterior creada y se le agregan las plataformas al jugador.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
        
        #for plataforma2 in nivel:
         #   bloque = platforma.Plataforma(plataforma[0])
          #  bloque.rect.x = plataforma2[1]
           # bloque.rect.y = plataforma2[2]
            #bloque.jugador = self.jugador
            #self.lista_plataformas.add(bloque)
        
        for enemigo in enemigos:            
            un_enemigo = Pincho(enemigo[0])
            un_enemigo.rect.x = enemigo[1]
            un_enemigo.rect.y = enemigo[2]
            self.lista_enemigos.add(un_enemigo) 
        
        for objeto_punto in objetos_puntos:            
            punto = provisiones2.Provision(objeto_punto[0])
            punto.rect.x = objeto_punto[1]
            punto.rect.y = objeto_punto[2]
            self.lista_de_cosas_con_puntitos.add(punto)

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