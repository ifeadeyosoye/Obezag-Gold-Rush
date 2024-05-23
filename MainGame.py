# things to do
# music/sound effects; 2nd obstacle; increase difficulty as time goes on; animate objects; extra ability/mechanic (invincibility?), menu screen, tutorial screen, home button in menu screen?
# accumilating "ult" bar. Once triggered, can double jump over flying obstacles to get coins worth double?
# or maybe extra life?
# like a health bar that has 3 hearts for 3 extra lives that fills up slowly

# importing modules
import pygame as py
from sys import exit
from random import randint

# functions defined
def display_score(score_count):
    """Updating and displaying score"""
    score_message = "Score: {}".format(score_count)
    score_surf = test_font.render(score_message, False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 26))
    py.draw.rect(screen, 'powderblue', score_rect)
    py.draw.rect(screen, 'powderblue', score_rect, 10)
    screen.blit(score_surf, score_rect)

def display_final_score(score_count):
    """showing final score in ending screen"""
    score_message = "Your Score: {}".format(score_count)
    ending_score_surf = test_font.render("Your Score: {}".format(score_count), False, (64, 64, 64))
    ending_score_rect = ending_score_surf.get_rect(center=(400, 360))
    py.draw.rect(screen, 'powderblue', ending_score_rect)
    py.draw.rect(screen, 'powderblue', ending_score_rect, 10)
    screen.blit(ending_score_surf, ending_score_rect)

def obstacle_movement(obstacle_list):
    """moving obstacles"""
    # if list is empty, if statement doesn't run/ checking if list is empty
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 8
            if obstacle_rect.bottom == 304:
                screen.blit(volleyball_surf, obstacle_rect)
            else:
                screen.blit(bird_surf, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True


# settings for display window
py.init()
screen = py.display.set_mode((800, 400))
py.display.set_caption('Obezag Gold Rush: Coin Collector')
pygame_icon = py.image.load('coin.png').convert_alpha()
py.display.set_icon(pygame_icon)
clock = py.time.Clock()
test_font = py.font.Font('Pixeltype.ttf', 50)



# SURFACES
# ground/sky surface
sky_surf = py.image.load('Sky.png').convert()
ground_surf = py.image.load('ground.png').convert()

# text surfaces
ending_surf = test_font.render('Press Space to Start Again!', False, (64,64,64))
ending_rect = ending_surf.get_rect(center = (400, 50))

# OBSTACLES
# volleyball surface
volleyball_surf = py.image.load('volleyball1.png').convert_alpha()
#volleyball_rect = volleyball_surf.get_rect(bottomright = (600, 304))

bird_surf = py.image.load("bird1.png").convert_alpha()
obstacle_rect_list = []

# player surface
player_surf = py.image.load("person-walking1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 303))

# ending scene player surfaces
player_ending_surf = py.image.load("person_standing.png").convert_alpha()
player_ending_surf1 = py.transform.scale(player_ending_surf, (192, 252))
player_ending_rect = player_ending_surf1.get_rect(center = (400, 200))

# coin surface
coin_surf = py.image.load('coin.png').convert_alpha()
coin_rect = coin_surf.get_rect(bottomright = (randint(1500, 3000), 300))

# OTHER VALUES
# player gravity
player_gravity = 0
# coin count
score_count = 0
# Timer
obstacle_timer = py.USEREVENT + 1
py.time.set_timer(obstacle_timer, 1400)
# game active
game_active = True

# game loop
while True:
    # exit for loop
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()

        if game_active == True:
            if (event.type == py.MOUSEBUTTONDOWN) and (player_rect.bottom >= 300):
                if player_rect.collidepoint(py.mouse.get_pos()):
                    player_gravity = -19

            if (event.type == py.KEYDOWN) and (player_rect.bottom >= 300):
                if event.key == py.K_SPACE:
                    player_gravity = -19
        else:
            if (event.type == py.KEYDOWN) and (event.key == py.K_SPACE):
                game_active = True
                #volleyball_rect.left = 800

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(volleyball_surf.get_rect(bottomright = (randint(900, 1110), 304)))
            else:
                obstacle_rect_list.append(bird_surf.get_rect(bottomright = (randint(900, 1110), 170)))


    if game_active == True:
        # placing sky, ground, and score
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        display_score(score_count)

        # placing and moving volleyball
       # volleyball_rect.x -= 8
       # if volleyball_rect.right < 0:
         #   volleyball_rect.left = 800
       # screen.blit(volleyball_surf, volleyball_rect)

        # placing and moving coin
        coin_rect.x -= 8
        if coin_rect.right < 0:
            coin_rect.right = 800
        screen.blit(coin_surf, coin_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 303:
            player_rect.bottom = 303
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision volleyball
        if collisions(player_rect, obstacle_rect_list) == False:
            game_active = False
            final_score_count = score_count
            score_count = 0

        # collision coin
        if coin_rect.colliderect(player_rect):
            coin_rect.right = 800
            display_score(score_count)
            score_count += 1

    else:
        screen.fill("lightskyblue")
        display_final_score(final_score_count)
        py.draw.rect(screen, 'powderblue', ending_rect)
        py.draw.rect(screen, 'powderblue', ending_rect, 10)
        screen.blit(ending_surf, ending_rect)
        screen.blit(player_ending_surf1, player_ending_rect)
        obstacle_rect_list.clear()

    py.display.update()
    # this while true loop should not run faster than 60 times per second
    clock.tick(60)