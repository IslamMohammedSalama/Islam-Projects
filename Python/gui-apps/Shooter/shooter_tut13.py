import pygame
from pygame import mixer
import os
import random
import csv
import button

# mixer.init()
pygame.init()

SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h - 30
print(f'Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT}')
# SCREEN_WIDTH = 1250
# SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')
# set framerate
clock = pygame.time.Clock()
FPS = 60

# define game variables
GRAVITY = 0.75
SCROLL_THRESH = 200
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
MAX_LEVELS = 6

screen_scroll = 0
bg_scroll = 0
level = 1
start_game = False
start_intro = False
enemy_lenth = 0
max_enemey_lenth = 0
player_speed = 10
null_exit_imag = pygame.image.load('img/tile/20-2.png').convert_alpha()
exit_imag = pygame.image.load('img/tile/20.png').convert_alpha()
currnt_exit_image = null_exit_imag
# define player action variables
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False
fire = False
fire_thrown = False

# load music and sounds
# pygame.mixer.music.load('audio/music2.mp3')
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play(-1, 0.0, 5000)
# jump_fx = pygame.mixer.Sound('audio/jump.wav')
# jump_fx.set_volume(0.05)
# shot_fx = pygame.mixer.Sound('audio/shot.wav')
# shot_fx.set_volume(0.05)
# grenade_fx = pygame.mixer.Sound('audio/grenade.wav')
# grenade_fx.set_volume(0.05)


# load images
# button images
start_img = pygame.image.load('img/btns/start_btn.png').convert_alpha()
exit_img = pygame.image.load('img/btns/exit_btn.png').convert_alpha()
restart_img = pygame.image.load('img/btns/restart_btn.png').convert_alpha()
# background
pine1_img = pygame.image.load('img/background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('img/background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('img/background/mountain.png').convert_alpha()
sky_img = pygame.image.load('img/background/sky_cloud.png').convert_alpha()
# store tiles in a list
img_list = []

for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/tile/{x}.png')
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)
# bullet
bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()
# grenade
grenade_img = pygame.image.load('img/icons/grenade.png').convert_alpha()
# fire
fire_img = pygame.image.load('img/icons/fire.png').convert_alpha()
# pick up boxes
health_box_img = pygame.image.load('img/icons/health_box.png').convert_alpha()
ammo_box_img = pygame.image.load('img/icons/ammo_box.png').convert_alpha()
grenade_box_img = pygame.image.load(
    'img/icons/grenade_box.png').convert_alpha()
fire_box_img = pygame.image.load('img/icons/fire_box.png').convert_alpha()
speeder_box_img = pygame.image.load(
    'img/icons/speeder_box.png').convert_alpha()
item_boxes = {
    'Health': health_box_img,
    'Ammo': ammo_box_img,
    'Grenade': grenade_box_img,
    'Fire': fire_box_img,
    'Speeder': speeder_box_img
}

text_of_task = 'Kill All Enemies To Open The Next Level '
# define colors
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 255, 255)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)

