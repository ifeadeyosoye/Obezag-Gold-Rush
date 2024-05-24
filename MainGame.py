# things to do
# music/sound effects; increase difficulty as time goes on; animate objects; extra ability/mechanic (invincibility?), menu screen, tutorial screen, home button in menu screen?
# accumilating "ult" bar. Once triggered, can double jump over flying obstacles to get coins worth double?
# or maybe extra life?
# like a health bar that has 3 hearts for 3 extra lives that fills up slowly
# make game pause for game over sound.
# heart system?
# hold highest score?

# importing modules
import pygame as py
from sys import exit
from random import randint, choice
import time

# classes defined
class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = py.image.load("person-walking1.png").convert_alpha()
        player_walk2 = py.image.load("person-walking2.png").convert_alpha()
        player_walk3 = py.image.load("person-walking3.png").convert_alpha()
        self.player_walk = [player_walk1, player_walk2, player_walk3]
        self.player_index = 0
        self.player_jump = py.image.load("person-walking1.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,303))
        self.gravity = 0

        self.jump_sound = py.mixer.Sound('jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = py.key.get_pressed()
        mouse = py.mouse.get_pressed()
        if keys[py.K_SPACE] and self.rect.bottom >= 303:
            self.gravity = -19
            self.jump_sound.play()
        elif (event.type == py.MOUSEBUTTONDOWN) and (self.rect.bottom >= 303):
            if self.rect.collidepoint(py.mouse.get_pos()):
                self.gravity = -19
                self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 303:
            self.rect.bottom = 303

    def animation_state(self):
        if self.rect.bottom < 303:
            self.image = self.player_jump
        else:
            self.player_index += 0.14
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]


    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(py.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'bird':
            bird_frame1 = py.image.load('bird1.png').convert_alpha()
            bird_frame2 = py.image.load('bird2.png').convert_alpha()
            self.frames = [bird_frame1, bird_frame2]
            y_pos = 170
        else:
            volleyball_frame1 = py.image.load('volleyball11.png').convert_alpha()
            volleyball_frame2 = py.image.load('volleyball2.png').convert_alpha()
            volleyball_frame3 = py.image.load('volleyball3.png').convert_alpha()
            volleyball_frame4 = py.image.load('volleyball4.png').convert_alpha()
            self.frames = [volleyball_frame1, volleyball_frame2, volleyball_frame3, volleyball_frame4]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index > (len(self.frames)):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 8
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

class Coin(py.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'coin':
            coin_frame1 = py.image.load('coin1.png').convert_alpha()
            coin_frame2 = py.image.load('coin2.png').convert_alpha()
            self.coin_frames = [coin_frame1, coin_frame2]

        self.coin_index = 0
        self.image = self.coin_frames[self.coin_index]
        self.rect = self.image.get_rect(bottomright = (randint(1500, 3000), 300))

    def animation_state(self):
        self.coin_index += 0.045
        if self.coin_index > len(self.coin_frames):
            self.coin_index = 0
        self.image = self.coin_frames[int(self.coin_index)]

    def destroy(self):
        global score_count

        if collision_coin_sprite():
            coin_collect_sound.play()
            self.kill()
            score_count += 1
            display_score(score_count)
            print(score_count)

    def reset(self):
        if self.rect.right < 0:
            self.rect.right = randint(1200, 2500)

    def update(self):
        self.animation_state()
        self.rect.x -= 8
        self.destroy()
        self.reset()


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

def collision_sprite():
    global death_sound

    if py.sprite.spritecollide(player.sprite, obstacle_group, False):
        death_sound.play()
        obstacle_group.empty()
        return False
    else:
        return True

def collision_coin_sprite():
    if py.sprite.spritecollide(player.sprite, coin, False):
        #coin.sprite.kill()
        return True
    else:
        return False


# settings for display window
py.init()
screen = py.display.set_mode((800, 400), vsync=1)
py.display.set_caption('Obezag Gold Rush: Coin Collector')
pygame_icon = py.image.load('coin1.png').convert_alpha()
py.display.set_icon(pygame_icon)
clock = py.time.Clock()
test_font = py.font.Font('Pixeltype.ttf', 50)
bg_music = py.mixer.Sound('combined-theme-song-1.mp3')
bg_music.set_volume(0.3)
bg_music.play(loops = -1)

# Groups
player = py.sprite.GroupSingle()
player.add(Player())
obstacle_group = py.sprite.Group()
coin = py.sprite.Group()


# SURFACES
# ground/sky surface
sky_surf = py.image.load('Sky.png').convert()
ground_surf = py.image.load('ground.png').convert()


# RESTART SCENE
# player surfaces (RESTART)
player_ending_surf = py.image.load("person_standing.png").convert_alpha()
player_ending_surf1 = py.transform.scale(player_ending_surf, (192, 252))
player_ending_rect = player_ending_surf1.get_rect(center = (400, 200))
# text surfaces (RESTART)
ending_surf = test_font.render('Press Space to Start Again!', False, (64,64,64))
ending_rect = ending_surf.get_rect(center = (400, 50))

# OTHER VALUES
# coin count
score_count = 0
# game active
game_active = True

# TIMERS
# obstacle timers
obstacle_timer = py.USEREVENT + 1
py.time.set_timer(obstacle_timer, 1400)
# coin timer
coin_timer = py.USEREVENT + 1
py.time.set_timer(coin_timer, 1200)

# SOUNDS
coin_collect_sound = py.mixer.Sound('coincollect.mp3')
coin_collect_sound.set_volume(0.8)
death_sound = py.mixer.Sound('gameover1.mp3')
death_sound.set_volume(1.5)

# game loop
while True:
    # exit for loop
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()

        if game_active != True:
            if (event.type == py.KEYDOWN) and (event.key == py.K_SPACE):
                game_active = True

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['bird', 'volleyball', 'volleyball', 'volleyball'])))

        if game_active:
            if event.type == coin_timer:
                coin.add(Coin(choice(['coin', 'coin'])))

    if game_active == True:
        # placing sky, ground, and score
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        display_score(score_count)

        # Player
        player.draw(screen)
        player.update()

        # Coins
        coin.draw(screen)
        coin.update()

        # Obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()

        # collision with volleyball/birds
        if collision_sprite() == False:
            game_active = False
            final_score_count = score_count
            score_count = 0

    else:
        # restart screen
        screen.fill("lightskyblue")
        display_final_score(final_score_count)
        py.draw.rect(screen, 'powderblue', ending_rect)
        py.draw.rect(screen, 'powderblue', ending_rect, 10)
        screen.blit(ending_surf, ending_rect)
        screen.blit(player_ending_surf1, player_ending_rect)


    py.display.update()
    # this while true loop should not run faster than 60 times per second
    clock.tick(60)