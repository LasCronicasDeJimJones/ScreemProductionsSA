import pygame
import constantes
import menu
from nivel2 import Level_02
from nivel1 import Level_01
from jugador import Player
from pygame.mixer import music
from jugador import Player
from menu import cMenu, EVENT_CHANGE_STATE
from string import center
from funciones_spritesheet import SpriteSheet
from funciones_spritesheet import SpriteSheetNotas
import time

def jugar(pantalla, jugador):
    # Creamos al jugador con la imagen p1_walk.png
    jugador_principal = Player(jugador)

    letraparapuntos=pygame.font.SysFont("comicsans",24)
    #letraTiempo = pygame.font.Font("comicsans", 24)

    # Creamos todos los niveles del juego
    lista_niveles = []
    lista_niveles.append(Level_01(jugador_principal))
    lista_niveles.append(Level_02(jugador_principal))

    # Seteamos cual es el primer nivel.
    numero_del_nivel_actual = 0
    nivel_actual = lista_niveles[numero_del_nivel_actual]

    lista_sprites_activos = pygame.sprite.Group()
    jugador_principal.nivel = nivel_actual

    jugador_principal.rect.x = 340
    jugador_principal.rect.y = constantes.LARGO_PISO - jugador_principal.rect.height
    lista_sprites_activos.add(jugador_principal)
    
    #musica
    nivel_actual.sonido.play(-1)

    #Variable booleano que nos avisa cuando el usuario aprieta el botOn salir.
    salir = False

    clock = pygame.time.Clock()
    
    starting_point = time.time() + 700
    
    # -------- Loop Princiapl -----------
    while not salir:
        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT: 
                salir = True 

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador_principal.retroceder()
                if evento.key == pygame.K_RIGHT:
                    jugador_principal.avanzar()
                if evento.key == pygame.K_UP:
                    jugador_principal.saltar()
                if evento.key == pygame.K_LSHIFT and pygame.K_RIGHT:
                    jugador_principal.turbo = True
                    
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and jugador_principal.mover_x < 0:
                    jugador_principal.parar()
                if evento.key == pygame.K_RIGHT and jugador_principal.mover_x > 0:
                    jugador_principal.parar()
                if evento.key == pygame.K_LSHIFT and pygame.K_LEFT:
                    jugador_principal.turbo = False
                    


        # Actualiza todo el jugador
        lista_sprites_activos.update()


        # Actualiza los elementos del nivel
        nivel_actual.update()


        # Si el jugador se acarca hacia el lado derecho mueve el mundo hacia la izquierda (-x)
        if jugador_principal.rect.x >= 500:
            diff = jugador_principal.rect.x - 500
            jugador_principal.rect.x = 500
            nivel_actual.avance_nivel(-diff)


        # Si el jugador se acarca hacia el lado izquierda mueve el mundo hacia la derecha (-x)
        if jugador_principal.rect.x <= 120:
            diff = 120 - jugador_principal.rect.x
            jugador_principal.rect.x = 120
            nivel_actual.avance_nivel(diff)


        #Si el jugador se mueve hacia el fin del nivel cambia el jugador al siguiente nivel.
        current_position = jugador_principal.rect.x + nivel_actual.posicion_jugador_nivel
        if current_position < nivel_actual.limite_nivel:
            jugador_principal.rect.x = 120
            if numero_del_nivel_actual < len(lista_niveles)-1:
                pygame.mixer.stop()
                numero_del_nivel_actual += 1
                if (numero_del_nivel_actual<=1):
                    nivel_actual = lista_niveles[numero_del_nivel_actual]
                    jugador_principal.nivel = nivel_actual
                    nivel_actual.sonido.play(-1)
                    starting_point = time.time() + 700
            else:
                pantalla.fill(constantes.NEGRO)
                game = pygame.image.load("imagenes/Fin.png").convert()
                pantalla.blit(game,(0,0))
                pygame.display.flip()
                pygame.event.wait()
                main()

        if jugador_principal.vidas <= 0:
            pygame.mixer.stop()
            pantalla.fill(constantes.NEGRO)
            game = pygame.image.load("imagenes/Gameover.png").convert()
            pantalla.blit(game,(0,0))
            #textopuntos=letraparapuntos.render("GAME OVER",0, constantes.BLANCO)
            #pantalla.blit( textopuntos,(100,100))
            pygame.display.flip()
            pygame.event.wait()
            main()
            
        elapsed_time = starting_point - time.time ()
        elapsed_time_int = int(elapsed_time)    
        if elapsed_time <= 0:
            pygame.mixer.stop()
            pantalla.fill(constantes.NEGRO)
            game = pygame.image.load("imagenes/Gameover.png").convert()
            pantalla.blit(game,(0,0))
            #textopuntos=letraparapuntos.render("GAME OVER",0, constantes.BLANCO)
            #pantalla.blit( textopuntos,(100,100))
            pygame.display.flip()
            pygame.event.wait()
            main()


        print "current pos: ",  current_position
                
        # TODO EL CODIGO PARA DIBUJAR DEBE IR DEBAJO DE ESTE COMENTARIO.
        nivel_actual.draw(pantalla)
        lista_sprites_activos.draw(pantalla)

        textopuntos=letraparapuntos.render("Puntos: "+str(jugador_principal.puntos),0, constantes.BLANCO)
        pantalla.blit( textopuntos,(10,10))
        
        textovidas=letraparapuntos.render("Vidas: "+str(jugador_principal.vidas),0, constantes.BLANCO)
        pantalla.blit( textovidas,(10,35))
        
        
        textotiempo = letraparapuntos.render("Tiempo: "+ str(elapsed_time_int), 1, constantes.BLANCO)
        pantalla.blit(textotiempo, (10,60))
        # TODO EL CODIGO PARA DIBUJAR DEBE IR POR ARRIBA DE ESTE COMENTARIO.

        clock.tick(60)

        pygame.display.flip()

    return salir
    
