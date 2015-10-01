import pygame
import constantes
import platforma
import provisiones
from nivel import Level
from enemigos import Pincho,PINCHO,PINCHO2,PINCHO3,PINCHO4


#from Template.puntos import puntos

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
        
        self.sonido = pygame.mixer.Sound("sonido/Playafinal.ogg")
        #sonido.play(-1)
        #nivel_puntos = 

        
         
        objetos_puntos = [[provisiones.botiquin, 500, 100],
                          [provisiones.banana, 500, 300],
                          [provisiones.botella, 500, 200],
                          [provisiones.botiquin, 700, 200], 
                          [provisiones.banana, 1100, 200],
                          [provisiones.botella, 1900, 200],
                          [provisiones.botiquin, 2700, 200],
                          [provisiones.banana, 4000, 100],
                          [provisiones.botiquin, 4900, 100],
                          [provisiones.botella, 6000, 300],
                          [provisiones.banana, 7000, 90],
                          [provisiones.botiquin, 8050, 500],#Easteregg
                          [provisiones.botella, 9000, 300],
                          [provisiones.banana, 10000, 100],
                          [provisiones.botiquin, 11000, 90],
                          [provisiones.botella, 12000, 600],
                          [provisiones.banana, 13050, 300],
                          [provisiones.botella, 14000, 200],
                          [provisiones.botiquin, 15000, 400],
                          [provisiones.banana, 16500, 300],
                          [provisiones.botiquin, 17500, 200],
                          [provisiones.botella, 18500, 300],
                          [provisiones.banana, 20000, 400],
                          [provisiones.botiquin, 21000, 300],
                          [provisiones.botella, 22000, 200],
                          [provisiones.botella, 24500, 200],
                          [provisiones.botiquin, 25000, 90],
                          [provisiones.banana, 26000, 400],
                          [provisiones.botiquin, 27000, 300],
                          [provisiones.botiquin, 28000, 200],
                          [provisiones.botiquin, 29000, 400],
                          [provisiones.botiquin, 30000, 200],
                        ]
                 
                 
        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel =   [[platforma.PLATAFORMA6, 600, 400],
                  [platforma.PLATAFORMA6, 650, 300],
                  [platforma.PLATAFORMA6, 1045, 300],
                  [platforma.PLATAFORMA6, 1600, 300],
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
                  [platforma.PLATAFORMA6, 27000, 200],
                  [platforma.PLATAFORMA6, 26500, 300]]
        #Enemigos
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
                    [PINCHO,28900,545],
                    
                    
                    ]

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
            
        for objeto_punto in objetos_puntos:            
            punto = provisiones.Provision(objeto_punto[0])
            punto.rect.x = objeto_punto[1]
            punto.rect.y = objeto_punto[2]
            self.lista_de_cosas_con_puntitos.add(punto)    
            
        for enemigo in enemigos:            
            un_enemigo = Pincho(enemigo[0])
            un_enemigo.rect.x = enemigo[1]
            un_enemigo.rect.y = enemigo[2]
            self.lista_enemigos.add(un_enemigo)    
         

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
        
                
        
        
        
        