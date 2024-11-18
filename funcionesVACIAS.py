from configuracion import *
from pygame.locals import *
import random
import math
import unicodedata
import pygame


#FUNCION AUXILIAR:
#Recorre cada linea del archivo y lo guarda en la lista correspondiente.
#La variable concatena guarda todos los caracteres eliminando los signos, y las tildes.

def cargarEnListas(linea, letra, artistaYcancion):
    concatena=""
    cont=0
    for i in range(len(linea)):
        if linea[i]=="-":
            concatena=concatena+" "  #Agrega un espacio vacio cuando hay un "-"
        if linea[i]=="Ã­":
            concatena=concatena+"i"
        if linea[i]=="Ã³":
            concatena=concatena+"o"
        if linea[i]=="Ã¡":
            concatena=concatena+"a"
        if linea[i]=="Ãº":
            concatena=concatena+"u"
        if linea[i]=="Ã©":
            concatena=concatena+"e"
        if linea[i]=="\n":
            concatena=concatena+"\n"
        if linea[i]=="!\n":
            concatena=concatena+"! "

        if linea[i]!=";" and linea[i]!="â€œ" and linea[i] !="â€" and linea[i] !='"' and linea[i]!="\n" and linea[i]!="▯":
            if linea[i]!="," and linea[i]!=":" and linea[i]!="?" and linea[i]!="Â¿":
                if linea[i]!="!" and linea[i]!="Â¡" and linea[i]!="-":
                    if linea[i]!="Ã¡" and linea[i]!="Ã©" and linea[i]!="Ã­" and linea[i]!="Ã³" and linea[i]!="Ãº":
                        concatena+=linea[i].lower()

    letra.append(concatena)
    concatena=""       #La variable concatena cada vez que entra vuelve a estar vacia

    return letra


def lectura(archivo, letra, artistaYcancion): #se queda solo con los oraciones de cierta longitud, filtra tildes, lee el archivo y

    letra=archivo.readlines() #carga *.txt en variable letra
    for i in range(1,len(letra)):#agarra el indice de cada linea
        cargarEnListas(letra[i], letra, artistaYcancion) #llamamos a la funcion cargarEnListas
                                                          #y toma como parametro cada linea del archivo.
    artistaYcancion=letra[0]
    archivo.close()

    return (archivo,letra,artistaYcancion)



#########################################################################

def seleccion(letra):#elige uno al azar, devuelve ese y el siguiente

    caracteres = '"@#%^&*()[]{}\n/<>?\|`~-=_+"'
    linea=random.randrange(2,len(letra)-1)
    contador=0
#Aquí saco simbolos raros que puedan llega a aparecer

    for x in letra[linea]:
        #if contador < 20:
            if x in caracteres:
                letra1=letra[linea].replace(x,"")
                contador+=1
            else:
                letra1=letra[linea]+x
                contador+=1

        #else:
        #    contador=0
        #    if x in caracteres:
        #        letra1=letra[linea].replace(x,"")+('\n')
        #        contador+=1
        #    else:
        #        letra1=letra[linea]+x+('\n')
        #        contador+=1


    for y in letra[linea+1]:
        if y in caracteres:
            letra2=letra[linea+1].replace(y,"")
        else:
            letra2=letra[linea+1]+y

    #print(letra1)
    #print(letra2)
    return (letra1,letra2)


def puntaje(correctas):
    #devuelve el puntaje, segun seguidilla

    if correctas == 0:
        correctas=1
        suma=correctas

    else:
        if correctas<=5:
            suma=correctas
        elif correctas>5:
            correctas=5
            suma=correctas
    print(suma)
    return suma


def esCorrecta(palabraUsuario, artistaYCancion, correctas):
    caracteres = '"@#$%^&*()[]{}:.\n/<>?\|`~-=_+ "'
    aux_palabraUsuario=""
    aux_artistaYCancion=""
    aux_artistaYCancion_List=[]
    suma=0

    while True: #creo lista con nombre de canción y/o artista
        for letra in artistaYCancion:
            if letra in caracteres:
                letra=letra.replace(letra,"") #quita espacio y caracteres especiales

            if letra != ";":
                aux_artistaYCancion=aux_artistaYCancion+str(letra)
            else:
                aux_artistaYCancion_List.append(aux_artistaYCancion)
                aux_artistaYCancion=""
        aux_artistaYCancion_List.append(aux_artistaYCancion) # Agrego la última concatenación ya que no termina en ";"

        print(aux_artistaYCancion)
        #print(aux_artistaYCancion_List)

        break
    for letra_biz in palabraUsuario: #creo lista del input del usuario
        if letra_biz in caracteres:
            letra_biz=letra_biz.replace(letra_biz,"") #quita espacio y caracteres especiales
            aux_palabraUsuario=aux_palabraUsuario+str(letra_biz)
        else:
            aux_palabraUsuario=aux_palabraUsuario+str(letra_biz)

    #print(aux_palabraUsuario)

    for i in range (0,len(aux_artistaYCancion_List)):
        str_artistaCancion = str(aux_artistaYCancion_List[i])
        if str_artistaCancion.lower() == aux_palabraUsuario:
            suma=puntaje(correctas)
            return suma

    return suma
    #return 0
    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla
    #sumar=esCorrecta(palabraUsuario, artistaYcancion, correctas) | Variable que llama a la función esCorrecta



def burlas():

    lista_burlas = ["Dale, ponele onda!!","Asi no vas a ganar nunca","A que estas jugando?","Dedicate a otra cosa...","Dios MIO!","Creo que la musica no es lo tuyo","Como musico, buen programador!"]

    indice_burlas = random.randrange(0,len(lista_burlas))

    burla=lista_burlas[indice_burlas]

    return burla












