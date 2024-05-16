# importing modules
import pygame as py
from sys import exit

# settings for display window
py.init()
screen = py.display.set_mode((800, 400))
py.display.set_caption('Obezag Gold Rush: Coin Collector')
pygame_icon = py.image.load('cute-rabbit-characters-png.png')
py.display.set_icon(pygame_icon)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    # draw all the elements
    # update everything
    py.display.update()







