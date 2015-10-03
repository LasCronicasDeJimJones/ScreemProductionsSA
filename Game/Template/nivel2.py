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
        self.limite_nivel = -45442
        
    
        self.sonido = pygame.mixer.Sound("sonido/Bosque.ogg")
        #sonido.play(-1)
        #nivel_puntos = 

        #Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [platforma2.PLATAFORMA10, 500, 450],
                  [platforma2.PLATAFORMA8, 800, 450],
                  [platforma2.PLATAFORMA10, 1200, 400],
                  [platforma2.PLATAFORMA10,1500,400],
                  [platforma2.PLATAFORMA8, 1800,350],
                  [platforma2.PLATAFORMA7, 2200,300],
                  [platforma2.PLATAFORMA10,2900,500],
                  [platforma2.PLATAFORMA8, 3300,500],
                  [platforma2.PLATAFORMA7, 3700,450], 
                  [platforma2.PLATAFORMA9, 4100,500],
                  [platforma2.PLATAFORMA10, 4500,500],
                  [platforma2.PLATAFORMA8, 4900,500],
                  [platforma2.PLATAFORMA8, 5200,400],
                  [platforma2.PLATAFORMA7, 5600,300],
                  [platforma2.PLATAFORMA9, 6000,450],
                  [platforma2.PLATAFORMA10, 6300,450],
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
                  [platforma2.PLATAFORMA7, 13600,500],
                  [platforma2.PLATAFORMA8, 13900,400],
                  [platforma2.PLATAFORMA9, 14300,400],
                  [platforma2.PLATAFORMA10, 14600,300],
                  [platforma2.PLATAFORMA10, 15000,200],
                  [platforma2.PLATAFORMA7, 19000,500],
                  [platforma2.PLATAFORMA9, 19600,400],
                  [platforma2.PLATAFORMA10, 19900,300],
                  [platforma2.PLATAFORMA7, 20200,400],
                  [platforma2.PLATAFORMA9, 20600,300],
                  [platforma2.PLATAFORMA8, 20900,200],
                  [platforma2.PLATAFORMA9, 21200,400],
                  [platforma2.PLATAFORMA9, 21500,500],
                  [platforma2.PLATAFORMA10, 21900,450],
                  [platforma2.PLATAFORMA7, 22200,400],
                  [platforma2.PLATAFORMA7, 22600,300],
                  [platforma2.PLATAFORMA8, 22900,400],
                  [platforma2.PLATAFORMA9, 23200,500],
                  [platforma2.PLATAFORMA10, 23600,400],
                  [platforma2.PLATAFORMA10, 23900,350],
                  [platforma2.PLATAFORMA10, 24300,250],
                  [platforma2.PLATAFORMA10, 24700,350],
                  [platforma2.PLATAFORMA10, 25100,450],
                  [platforma2.PLATAFORMA10, 25500,500],
                  [platforma2.PLATAFORMA10, 25900,500],
                  [platforma2.PLATAFORMA10, 26200,450],
                  [platforma2.PLATAFORMA10, 26500,350],
                  [platforma2.PLATAFORMA10, 26900,350],
                  [platforma2.PLATAFORMA10, 27300,250],
                  [platforma2.PLATAFORMA10, 27600,350],
                  [platforma2.PLATAFORMA10, 28000,450],
                  [platforma2.PLATAFORMA10, 28300,450],
                  [platforma2.PLATAFORMA10, 28700,500],
                  [platforma2.PLATAFORMA10, 29000,500],
                  [platforma2.PLATAFORMA10, 29400,450],
                  [platforma2.PLATAFORMA10, 29800,350],
                  [platforma2.PLATAFORMA10, 30100,250],
                  [platforma2.PLATAFORMA10, 30500,500],
                  [platforma2.PLATAFORMA10, 30800,450],
                  [platforma2.PLATAFORMA10, 31200,500],
                  [platforma2.PLATAFORMA10, 31500,450],
                  [platforma2.PLATAFORMA10, 31900,350],
                  [platforma2.PLATAFORMA10, 32300,450],
                  [platforma2.PLATAFORMA10, 32600,500],
                  [platforma2.PLATAFORMA10, 32900,450],
                  [platforma2.PLATAFORMA10, 33300,350],
                  [platforma2.PLATAFORMA10, 33700,350],
                  [platforma2.PLATAFORMA10, 34000,250],
                  [platforma2.PLATAFORMA10, 34400,350],
                  [platforma2.PLATAFORMA10, 34700,450],
                  [platforma2.PLATAFORMA10, 35000,500],
                  [platforma2.PLATAFORMA10, 35300,450],
                  [platforma2.PLATAFORMA10, 35600,350],
                  [platforma2.PLATAFORMA10, 35900,250],
                  [platforma2.PLATAFORMA10, 36300,350],
                  [platforma2.PLATAFORMA10, 36600,450],
                  [platforma2.PLATAFORMA10, 36900,500],
                  [platforma2.PLATAFORMA10, 37200,450],
                  [platforma2.PLATAFORMA10, 37400,500],
                  [platforma2.PLATAFORMA10, 37600,450],
                  [platforma2.PLATAFORMA10, 37900,400],
                  [platforma2.PLATAFORMA10, 38100,380],
                  [platforma2.PLATAFORMA10, 38600,380],
                  [platforma2.PLATAFORMA10, 38900,400],
                  [platforma2.PLATAFORMA10, 39100,420],
                  [platforma2.PLATAFORMA10, 39500,420],
                  [platforma2.PLATAFORMA10, 40000,500],
                  [platforma2.PLATAFORMA10, 40400,500],
                  [platforma2.PLATAFORMA10, 40800,500],
                  [platforma2.PLATAFORMA10, 41200,480],
                  [platforma2.PLATAFORMA10, 41600,460],
                  [platforma2.PLATAFORMA10, 42100,500],
                  [platforma2.PLATAFORMA10, 42400,450],
                  [platforma2.PLATAFORMA10, 42500,400],
                  [platforma2.PLATAFORMA10, 43000,350],
                  [platforma2.PLATAFORMA10, 43300,300],
                  [platforma2.PLATAFORMA10, 43600,250],
                  [platforma2.PLATAFORMA10, 43900,350],
                  [platforma2.PLATAFORMA10, 44200,400],
                  [platforma2.PLATAFORMA10, 44600,550]]                    
                
        
        
        enemigos = [[PINCHO,3000,545],
                    [PINCHO,1250,545],
                    [PINCHO,1600,545],
                    [PINCHO,3500,545],
                    [PINCHO,4600,545],
                    [PINCHO,5500,545],
                    [PINCHO,6300,545],
                    [PINCHO,7500,545],
                    [PINCHO,9000,545],
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
                    [PINCHO,28900,545],
                    [PINCHO,30000,545],
                    [PINCHO,31500,545],
                    [PINCHO,32000,545],
                    [PINCHO,32600,545],
                    [PINCHO,33000,545],
                    [PINCHO,33500,545],
                    [PINCHO,33500,545],
                    [PINCHO,34000,545],
                    [PINCHO,34500,545],
                    [PINCHO,35000,545],
                    [PINCHO,35500,545],
                    [PINCHO,36000,545],
                    [PINCHO,36500,545],
                    [PINCHO,37000,545],
                    [PINCHO,37500,545],
                    [PINCHO,38000,545],
                    [PINCHO,38500,545],
                    [PINCHO,39000,545],
                    [PINCHO,39500,545],
                    [PINCHO,40000,545],
                    [PINCHO,40500,545],
                    [PINCHO,41000,545],
                    [PINCHO,41500,545],
                    ]
        
        objetos_puntos = [[provisiones2.rama3, 700, 400],
                          [provisiones2.rama2, 2000, 200],
                          [provisiones2.rama1, 3000,300],
                          [provisiones2.rama1, 5050, 300],
                          [provisiones2.rama2, 6000, 400],
                          [provisiones2.rama3, 6500, 200],
                          [provisiones2.rama3, 7000, 300],
                          [provisiones2.rama2, 8050, 300],
                          [provisiones2.rama1, 8800, 200],
                          [provisiones2.rama1, 9500, 200],
                          [provisiones2.rama3, 11000, 200],
                          [provisiones2.rama2, 13000, 200],
                          [provisiones2.rama1, 13500, 300],
                          [provisiones2.rama3, 14000, 200],
                          [provisiones2.rama3, 15000, 100],
                          [provisiones2.rama2, 16500, 300],
                          [provisiones2.rama3, 17000, 400],
                          [provisiones2.rama1, 17500, 300],
                          [provisiones2.rama1, 18300, 300],
                          [provisiones2.rama2, 21000, 200],
                          [provisiones2.rama3, 23000, 300],
                          [provisiones2.rama1, 24000, 200],
                          [provisiones2.rama3, 25500, 300],
                          [provisiones2.rama2, 26700, 200],
                          [provisiones2.rama3, 28000, 200],
                          [provisiones2.rama1, 30000, 200],
                          [provisiones2.rama1, 32000, 300],
                          [provisiones2.rama2, 34000, 200],
                          [provisiones2.rama3, 36000, 400],
                          [provisiones2.rama2, 36500, 200],
                          [provisiones2.rama1, 38000, 300],
                          [provisiones2.rama2, 38200, 200],
                          [provisiones2.rama3, 38500, 400],
                          [provisiones2.rama2, 39000, 300],
                          [provisiones2.rama1, 39300, 300],
                          [provisiones2.rama2, 39600, 320],
                          [provisiones2.rama3, 39900, 400],
                          [provisiones2.rama2, 40000, 300],
                          [provisiones2.rama1, 40400, 300],
                          [provisiones2.rama2, 40800, 200],
                          [provisiones2.rama3, 41200, 400],
                          [provisiones2.rama2, 41600, 200],
                          [provisiones2.rama1, 42000, 300],
                          [provisiones2.rama2, 42500, 200],
                          [provisiones2.rama3, 43000, 400],
                          [provisiones2.rama2, 43500, 200],
                          [provisiones2.rama1, 43800, 300],
                          [provisiones2.rama2, 44000, 200],
                          [provisiones2.rama3, 44200, 3000],
                          [provisiones2.rama2, 44600, 300],                          
                        ]
        #Se busca en la lista anterior creada y se le agregan las plataformas al jugador.
        for plataforma in nivel:
            bloque = platforma2.Plataforma2(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
        
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
        bloque = platforma2.PlataformaConMovimiento2(platforma2.PLATAFORMA10)
        bloque.rect.x = 2500
        bloque.rect.y = 300
        bloque.limite_superior = 100
        bloque.limite_inferior = 550
        bloque.mover_y = -1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)