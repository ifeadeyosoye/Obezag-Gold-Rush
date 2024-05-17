# importing modules
import pygame as py
from sys import exit

# settings for display window
py.init()
screen = py.display.set_mode((800, 400))
py.display.set_caption('Obezag Gold Rush: Coin Collector')
pygame_icon = py.image.load('bitcoin-cryptocurrency-in-pixel-art-style-illustration-free-png.png').convert()
py.display.set_icon(pygame_icon)
clock = py.time.Clock()
test_font = py.font.Font('Pixeltype.ttf', 50)

# Surfaces
sky_surface = py.image.load('Sky.png').convert()
ground_surface = py.image.load('ground.png')
text_surface = test_font.render('My game', False, 'Black')

# volleyball surface
volleyball_surface = py.image.load('volleyball1.png').convert_alpha()
volleyball_x_pos = 600


while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))

    volleyball_x_pos -= 4
    if volleyball_x_pos < 0:
        volleyball_x_pos = 800
    screen.blit(volleyball_surface, (volleyball_x_pos, 250))

    py.display.update()
    # this while true loop should not run faster than 60 times per second
    clock.tick(60)







