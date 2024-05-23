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
            if obstacle_rect.bottom == 300:
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

def player_animation():
    """display jump/walking animations for player"""
    global player_surf, player_index

    if player_rect.bottom < 303:
        player_surf = player_jump
    else:
        player_index += 0.14
        if player_index > len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

def coin_animation():
    global coin_surf, coin_index

    coin_index += 0.045
    if coin_index > len(coin_frames):
        coin_index = 0
    coin_surf = coin_frames[int(coin_index)]



# settings for display window
py.init()
screen = py.display.set_mode((800, 400))
py.display.set_caption('Obezag Gold Rush: Coin Collector')
pygame_icon = py.image.load('coin1.png').convert_alpha()
py.display.set_icon(pygame_icon)
clock = py.time.Clock()
test_font = py.font.Font('Pixeltype.ttf', 50)



# SURFACES
# ground/sky surface
sky_surf = py.image.load('Sky.png').convert()
ground_surf = py.image.load('ground.png').convert()


# OBSTACLES SURFACES
# volleyball surface
volleyball_frame1 = py.image.load('volleyball11.png').convert_alpha()
volleyball_frame2 = py.image.load('volleyball2.png').convert_alpha()
volleyball_frame3 = py.image.load('volleyball3.png').convert_alpha()
volleyball_frame4 = py.image.load('volleyball4.png').convert_alpha()
volleyball_frames = [volleyball_frame1, volleyball_frame2, volleyball_frame3, volleyball_frame4]
volleyball_frame_index = 0
volleyball_surf = volleyball_frames[volleyball_frame_index]
#volleyball_rect = volleyball_surf.get_rect(bottomright = (600, 304))

# bird surfaces
bird_frame1 = py.image.load('bird1.png').convert_alpha()
bird_frame2 = py.image.load('bird2.png').convert_alpha()
bird_frames = [bird_frame1, bird_frame2]
bird_frame_index = 0
bird_surf = bird_frames[bird_frame_index]

obstacle_rect_list = []

# player surface
player_walk1 = py.image.load("person-walking1.png").convert_alpha()
player_walk2 = py.image.load("person-walking2.png").convert_alpha()
player_walk3 = py.image.load("person-walking3.png").convert_alpha()
player_walk = [player_walk1, player_walk2, player_walk3]
player_index = 0
player_jump = py.image.load("person-walking1.png").convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 303))

# coin surface
coin_frame1 = py.image.load('coin1.png').convert_alpha()
coin_frame2 = py.image.load('coin2.png').convert_alpha()
coin_frames = [coin_frame1, coin_frame2]
coin_index = 0
coin_surf = coin_frames[coin_index]
coin_rect = coin_surf.get_rect(bottomright = (randint(1500, 3000), 300))

# RESTART SCENE
# player surfaces (RESTART)
player_ending_surf = py.image.load("person_standing.png").convert_alpha()
player_ending_surf1 = py.transform.scale(player_ending_surf, (192, 252))
player_ending_rect = player_ending_surf1.get_rect(center = (400, 200))
# text surfaces (RESTART)
ending_surf = test_font.render('Press Space to Start Again!', False, (64,64,64))
ending_rect = ending_surf.get_rect(center = (400, 50))



# OTHER VALUES

# player gravity
player_gravity = 0

# coin count
score_count = 0

# game active
game_active = True


# Timers
# obstacle timers
obstacle_timer = py.USEREVENT + 1
py.time.set_timer(obstacle_timer, 1400)
# animation timers
volleyball_animation_timer = py.USEREVENT + 2
py.time.set_timer(volleyball_animation_timer, 150)
bird_animation_timer = py.USEREVENT + 2
py.time.set_timer(bird_animation_timer, 200)


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
        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(volleyball_surf.get_rect(bottomright = (randint(900, 1110), 300)))
                else:
                    obstacle_rect_list.append(bird_surf.get_rect(bottomright = (randint(900, 1110), 170)))

            if event.type == volleyball_animation_timer:
                volleyball_frame_index += 1
                if volleyball_frame_index > (len(volleyball_frames) - 1):
                    volleyball_frame_index = 0
                volleyball_surf = volleyball_frames[volleyball_frame_index]

            if event.type == bird_animation_timer:
                bird_frame_index += 1
                if bird_frame_index > (len(bird_frames) -1):
                    bird_frame_index = 0
                bird_surf = bird_frames[bird_frame_index]

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
        coin_animation()
        screen.blit(coin_surf, coin_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 303:
            player_rect.bottom = 303
        player_animation()
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision volleyball/birds
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