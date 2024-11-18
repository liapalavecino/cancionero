#! /usr/bin/env python
import os, random, sys, math

import pygame, sys
from pygame.locals import *
from configuracion import *
from extras import *
from menu import *
from funcionesVACIAS import *

#Funcion principal
def comenzar_nuevo_juego():

        pygame.mixer.music.stop()
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Cancionero...")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        #definimos funciones

        #Le asigno a la variable "N" la cantidad de archivos en el directorio de letras
        directory = 'letras'
        N = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        tiempoMenu =  pygame.time.get_ticks()/1000
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        artistaYcancion=[]
        puntos = 0
        palabraUsuario = ""
        letra=[]
        correctas=0
        elegidos= []
        masDeUnaVuelta = False
        sonido_correcto = pygame.mixer.Sound("sonidos/correcto.wav")
        sonido_incorrecto = pygame.mixer.Sound("sonidos/error.wav")
        sonido_final = pygame.mixer.Sound("sonidos/gameover.wav")
        #salir = False
        #elige una cancion de todas las disponibles
        azar=random.randrange(1,N+1)
        elegidos.append(azar) #la agrega a la lista de los ya elegidos
        archivo= open(".\\letras\\"+str(azar)+".txt","r", encoding='utf-8') # abre el archivo elegido con unicode.


        #lectura del archivo y filtrado de caracteres especiales, la primer linea es el artista y cancion
        aux=lectura(archivo, letra, artistaYcancion)
        letra=aux[1]
        artistaYcancion=aux[2]
        #elige una linea al azar y su siguiente
        lista=seleccion(letra)
        #print("Este es artista y canción: ",artistaYcancion)
##        print(lista)

        ayuda = "Cancionero"
        burla = " "
        prueba = burla

        dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda, prueba)

        #Fondo del juego iniciado
        fondojuego = pygame.image.load("imagenes/fondojuego.jpg").convert()
        screen.blit(fondojuego, (0, 0))
        #se muestran lo cambios en pantalla
        pygame.display.flip()

        #if correctas == 0:

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

##################### función de puntaje########################

            if int(segundos) < 1:
                print(int(segundos))
                perro = True
                sonido_final.play()
                while perro:
                    gameOver(screen,puntos)
                    pygame.display.flip()
                    archivo_puntos = open("max_score.txt","w")
                    archivo_puntos.write(str(puntos))#,str(nombre))
                    archivo_puntos.close()
                    for e in pygame.event.get():
                        #QUIT es apretar la X en la ventana
                        if e.type == QUIT:
                            pygame.mixer.music.play(1)
                            salir = True
                            return salir

                        if e.type == KEYDOWN:
                            #letraApretada = dameLetraApretada(e.key)
                            #if (str(letraApretada) == str(letraApretada)) or (str(letraApretada) == letraApretada):
                            if e.key == K_RETURN:
                                #pygame.time.delay(50)
                                pygame.mixer.music.play(-1)
                                perro = False

################################################################

            if True:
            	fps = 10

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.mixer.music.play(-1)
                    salir = True
                    #pygame.quit()
                    return salir

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letraApretada = dameLetraApretada(e.key)
                    palabraUsuario += letraApretada
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #chequea si es correcta y suma o resta puntos
                        sumar=esCorrecta(palabraUsuario, artistaYcancion, correctas)

                        puntos+=sumar
                        #puntos=puntos+puntaje(correctas)

                        if sumar>0:
                            sonido_correcto.play()
                            correctas=correctas+1
                            prueba= ""

                        else:
                            correctas=0
                            puntos = puntos -1
                            sonido_incorrecto.play()
                            burla=burlas()
                            prueba = burla
                            #draw_text(screen, str(burla), 30, ANCHO // 2, 400) # función para dibujar y burlar

                        if len(elegidos)==N:
                                elegidos=[]
                                masDeUnaVuelta = True

                        azar=random.randrange(1,N+1)
                        while(azar in elegidos):
                            azar=random.randrange(1,N+1)

                        elegidos.append(azar)

                        if masDeUnaVuelta == True:
                            #si las canciones se vuelven a repetir se mostrará una pista
                            lineaPistas=letra[0]
                            #guardo la primera linea (donde estan las pistas) en una variable
                            pistas=lineaPistas.split(sep=";")
                            #separo las pistas y las guardo en una lista
                            ayuda="Pista (anterior):" + pistas[0]


                        archivo= open(".\\letras\\"+str(azar)+".txt","r", encoding='utf-8')
                        palabraUsuario = ""
                        #lectura del archivo y filtrado de caracteres especiales
                        artistaYcancion=[]
                        letra = []
                        #lectura(archivo, letra, artistaYcancion)
                        aux1=lectura(archivo, letra, artistaYcancion)
                        letra= aux1[1]
                        artistaYcancion=aux1[2]
                        #elige una linea al azar y su siguiente
                        lista=seleccion(letra)


            segundos = TIEMPO_MAX +tiempoMenu - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            screen.blit(fondojuego, (0, 0))
            dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda, prueba)

            pygame.display.flip()

        archivo.close()

#Programa Principal ejecuta Main

if __name__ == "__main__":
    salir = False
    while 1:
        pygame.mixer.music.load("sonidos/rezo.mid")
        pygame.mixer.music.play(-1)

        if not salir:



            opciones = [
                ("Jugar", comenzar_nuevo_juego),
                ("Puntaje", mostrar_scoremax),
                ("Creditos", creditos),
                #("Salir", salir_del_programa)
                ]

            pygame.font.init()
            screen = pygame.display.set_mode((1200, 600))
            fondo = pygame.image.load("imagenes/fondo.jpg").convert()
            titulo = pygame.image.load("imagenes/cancionero.png")
            charly = pygame.image.load("imagenes/charlygarcia.png")
            cerati = pygame.image.load("imagenes/cerati.png")
            spinetta = pygame.image.load("imagenes/spinetta.png")
            calamaro = pygame.image.load("imagenes/calamaro.png")
            menu = Menu(opciones)

            while not salir:
                #Personajes del menu
                screen.blit(fondo, (0, 0))
                screen.blit(titulo, (100,100))
                screen.blit(charly, (500,485))
                screen.blit(cerati, (620,479))
                screen.blit(spinetta, (740,479))
                screen.blit(calamaro, (865,479))


                menu.actualizar()
                menu.imprimir(screen)
                pygame.display.flip()
                pygame.time.delay(10)

                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        salir = True
                        pygame.quit()
                        sys.exit()
                pygame.display.update()



        else:
            break
