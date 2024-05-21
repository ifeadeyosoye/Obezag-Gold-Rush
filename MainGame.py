# importing modules
import pygame as py
from sys import exit
import time

# settings for display window
py.init()
screen = py.display.set_mode((800, 400))
py.display.set_caption('Obezag Gold Rush: Coin Collector')
pygame_icon = py.image.load('bitcoin-cryptocurrency-in-pixel-art-style-illustration-free-png.png').convert()
py.display.set_icon(pygame_icon)
clock = py.time.Clock()
test_font = py.font.Font('Pixeltype.ttf', 50)
#game_active = True

# SURFACES
# ground/sky surface
sky_surf = py.image.load('Sky.png').convert()
ground_surf = py.image.load('ground.png')

# text surfaces
score_surf = test_font.render('My Game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,26))

# volleyball surface
volleyball_surf = py.image.load('volleyball1.png').convert_alpha()
volleyball_rect = volleyball_surf.get_rect(bottomright = (600, 304))

# player surface
player_surf = py.image.load("person-walking1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,303))

# player gravity
player_gravity = 0

# game loop
while True:
    # exit for loop
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if (event.type == py.MOUSEBUTTONDOWN) and (player_rect.bottom >= 300):
            if player_rect.collidepoint(py.mouse.get_pos()):
               player_gravity = -19
        if (event.type == py.KEYDOWN) and (player_rect.bottom >= 300):
            if event.key == py.K_SPACE:
                player_gravity = -19

        # placing sky, ground, and score
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        py.draw.rect(screen, 'powderblue', score_rect)
        py.draw.rect(screen, 'powderblue', score_rect, 10)
        screen.blit(score_surf, score_rect)

        # placing and moving volleyball
        volleyball_rect.x -= 8
        if volleyball_rect.right < 0:
            volleyball_rect.left = 800
        screen.blit(volleyball_surf, volleyball_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 303:
            player_rect.bottom = 303
        screen.blit(player_surf, player_rect)

        # collision
        if volleyball_rect.colliderect(player_rect):
            time.sleep(0.5)
            py.quit()
            quit()


    py.display.update()
    # this while true loop should not run faster than 60 times per second
    clock.tick(60)







