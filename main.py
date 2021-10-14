# Import a library of functions called 'pygame'
import pygame
from main_functions import *
# Initialize the game engine
pygame.init()
#Set window size
size = [1300, 600]
width = int(input("Ancho de la ventana: "))
height = int(input("Alto de l ventana: "))
size[0] = width
size[1] = height
#Set color background
colorfondo = [255, 255, 255]
nivelrojo = int(input("Nivel de color rojo: "))
nivelverde = int(input("Nivel de color verde: "))
nivelazul = int(input("Nivel de verde: "))
colorfondo[0] = nivelrojo
colorfondo[1] = nivelverde
colorfondo[2] = nivelazul
#call main routine
titulo = input("Inserta un título: ")
main2(size, titulo, colorfondo)