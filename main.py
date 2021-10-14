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
#call main routine
titulo = input("Inserta un título: ")
main2(size, titulo)