import pygame

import constantes

class Level():
    """ Super-Clase generica usada para definir los niveles del juego. 
        Se debe crear una clase hija para cada nivel."""

    # Lista de todos los sprites utilizados en todos los niveles.  
    lista_plataformas = None
    lista_enemigos = None
    lista_de_cosas_con_puntitos = None
    # Imagen de fondo
    fondo = None

    sonido = None
    
    # Valor numerico de que tan lejos avanzo nuestro jugador en el nivel
    posicion_jugador_nivel = 0
    limite_nivel = -33095
    #limite_izquierdo = 0

    def __init__(self, jugador):
        """ Constructor. Se le debe pasar al jugador para saber sobre que nivel esta. """
        self.lista_plataformas = pygame.sprite.Group()
        self.lista_enemigos = pygame.sprite.Group()
        self.lista_de_cosas_con_puntitos = pygame.sprite.Group()
        self.jugador = jugador


    def update(self):
        """ Actualizar todo sobre el nivel """
        self.lista_plataformas.update()
        self.lista_enemigos.update()
        self.lista_de_cosas_con_puntitos.update()

    def draw(self, pantalla):
        """ Dibujamos todo sobre el nivel. """

        # Se debe dibujar el fondo.
        pantalla.fill(constantes.BLANCO)
        pantalla.blit(self.fondo,(self.posicion_jugador_nivel // 3,0))

        # Se dibujan todos los sprite que se cargaron.
        self.lista_plataformas.draw(pantalla)
        self.lista_enemigos.draw(pantalla)
        self.lista_de_cosas_con_puntitos.draw(pantalla)
         
         

    def avance_nivel(self, avance_x):
        """ Cuando el usuario se mueve de izquierda/derecha se debe mover el nivel """

        self.posicion_jugador_nivel += avance_x

        for plataforma in self.lista_plataformas:
            plataforma.rect.x += avance_x
        
        for enemigo in self.lista_enemigos:
            enemigo.rect.x += avance_x
            
        for puntos in self.lista_de_cosas_con_puntitos:
            puntos.rect.x+= avance_x    