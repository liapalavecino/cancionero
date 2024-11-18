# -*- coding: utf-8 -*-
#
# autor: Hugo Ruscitti | Modificado y adaptado por alumnos de la UNGS
#
#Esteban Bolañez
#Lía Palavecino
#Ailen Cortez
#
#web: www.losersjuegos.com.ar
# licencia: GPL 2

import random
import pygame, sys
from pygame.locals import *
from principal import *
from configuracion import *
pygame.mixer.init()


class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (255, 255, 255))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 205
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('imagenes/nota.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    "Representa un menú con opciones para un juego"

    def __init__(self, opciones):

        self.opciones = []
        fuente = pygame.font.Font('fuente/gameover.ttf', 30) #Fuente de la letra mostrada
        x = 213
        y = 305
        paridad = 1

        self.cursor = Cursor(x - 40, y, 40)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 40
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""
        sonido_menu = pygame.mixer.Sound("sonidos/menu.wav")
        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                sonido_menu.play()
                self.seleccionado -= 1

            elif k[K_DOWN]:
                sonido_menu.play()
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)


def mostrar_scoremax():

    credit = True
    while True:

        screen = pygame.display.set_mode((ANCHO, ALTO))
        fondo = pygame.image.load("imagenes/fondo.jpg").convert()
        #screen.blit(fondo,(0,0))
        record_puntaje = open("max_score.txt","r")
        pts = str(record_puntaje.readlines())
        FontCredito= pygame.font.Font('fuente/gameover.ttf',40)
        FontCredito_chico= pygame.font.Font('fuente/gameover.ttf',30)
        TAMANNO_CREDITO = 40
        TAMANNO_CREDITO_CHICO = 30
        mensaje1 = "El record de puntaje es:"
        mensaje2 = pts
        mensaje3 = 'Presione "Tecla Cualquiera" o en la X para volver'

        while credit == True:
            screen.blit(fondo,(0,0))
            screen.blit(FontCredito.render(mensaje1,1,(200,42,42)),(ANCHO//2-(len(mensaje1)*TAMANNO_CREDITO//3.5),200))
            screen.blit(FontCredito.render(mensaje2,1,(200,42,42)),(ANCHO//2-(len(mensaje2)*TAMANNO_CREDITO//3.5),250))
            screen.blit(FontCredito_chico.render(mensaje3,1,(255,255,255)),(ANCHO//2-(len(mensaje3)*TAMANNO_CREDITO_CHICO//4),400))
            pygame.display.update()
            for e in pygame.event.get():
                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    #pygame.mixer.music.play(1)
                    credit = False

                    #pygame.quit()
                    #return
                if e.type == KEYDOWN:
                    #pygame.mixer.music.play(-1)
                    letraApretada = dameLetraApretada(e.key)
                    print(letraApretada)
                    if (str(letraApretada) == str(letraApretada)) or (str(letraApretada) == letraApretada):
                        credit = False
        break
    return

def creditos():
    credit = True
    while True:

        screen = pygame.display.set_mode((ANCHO, ALTO))
        fondo = pygame.image.load("imagenes/fondo.jpg").convert()
        #screen.blit(fondo,(0,0))

        FontCredito= pygame.font.Font('fuente/gameover.ttf',40)
        FontCredito_chico= pygame.font.Font('fuente/gameover.ttf',30)
        TAMANNO_CREDITO = 40
        TAMANNO_CREDITO_CHICO = 30
        mensaje1 = "Programa desarrollado por GRUPO: 6 - IP"
        mensaje2 = "Con mucho esfuezo para sacarnos un 10 (DIEZ)"
        mensaje3 = 'Presione "Tecla Cualquiera" o en la X para volver'

        while credit == True:
            screen.blit(fondo,(0,0))
            screen.blit(FontCredito.render(mensaje1,1,(200,42,42)),(ANCHO//2-(len(mensaje1)*TAMANNO_CREDITO//3.5),200))
            screen.blit(FontCredito.render(mensaje2,1,(200,42,42)),(ANCHO//2-(len(mensaje2)*TAMANNO_CREDITO//3.5),250))
            screen.blit(FontCredito_chico.render(mensaje3,1,(255,255,255)),(ANCHO//2-(len(mensaje3)*TAMANNO_CREDITO_CHICO//4),400))
            pygame.display.update()
            for e in pygame.event.get():
                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    #pygame.mixer.music.play(1)
                    credit = False

                    #pygame.quit()
                    #return
                if e.type == KEYDOWN:
                    #pygame.mixer.music.play(-1)
                    letraApretada = dameLetraApretada(e.key)
                    print(letraApretada)
                    if (str(letraApretada) == str(letraApretada)) or (str(letraApretada) == letraApretada):
                        credit = False
        break
    return