def main():
    """ Clase principal en el que se debe ejecutar el juego. """
    pygame.init()

    # Configuramos el alto y largo de la pantalla
    tamanio = [constantes.ANCHO_PANTALLA, constantes.LARGO_PANTALLA]
    pantalla = pygame.display.set_mode(tamanio)

    pygame.display.set_caption("The Chornicles of Jim Jones")
    
    sprite_sheet = SpriteSheetNotas("imagenes/personajes.png")
    jugador1 = sprite_sheet.get_image(156,0,141,298)
    sprite_sheet = SpriteSheetNotas("imagenes/personajes.png")
    jugador2 = sprite_sheet.get_image(0,0,151,298)
    historia = pygame.image.load("imagenes/1pergamino.png").convert()
    historia2 = pygame.image.load("imagenes/2pergamino.png").convert()
    historia3 = pygame.image.load("imagenes/3pergamino.png").convert()
    historia4 = pygame.image.load("imagenes/4pergamino.png").convert()
    historia5 = pygame.image.load("imagenes/5pergamino.png").convert()
    creditos = pygame.image.load("imagenes/creditos.png").convert()
    logo = pygame.image.load("imagenes/Logo.png").convert()
    logo.set_colorkey(constantes.BLANCO)
    alogo = True
    if alogo == True:
        pantalla.blit(logo,(0,0))
        pygame.display.flip()
        alogo = False
    
    menuJuego = cMenu(350,350,20,5,"vertical",100,pantalla,[("Jugar",1,None),("Historia",2,None),("Creditos",3,None),("Salir",4,None)])
    menuJugador = cMenu(250, 300, 20, 5, "horizontal", 4, pantalla, [("Metalero",5,jugador1),("Rastafari",6,jugador2),("Volver",0,None)])
    historia = cMenu (0,0, 600, 800, 'vertical',5,pantalla,[("Historia",7,historia)])
    historia2 = cMenu (0,0, 600, 800, 'vertical',5,pantalla,[("Historia",8,historia2)])
    historia3 = cMenu (0,0, 600, 800, 'vertical',5,pantalla,[("Historia",9,historia3)])
    historia4 = cMenu (0,0, 600, 800, 'vertical',5,pantalla,[("Historia",10,historia4)])
    historia5 = cMenu (0,0, 600, 800, 'vertical',5,pantalla,[("Historia",11,historia5)])
    creditos = cMenu (0,0, 600, 800, 'vertical',6,pantalla,[("Creditos",12,creditos)])
    
    #Alineamos el menu
       
    
    #"""menuPrueba = cMenu(x, y, h_pad, v_pad, orientation, number, background, buttonList)"""
    #menuJuego.set_center(True, True)
    #menuJuego.set_alignment("center", "center")
    
    estado = 0
    estado_previo = 1 
    
    opcion =  [] 
    jugador = 1
    salir = False
    
    
    while not salir:
        if estado_previo != estado:
            pygame.event.post(pygame.event.Event(menu.EVENT_CHANGE_STATE, key = 0))
            estado_previo = estado
        e = pygame.event.wait()
        
        if e.type == pygame.KEYDOWN or e.type == menu.EVENT_CHANGE_STATE:
            if estado == 0:
                opcion, estado = menuJuego.update(e,estado) 
            elif estado == 1:                
                pantalla.blit(logo,(0,0))
                opcion, estado = menuJugador.update(e, estado)
                pygame.display.flip()

            elif estado == 2:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = historia.update(e, estado)
                pygame.display.flip()

            elif estado == 3:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = creditos.update(e, estado)
                pygame.display.flip()

            elif estado == 5:
                jugar(pantalla, 1)
            elif estado == 6:
                jugar(pantalla, 2)
            elif estado == 7:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = historia2.update(e, estado)
                pygame.display.flip()
            elif estado == 8:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = historia3.update(e, estado)
                pygame.display.flip()
            elif estado == 9:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = historia4.update(e, estado)
                pygame.display.flip()
            elif estado == 10:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = historia5.update(e, estado)
                pygame.display.flip()
            elif estado == 11:
                pantalla.blit(logo,(0,0))
                opcion, estado = menuJuego.update(e,estado)
                pygame.display.flip()
            elif estado == 12:               
                pantalla.blit(logo,(0,0))
                opcion, estado = menuJuego.update(e, estado)
                pygame.display.flip()

            else:
                salir = True
            
        if e.type == pygame.QUIT:
            salir = True
            
        pygame.display.update(opcion)

    pygame.quit()
    
if __name__ == "__main__":
    main()
