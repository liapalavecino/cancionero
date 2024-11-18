import pygame
from pygame.locals import *
from configuracion import *
from funcionesVACIAS import*

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda, prueba):

    tittleFont= pygame.font.Font('fuente/ka1.ttf', TAMANNO_LETRA)
    defaultFont= pygame.font.Font('fuente/Pixeland.ttf', TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font('fuente/VT323.ttf', TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (440, 550))
    #muestra el puntaje
    screen.blit(defaultFont.render("PUNTOS: " + str(puntos), 1, COLOR_TEXTO), (1000, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("TIEMPO: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("TIEMPO: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (50, 10))

    #muestra el nombre
    screen.blit(tittleFont.render(ayuda, 1, COLOR_PELI), (ANCHO//2-(len(ayuda)*TAMANNO_LETRA//2.5),(TAMANNO_LETRA*2)))

    #muestra las 2 lineas
    screen.blit(defaultFontGrande.render(lista[0], 1, COLOR_LETRAS), (ANCHO//2-len(lista[0])*TAMANNO_LETRA_GRANDE//5,(TAMANNO_LETRA_GRANDE)*6))
    screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//5,(TAMANNO_LETRA_GRANDE)*8))

    #Se cargan burlas para mostrar en caso de incorrecto

    #prueba = draw_text(screen, str(burla), 30, ANCHO // 2, 400) # función para dibujar y burlar
    screen.blit(defaultFont.render(str(prueba), 1, COLOR_BLANCO), (ANCHO//1.9-len(prueba)*TAMANNO_LETRA//4,400))


def gameOver(screen,puntos):

    fondo = pygame.image.load("imagenes/fondo.jpg").convert()
    screen.blit(fondo,(0,0))

    Game_over_font= pygame.font.Font('fuente/gameover.ttf',50)
    Game_over_font_mediana= pygame.font.Font('fuente/gameover.ttf',30)
    FontCredito_chico= pygame.font.Font('fuente/gameover.ttf',20)
    TAMANNO_CREDITO_CHICO = 20

    mensaje1=pygame.image.load("imagenes/gameover.png")
    mensaje2="Puntaje: "+ str(puntos)
    mensaje3 = 'Presione "Tecla ENTER..." o en la X para volver'

    screen.blit(mensaje1, (435,100))
    screen.blit(Game_over_font.render(mensaje2,1,(255,255,255)),(ANCHO//2-9*TAMANNO_LETRA_GRANDE//2,300))
    screen.blit(FontCredito_chico.render(mensaje3,1,(255,255,255)),(ANCHO//2-(len(mensaje3)*TAMANNO_CREDITO_CHICO//4),500))


