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
                  [platforma2.PLATAFORMA10, 1200,550],
                  [platforma2.PLATAFORMA8, 1900,300],
                  [platforma2.PLATAFORMA7, 2200,200],
                  [platforma2.PLATAFORMA10, 2900,300],
                  [platforma2.PLATAFORMA8, 3300,400],
                  [platforma2.PLATAFORMA7, 3700,500],
                  [platforma2.PLATAFORMA9, 4100,600],
                  [platforma2.PLATAFORMA10, 4500,500],
                  [platforma2.PLATAFORMA8, 4900,500],
                  [platforma2.PLATAFORMA8, 5200,400],
                  [platforma2.PLATAFORMA7, 5600,300],
                  [platforma2.PLATAFORMA9, 6000,450],
                  [platforma2.PLATAFORMA10, 6300,550],
                  [platforma2.PLATAFORMA7, 6700,600],
                  [platforma2.PLATAFORMA7, 7000,600],
                  [platforma2.PLATAFORMA8, 7400,500],
                  [platforma2.PLATAFORMA9, 7800,400],
                  [platforma2.PLATAFORMA8, 8200,300],
                  [platforma2.PLATAFORMA10, 8600,400],
                  [platforma2.PLATAFORMA9, 9000,400],
                  [platforma2.PLATAFORMA8, 9300,400],
                  [platforma2.PLATAFORMA7, 9600,500],
                  [platforma2.PLATAFORMA10, 9900,600],
                  [platforma2.PLATAFORMA8, 10200,500],
                  [platforma2.PLATAFORMA7, 10600,400],
                  [platforma2.PLATAFORMA7, 10900,300],
                  [platforma2.PLATAFORMA10, 11200,200],
                  [platforma2.PLATAFORMA9, 11500,300],
                  [platforma2.PLATAFORMA8, 11800,300],
                  [platforma2.PLATAFORMA7, 12200,400],
                  [platforma2.PLATAFORMA9, 12500,500],
                  [platforma2.PLATAFORMA10, 12900,500],
                  [platforma2.PLATAFORMA7, 13300,600],
                  [platforma2.PLATAFORMA7, 13600,500],
                  [platforma2.PLATAFORMA8, 13900,400],
                  [platforma2.PLATAFORMA9, 14300,400],
                  [platforma2.PLATAFORMA10, 14600,300],
                  [platforma2.PLATAFORMA10, 15000,200],
                  [platforma2.PLATAFORMA7, 19000,600],
                  [platforma2.PLATAFORMA8, 19300,500],
                  [platforma2.PLATAFORMA9, 19600,400],
                  [platforma2.PLATAFORMA10, 19900,300],
                  [platforma2.PLATAFORMA7, 20200,400],
                  [platforma2.PLATAFORMA9, 20600,300],
                  [platforma2.PLATAFORMA8, 20900,200],
                  [platforma2.PLATAFORMA9, 21200,400],
                  [platforma2.PLATAFORMA9, 21500,500],
                  [platforma2.PLATAFORMA10, 21900,550],
                  [platforma2.PLATAFORMA7, 22200,400],
                  [platforma2.PLATAFORMA7, 22600,300],
                  [platforma2.PLATAFORMA8, 22900,400],
                  [platforma2.PLATAFORMA9, 23200,500],
                  [platforma2.PLATAFORMA10, 23600,550],
               
                ]
        
        
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
                          [provisiones2.rama3, 700, 400],
                          [provisiones2.rama2, 2000, 400],
                          [provisiones2.rama1, 3000,300],
                          [provisiones2.rama1, 5050, 300],
                          [provisiones2.rama2, 6000, 400],
                          [provisiones2.rama3, 6500, 500],
                          [provisiones2.rama3, 7000, 300],
                          [provisiones2.rama2, 8050, 300],
                          [provisiones2.rama1, 8800, 400],
                          [provisiones2.rama1, 9500, 500],
                          [provisiones2.rama3, 11000, 300],
                          [provisiones2.rama2, 13000, 200],
                          [provisiones2.rama1, 13500, 300],
                          [provisiones2.rama3, 14000, 400],
                          [provisiones2.rama3, 15000, 500],
                          [provisiones2.rama2, 16500, 300],
                          [provisiones2.rama3, 17000, 400],
                          [provisiones2.rama1, 17500, 300],
                          [provisiones2.rama1, 18300, 300],
                          [provisiones2.rama2, 21000, 400],
                          [provisiones2.rama3, 23000, 300],
                          [provisiones2.rama1, 24000, 200],
                          [provisiones2.rama3, 25500, 300],
                          [provisiones2.rama2, 26700, 400],
                          [provisiones2.rama3, 28000, 500],
                          [provisiones2.rama1, 30000, 400],
                          [provisiones2.rama1, 32000, 300],
                          [provisiones2.rama2, 34000, 400],
                          [provisiones2.rama3, 36000, 400],
                          [provisiones2.rama2, 36500, 500],
                          [provisiones2.rama1, 38000, 300],
                          
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