# define font
font = pygame.font.SysFont('Futura', 30)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_bg():
    screen.fill(BG)
    width = sky_img.get_width()
    for x in range(5):
        screen.blit(sky_img, ((x * width) - bg_scroll * 0.5, 0))
        screen.blit(mountain_img, ((x * width) - bg_scroll * 0.6,
                    SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, ((x * width) - bg_scroll * 0.7,
                    SCREEN_HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img, ((x * width) - bg_scroll * 0.8,
                    SCREEN_HEIGHT - pine2_img.get_height()))

# function to reset level


def reset_level():
    enemy_group.empty()
    bullet_group.empty()
    grenade_group.empty()
    fire_group.empty()
    explosion_group.empty()
    item_box_group.empty()
    decoration_group.empty()
    water_group.empty()
    exit_group.empty()

    # create empty tile list
    data = []
    for row in range(ROWS):
        r = [-1] * COLS
        data.append(r)

    return data


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades, health, fires):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.grenades = grenades
        self.fires = fires
        self.health = health
        self.MAX_HEALTH = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 0
        self.killed = False
        self.MAX_AMMOS , self.MAX_GRENADES , self.MAX_FIRES = 125,80,60


        # load all images for the players
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(
                f'img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(
                    f'img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(
                    img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 4

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True:  # and self.in_air == False:

            if self.rect.top + dy > SCREEN_HEIGHT:
                dy = 0
            else:
                self.vel_y = -(player_speed + 5 if player_speed <=
                               20 else player_speed)
                self.jump = False
                self.in_air = True
        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the ai has hit a wall then make it turn around
                if self.char_type == 'enemy':
                    self.direction *= -1

                    # self.vel_y = -20
                    self.move_counter = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top

                    # Add this line to make the player fall when hitting the ceiling

                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with water
        if pygame.sprite.spritecollide(self, water_group, False):
            self.health = 0

        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True

        # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # check if going off the edges of the screen
        if self.char_type == 'player':
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                dx = 0
        if self.rect.top + dy < 0 or self.rect.bottom + dy < 0 > SCREEN_HEIGHT:
            # dy = 0
            self.vel_y = 0
            dy = self.vel_y

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        # update scroll based on player position
        if self.char_type == 'player':
            if (self.rect.right > SCREEN_WIDTH - SCROLL_THRESH and bg_scroll < (world.level_length * TILE_SIZE) - SCREEN_WIDTH)\
                    or (self.rect.left < SCROLL_THRESH and bg_scroll > abs(dx)):
                self.rect.x -= dx
                screen_scroll = -dx

        return screen_scroll, level_complete

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.75 *
                            self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            # reduce ammo
            self.ammo -= 1
            # shot_fx.play()

    def ai(self):
        if self.alive and player.alive:
            if self.idling == False and random.randint(1, 200) == 1:
                self.update_action(0)  # 0: idle
                self.idling = True
                self.idling_counter = 50
            # check if the ai in near the player
            if self.vision.colliderect(player.rect):
                # stop running and face the player
                self.update_action(0)  # 0: idle
                # shoot
                self.shoot()
            else:
                if self.idling == False:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update ai vision as the enemy moves
                    self.vision.center = (
                        self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scroll
        self.rect.x += screen_scroll

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global enemy_lenth
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)
            if not self.killed and self.char_type == 'enemy':
                enemy_lenth -= 1
                self.killed = True

    def draw(self):
        screen.blit(pygame.transform.flip(
            self.image, self.flip, False), self.rect)


class World():
    def __init__(self):
        self.obstacle_list = []

    def process_data(self, data,ammo_count,grenade_count,fire_count):
        global enemy_lenth , max_enemey_lenth
        self.level_length = len(data[0])
        # iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    # if True:
                    # 	enemy = Soldier('enemy', x * TILE_SIZE, y * TILE_SIZE, 1.65, 2, 20, 0,100,0)
                    # 	enemy_group.add(enemy)
                    # and random.choice([True,False]):
                    if tile == random.choice([11, 12, 13, 14, 17, 18, 19, 11, 12, 13, 14,]):
                        item_box = random.choice([ItemBox('Ammo', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Fire', x * TILE_SIZE, y * TILE_SIZE), ItemBox(
                            'Health', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Grenade', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Speeder', x * TILE_SIZE, y * TILE_SIZE)])
                        item_box_group.add(item_box)
                        enemy = Soldier('enemy', x * TILE_SIZE,
                                        y * TILE_SIZE, 1.65, 2, 20, 0, 100, 0)
                        enemy_group.add(enemy)
                        enemy_lenth += 1
                        max_enemey_lenth = enemy_lenth
                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                        # item_box = random.choice([ItemBox('Ammo', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Fire', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Health', x * TILE_SIZE, y * TILE_SIZE),ItemBox('Grenade', x * TILE_SIZE, y * TILE_SIZE),ItemBox('Speeder', x * TILE_SIZE, y * TILE_SIZE)])
                        # item_box_group.add(item_box)
                    elif tile >= 9 and tile <= 10:
                        water = Water(img, x * TILE_SIZE, y * TILE_SIZE)
                        water_group.add(water)
                    elif tile >= 11 and tile <= 14:
                        decoration = Decoration(
                            img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_group.add(decoration)
                        # item_box = random.choice([ItemBox('Ammo', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Fire', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Health', x * TILE_SIZE, y * TILE_SIZE),ItemBox('Grenade', x * TILE_SIZE, y * TILE_SIZE),ItemBox('Speeder', x * TILE_SIZE, y * TILE_SIZE)])
                        # item_box_group.add(item_box)
                    elif tile == 15:  # create player
                        player = Soldier(
                            'player', x * TILE_SIZE, y * TILE_SIZE, 1.65, player_speed, ammo_count, grenade_count, 2500, fire_count)  # 1.65
                        health_bar = HealthBar(
                            220, 10, player.health, player.health)
                    # create enemies
                    elif tile == random.choice([ 11, 12, 13, 14, ]) or tile == 16 :
                        enemy = Soldier('enemy', x * TILE_SIZE,
                                        y * TILE_SIZE, 1.65, 2, 20, 0, 100, 0)
                        enemy_group.add(enemy)
                        enemy_lenth += 1
                        max_enemey_lenth = enemy_lenth


                    elif tile == 17:  # create ammo box
                        item_box = random.choice([ItemBox('Ammo', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Fire', x * TILE_SIZE, y * TILE_SIZE), ItemBox(
                            'Health', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Grenade', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Speeder', x * TILE_SIZE, y * TILE_SIZE)])
                        item_box_group.add(item_box)
                    elif tile == 18:  # create grenade box
                        item_box = random.choice([ItemBox('Ammo', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Fire', x * TILE_SIZE, y * TILE_SIZE), ItemBox(
                            'Health', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Grenade', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Speeder', x * TILE_SIZE, y * TILE_SIZE)])
                        item_box_group.add(item_box)
                    elif tile == 19:  # create health box
                        item_box = random.choice([ItemBox('Ammo', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Fire', x * TILE_SIZE, y * TILE_SIZE), ItemBox(
                            'Health', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Grenade', x * TILE_SIZE, y * TILE_SIZE), ItemBox('Speeder', x * TILE_SIZE, y * TILE_SIZE)])
                        item_box_group.add(item_box)
                    elif tile == 20:  # create exit
                        exit = Exit(currnt_exit_image, x *
                                    TILE_SIZE, y * TILE_SIZE)
                        exit_group.add(exit)

        return player, health_bar

    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])


class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class Water(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class Exit(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))
        self.image_changed = False

    def update(self):
        global currnt_exit_image
        self.rect.x += screen_scroll
        if enemy_lenth == 0 and not self.image_changed:
            # print('yes')
            currnt_exit_image = exit_imag
            self.image_changed = True
        elif enemy_lenth != 0 and self.image_changed:
            # print('no')
            currnt_exit_image = null_exit_imag
            self.image_changed = False
        self.image = currnt_exit_image


class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def update(self):
        global player_speed
        # scroll
        self.rect.x += screen_scroll
        # check if the player has picked up the box
        if pygame.sprite.collide_rect(self, player):
            # check what kind of box it was
            if self.item_type == 'Health':
                player.health += 500
                if player.health >= player.MAX_HEALTH:
                    player.health = player.MAX_HEALTH
            elif self.item_type == 'Ammo':
                # print('ammo 1')
                # if  player.ammo > player.MAX_AMMOS:
                #     player.ammo = player.MAX_AMMOS

                #     print('ammo 2')
                # else :
                player.ammo += 15
                if  player.ammo >= player.MAX_AMMOS:
                    player.ammo = player.MAX_AMMOS
                # print('ammo 3')
            elif self.item_type == 'Grenade':
                # print('grenade 1')
                # if  player.grenades > player.MAX_GRENADES:
                #     player.grenades = player.MAX_GRENADES
                #     print('grenade 2')
                # else :
                player.grenades += 3
                if  player.grenades >= player.MAX_GRENADES:
                    player.grenades = player.MAX_GRENADES
                    # print('grenade 3')
            elif self.item_type == 'Fire':
                # print('fire 1')
                # if  player.fires > player.MAX_FIRES:
                #     player.fires = player.MAX_FIRES
                #     print('fire 2')
                # else :
                player.fires += 3
                if  player.fires >= player.MAX_FIRES:
                    player.fires = player.MAX_FIRES
                # print('fire 3')
            elif self.item_type == 'Speeder':
                player_speed += 5
                player.speed = player_speed
            # delete the item box
            self.kill()


class HealthBar():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health

    def draw(self, health):
        # update with new health
        self.health = health
        # calculate health ratio
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, RED, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 150 * ratio, 20))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed) + screen_scroll

        # check for collision with level
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                # self.direction = self.direction * -1
                self.kill()
        # check collision with characters
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 25
                # self.direction = self.direction * -1
                self.kill()
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= 20
                    # self.direction = self.direction * -1
                    self.kill()


class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -12.5
        self.speed = 8
        self.image = grenade_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction

    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        # check for collision with level
        for tile in world.obstacle_list:
            # check collision with walls
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                self.direction *= -1
                dx = self.direction * self.speed
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0
                # check if below the ground, i.e. thrown up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom
        if self.rect.top + dy < 0 or self.rect.bottom + dy < 0 > SCREEN_HEIGHT:
            # dy = 0
            self.vel_y = 0
            dy = self.vel_y

        # update grenade position
        self.rect.x += dx + screen_scroll
        self.rect.y += dy

        # countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            # grenade_fx.play()
            self.direction = self.direction * 1
            explosion = Explosion(self.rect.x, self.rect.y, 0.5)
            explosion_group.add(explosion)
            # do damage to anyone that is nearby
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 2 and \
                    abs(self.rect.centery - player.rect.centery) < TILE_SIZE * 2:
                player.health -= 50
                self.kill()
                pass
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 2 and \
                        abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 2:
                    enemy.health -= 100
                    # self.kill()
                    # check for collision with level
            for tile in world.obstacle_list:
                if tile[1].colliderect(self.rect):
                    self.kill()
                    # pass


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(
                f'img/explosion/exp{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        # scroll
        self.rect.x += screen_scroll

        EXPLOSION_SPEED = 4
        # update explosion amimation
        self.counter += 1

        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.frame_index += 1
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]


class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -12.5
        self.speed = 8
        self.image = fire_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction

    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        # check for collision with level
        for tile in world.obstacle_list:
            # check collision with walls
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                self.kill()
                self.direction *= -1
                dx = self.direction * self.speed
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0
                # check if below the ground, i.e. thrown up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom
        if self.rect.top + dy < 0 or self.rect.bottom + dy < 0 > SCREEN_HEIGHT:
            # dy = 0
            self.vel_y = 0
            dy = self.vel_y

        # update fire position
        self.rect.x += dx + screen_scroll
        self.rect.y += dy

        # countdown timer
        self.timer -= 3
        if True:  # self.timer <= 0:
            # self.kill()
            # grenade_fx.play()
            self.direction = self.direction * 1
            explosion = Explosion(self.rect.x, self.rect.y, 0.5)
            explosion_group.add(explosion)
            # do damage to anyone that is nearby
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 2 and \
                    abs(self.rect.centery - player.rect.centery) < TILE_SIZE * 2:
                # player.health -= 50
                # self.kill()
                pass
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 2 and \
                        abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 2:
                    enemy.health -= 100
                    # self.kill()
                    # check for collision with level
            for tile in world.obstacle_list:
                if tile[1].colliderect(self.rect):
                    self.kill()
                    # pass


class ScreenFade():
    def __init__(self, direction, color, speed):
        self.direction = direction
        self.color = color
        self.speed = speed
        self.fade_counter = 0

    def fade(self):
        fade_complete = False
        self.fade_counter += self.speed
        if self.direction == 1:  # whole screen fade
            pygame.draw.rect(
                screen, self.color, (0 - self.fade_counter, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.color, (SCREEN_WIDTH //
                             2 + self.fade_counter, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.color, (0, 0 -
                             self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT // 2))
            pygame.draw.rect(screen, self.color, (0, SCREEN_HEIGHT //
                             2 + self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.direction == 2:  # vertical screen fade down
            pygame.draw.rect(screen, self.color,
                             (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))
        if self.fade_counter >= SCREEN_WIDTH:
            fade_complete = True

        return fade_complete


# create screen fades
intro_fade = ScreenFade(1, BLACK, 15)
death_fade = ScreenFade(2, PINK, 15)

# create buttons
start_button = button.Button(
    SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 150, start_img, 1)
exit_button = button.Button(SCREEN_WIDTH // 2 - 110,
                            SCREEN_HEIGHT // 2 + 50, exit_img, 1)
restart_button = button.Button(
    SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, restart_img, 2)

# create sprite groups
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

# create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)
# load in level data and create world
with open(f'levels/level{level}_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)
world = World()
player, health_bar = world.process_data(world_data,25,5,5)

run = True
if __name__ == '__main__':
    while run:

        clock.tick(pygame.time.Clock().get_fps())

        if start_game == False:
            # draw menu
            screen.fill(BG)
            # add buttons
            if start_button.draw(screen):
                start_game = True
                start_intro = True
            if exit_button.draw(screen):
                run = False
        else:
            # update background
            draw_bg()
            # draw world map
            world.draw()
            # show player health
            draw_text(f'HEALTH: {player.health}/{player.MAX_HEALTH} , ', font, WHITE, 10, 10)

            health_bar.draw(player.health)
            # show ammo
            draw_text(f'AMMO: {player.ammo}/{player.MAX_AMMOS} , ', font, WHITE, 10, 35)
            for x in range(player.ammo):
                screen.blit(bullet_img, (175 + (x * 10), 40))
            # show grenades
            draw_text(f'GRENADES: {player.grenades}/{player.MAX_GRENADES} , ', font, WHITE, 10, 60)
            for x in range(player.grenades):
                screen.blit(grenade_img, (205 + (x * 15), 60))
            # show fires
            draw_text(f'FIRES: {player.fires}/{player.MAX_FIRES} , ', font, WHITE, 10, 80)
            for x in range(player.fires):
                screen.blit(fire_img, (145 + (x * 15), 80))
            draw_text(f'ENEMEYS: {enemy_lenth}/{max_enemey_lenth}', font, WHITE, 10, 100)
            draw_text(f'LEVEL: {level}/{MAX_LEVELS}', font, WHITE, 10, 120)
            draw_text(text_of_task, font, RED if enemy_lenth !=
                    0 else BLUE, 10, 140)

            player.update()
            player.draw()

            for enemy in enemy_group:
                enemy.ai()
                enemy.update()
                enemy.draw()

            # update and draw groups
            bullet_group.update()
            grenade_group.update()
            fire_group.update()
            explosion_group.update()
            item_box_group.update()
            decoration_group.update()
            water_group.update()
            exit_group.update()
            bullet_group.draw(screen)
            grenade_group.draw(screen)
            fire_group.draw(screen)
            explosion_group.draw(screen)
            item_box_group.draw(screen)
            decoration_group.draw(screen)
            water_group.draw(screen)
            exit_group.draw(screen)

            # show intro
            if start_intro == True:
                if intro_fade.fade():
                    start_intro = False
                    intro_fade.fade_counter = 0

            # update player actions
            if player.alive:
                # shoot bullets
                if shoot:
                    player.shoot()
                # throw grenades
                elif grenade and grenade_thrown == False and player.grenades > 0:
                    grenade = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction),
                                    player.rect.top, player.direction)
                    grenade_group.add(grenade)
                    # reduce grenades
                    player.grenades -= 1
                    grenade_thrown = True
                elif fire and fire_thrown == False and player.fires > 0:
                    fire = Fire(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction),
                                player.rect.top, player.direction)
                    fire_group.add(fire)
                    # reduce fires
                    player.fires -= 1
                    fire_thrown = True
                if player.in_air:
                    player.update_action(2)  # 2: jump
                elif moving_left or moving_right:
                    player.update_action(1)  # 1: run
                else:
                    player.update_action(0)  # 0: idle
                screen_scroll, level_complete = player.move(
                    moving_left, moving_right)
                bg_scroll -= screen_scroll
                # check if player has completed the level
                if level_complete and enemy_lenth == 0:
                    start_intro = True
                    level += 1
                    player_speed = player_speed // 2 + 3
                    enemy_lenth = 0
                    max_enemey_lenth = 0
                    bg_scroll = 0
                    currnt_exit_image = null_exit_imag

                    world_data = reset_level()
                    for row in range(ROWS):
                        r = [-1] * COLS
                        world_data.append(r)
                    # world_data = reset_level()
                    if level <= MAX_LEVELS:
                        # load in level data and create world
                        with open(f'levels/level{level}_data.csv', newline='') as csvfile:
                            reader = csv.reader(csvfile, delimiter=',')
                            for x, row in enumerate(reader):
                                for y, tile in enumerate(row):
                                    world_data[x][y] = int(tile)
                        world = World()
                        player, health_bar = world.process_data(world_data,player.ammo + 10 if not player.ammo >= player.MAX_AMMOS else player.MAX_AMMOS
                                                                ,player.grenades + 5 if not player.grenades >= player.MAX_GRENADES else player.MAX_GRENADES,
                                                                player.fires + 5 if not player.fires >= player.MAX_FIRES else player.MAX_FIRES)
            else:
                screen_scroll = 0
                if death_fade.fade():
                    if restart_button.draw(screen):
                        death_fade.fade_counter = 0
                        start_intro = True
                        bg_scroll = 0
                        player_speed = player_speed // 2 + 3
                        currnt_exit_image = null_exit_imag
                        world_data = reset_level()
                        # load in level data and create world
                        with open(f'levels/level{level}_data.csv', newline='') as csvfile:
                            reader = csv.reader(csvfile, delimiter=',')
                            for x, row in enumerate(reader):
                                for y, tile in enumerate(row):
                                    world_data[x][y] = int(tile)
                        world = World()
                        player, health_bar = world.process_data(world_data,20,5,5)

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
            # keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_SPACE:
                    shoot = True
                if event.key == pygame.K_q:
                    grenade = True
                if event.key == pygame.K_f:
                    fire = True

                if event.key == pygame.K_w and player.alive:
                    player.jump = True
                    # jump_fx.play()
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_UP:
                    player.jump = True
                    # jump_fx.play()

            # keyboard button released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_SPACE:
                    shoot = False
                if event.key == pygame.K_q:
                    grenade = False
                    grenade_thrown = False
                if event.key == pygame.K_f:
                    fire = False
                    fire_thrown = False
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_UP:
                    player.jump = False
            if enemy_lenth == 0 and level != MAX_LEVELS:
                text_of_task = 'Go To New Level Indicator to Continue '
            elif enemy_lenth != 0 and level == MAX_LEVELS:
                text_of_task = 'Kill All Enemies To Complate The Game '
            elif enemy_lenth == 0 and level == MAX_LEVELS:
                text_of_task = 'You Have Completed The Game '
            else:
                text_of_task = 'Kill All Enemies To Open The Next Level '

        pygame.display.update()

    pygame.quit()
