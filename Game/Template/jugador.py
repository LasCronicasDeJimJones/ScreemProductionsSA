import pygame   
import constantes
from platforma import PlataformaConMovimiento
from funciones_spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    """Clase utilizada para desarrollar los jugadores del juego. """
    
    # -- Atributos
    mover_x = 0
    mover_y = 0

    # tecla shift
    turbo = False
    
    # Estas listas definen todas las imagenes de nuestro jugador.
    jugador_frame_izq = []
    jugador_frame_der = []

    # Direccion en la que va el jugador.
    direccion = "R"

    # Lista de sprite con las cosas que nos podemos chocar.
    nivel = None
    
    puntos = 0
    
    vidas = 3
    
    # -- Metodos
    def __init__(self,rol):
        """ __Funcion constructor__ 
            Aca en donde se debe cargar el sprite sheet del jugador.
            Se debe cargar los sprite con movimiento hacia la izquierda y hacia la derecha.
        """

        pygame.sprite.Sprite.__init__(self)
        if rol==1:
            sprite_sheet = SpriteSheet("imagenes/spritesdimensiones.png") 
           
            # Carga de todos los sprite de la imagen hacia la derecha.
            imagen = sprite_sheet.obtener_imagen(600,180 ,120 , 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(480, 180 , 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(360, 180, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(240, 180, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(120, 180, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 180, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(600, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(480, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(360, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(240, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(120, 0, 120, 180)
            self.jugador_frame_der.append(imagen)      
            imagen = sprite_sheet.obtener_imagen(0, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            # # Carga de todos los sprite de la imagen hacia la derecha y la rotamos.        
            imagen = sprite_sheet.obtener_imagen(600, 180, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(480,180, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(360,180 ,120 , 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(240, 180 , 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(120, 180, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 180, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(600, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(480, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(360, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(240, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(120, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)     
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            
        else:

            sprite_sheet = SpriteSheet("imagenes/Spritesheet2.png") 
           
            # Carga de todos los sprite de la imagen hacia la derecha.
            imagen = sprite_sheet.obtener_imagen(600,180 ,120 , 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(480, 180 , 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(360, 180, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(240, 180, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(120, 180, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 180, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(600, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(480, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(360, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(240, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(120, 0, 120, 180)
            self.jugador_frame_der.append(imagen)      
            imagen = sprite_sheet.obtener_imagen(0, 0, 120, 180)
            self.jugador_frame_der.append(imagen)
            # # Carga de todos los sprite de la imagen hacia la derecha y la rotamos.        
            imagen = sprite_sheet.obtener_imagen(600, 180, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(480,180, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(360,180 ,120 , 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(240, 180 , 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(120, 180, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 180, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(600, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(480, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(360, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(240, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(120, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)     
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 0, 120, 180)
            imagen = pygame.transform.flip(imagen, True, False)
            self.jugador_frame_izq.append(imagen)
        # Seteamos con que sprite comenzar
        self.image = self.jugador_frame_der[0]


        self.rect = self.image.get_rect()


    def update(self):
        """ Metodo que actualiza la posicion del jugador. """
        
        # Gravedad
        self.calc_grav()

        # Movimientos Izquierda/Derecha
        # no es turbo
        if self.turbo == False:
            self.rect.x += self.mover_x
            pos = self.rect.x + self.nivel.posicion_jugador_nivel
            if self.direccion == "R":
                frame = (pos // 30) % len(self.jugador_frame_der)
                self.image = self.jugador_frame_der[frame]
            else:
                frame = (pos // 30) % len(self.jugador_frame_izq)
                self.image = self.jugador_frame_izq[frame]
        # turbo
        else:
            self.rect.x += self.mover_x
            pos = self.rect.x + self.nivel.posicion_jugador_nivel
            if self.direccion == "R":
                frame = (pos // 15) % len(self.jugador_frame_der)
                self.image = self.jugador_frame_der[frame]
            else:
                frame = (pos // 15) % len(self.jugador_frame_izq)
                self.image = self.jugador_frame_izq[frame]
            

        # Verficiamos si colisionamos con algo mientras avanzamos
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.lista_plataformas, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_x > 0:
                self.rect.right = block.rect.left
            elif self.mover_x < 0:
                self.rect.left = block.rect.right
                
        # Verficamos si colisionamos con algo mientras avanzamos
        lista_de_colision_puntos = pygame.sprite.spritecollide(self, self.nivel.lista_de_cosas_con_puntitos, False)
        for objeto_punto in lista_de_colision_puntos:
            #sumar puntos al jugador
            self.puntos = self.puntos + 10
            objeto_punto.kill() 

        #verificamos si chocamos con enemigos        
        lista_de_colision_enemigo = pygame.sprite.spritecollide(self, self.nivel.lista_enemigos, False)
        for objeto_enemigo in lista_de_colision_enemigo:
            print "CHOQUE : ",self.nivel.posicion_jugador_nivel
            
            
            self.rect.x = pos 
            
        
            #self.rect.x = pos
            #self.rect.y = constantes.LARGO_PISO - self.rect.height
            
            #self.rect.x = pos
            self.vidas -= 1

        self.rect.y += self.mover_y

        # Verficiamos si colisionamos con algo si saltamos
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.lista_plataformas, False)
        for block in lista_de_bloques_colisionados:

            if self.mover_y > 0:
                self.rect.bottom = block.rect.top
            elif self.mover_y < 0:
                self.rect.top = block.rect.bottom

            self.mover_y = 0

            if isinstance(block, PlataformaConMovimiento):
                self.rect.x += block.mover_x
            
                
        
        
        
            

    def calc_grav(self):
        """ Calcula el efecto de la gravedad. """
        
        if self.mover_y == 0:
            self.mover_y = 1
        else:
            self.mover_y += .30

        # Verificamos si estamos en el suelo.
        if self.rect.y >= constantes.LARGO_PISO - self.rect.height and self.mover_y >= 0:
            self.mover_y = 0
            self.rect.y = constantes.LARGO_PISO - self.rect.height

    def saltar(self):
        """ Metodo que se llamam si saltamos. """

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.nivel.lista_plataformas, False)
        self.rect.y -= 2
        sonidosalto = pygame.mixer.Sound("sonido/Sonidosalto.ogg")
        sonidosalto.play()

        if len(platform_hit_list) > 0 or self.rect.bottom >= constantes.LARGO_PISO:
            self.mover_y = -10

    def retroceder(self):
        """ Se llama cuando movemos hacia la izq. """
        # no es turbo
        if self.turbo == False:
            self.mover_x = -6
            self.direccion = "L"
        else:
            self.mover_x = -8
            self.direccion= "L"
    def avanzar(self):
        """ Se llama cuando movemos hacia la der. """
        # no es turbo
        if self.turbo == False:
            self.mover_x = 6
        else:
            self.mover_x = 8
        self.direccion = "R"

    def parar(self):
        """ Se llama cuando soltamos la tecla. """
        self.mover_x = 0
