import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong Game")

# Load background image
background = pygame.image.load("pong_table.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Colors
white = (255, 255, 255)  # White color for texts and lines
red = (0, 250, 250)  # Red color for player1 paddle
blue = (255, 50, 0)  # Blue color for player2 paddle
orange = (0, 250, 250)  # Orange color for the ball

# Game objects
margin_top = 100  # Margin for the smaller playing field
margin_left = 50  # Margin for the smaller playing field
play_area = pygame.Rect(
    margin_left,
    margin_top,
    screen_width - 2 * margin_left,
    screen_height - 2 * margin_top,
)

ball_speed = [4, 4]
max_ball_speed = 10
ball = pygame.Rect(play_area.centerx - 10, play_area.centery - 10, 20, 20)
player1 = pygame.Rect(play_area.right - 40, play_area.centery - 40, 20, 120)
player2 = pygame.Rect(play_area.left + 25, play_area.centery - 40, 20, 120)

# Speeds
player1_speed = 0
player2_speed = 0
all_players_speed = 5
max_all_players_speed = 10
# Font
font = pygame.font.Font(None, 74)
font_title = pygame.font.Font(None, 34)

game_title = font_title.render("Ping Pong Game", True, white)

# Scores
player1_score = 0
player2_score = 0

# Clock
clock = pygame.time.Clock()


def ball_animation():
    global ball_speed, player1_score, player2_score, orange
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= play_area.top or ball.bottom >= play_area.bottom:
        ball_speed[1] = -ball_speed[1]
    if ball.left <= play_area.left:
        player1_score += 1
        orange = (0, 250, 250)
        ball_speed[0] = -ball_speed[0]
        increase_ball_speed()
    if ball.right >= play_area.right:
        player2_score += 1
        orange = (255, 50, 0)
        ball_speed[0] = -ball_speed[0]
        increase_ball_speed()

    if ball.colliderect(player1) and ball_speed[0] > 0:
        orange = (255, 50, 0)
        ball_speed[0] = -ball_speed[0]
    if ball.colliderect(player2) and ball_speed[0] < 0:
        orange = (0, 250, 250)
        ball_speed[0] = -ball_speed[0]


def increase_ball_speed():
    global all_players_speed
    if abs(ball_speed[0]) < max_ball_speed:
        ball_speed[0] = ball_speed[0] + 1 if ball_speed[0] > 0 else ball_speed[0] - 1
        all_players_speed = all_players_speed + 1 if all_players_speed < max_all_players_speed else all_players_speed
    if abs(ball_speed[1]) < max_ball_speed:
        ball_speed[1] = ball_speed[1] + 1 if ball_speed[1] > 0 else ball_speed[1] - 1
        all_players_speed = all_players_speed + 1 if all_players_speed < max_all_players_speed else all_players_speed


def player1_animation():
    player1.y += player1_speed
    if player1.top <= play_area.top:
        player1.top = play_area.top
    if player1.bottom >= play_area.bottom:
        player1.bottom = play_area.bottom


def player2_animation():
    player2.y += player2_speed
    if player2.top <= play_area.top:
        player2.top = play_area.top
    if player2.bottom >= play_area.bottom:
        player2.bottom = play_area.bottom


def ball_restart():
    global ball_speed
    ball.center = (play_area.centerx, play_area.centery)
    ball_speed[0] = -ball_speed[0]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_speed -= all_players_speed
            if event.key == pygame.K_DOWN:
                player1_speed += all_players_speed
            if event.key == pygame.K_w:
                player2_speed -= all_players_speed
            if event.key == pygame.K_s:
                player2_speed += all_players_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1_speed += all_players_speed
            if event.key == pygame.K_DOWN:
                player1_speed -= all_players_speed
            if event.key == pygame.K_w:
                player2_speed += all_players_speed
            if event.key == pygame.K_s:
                player2_speed -= all_players_speed

    ball_animation()
    player1_animation()
    player2_animation()

    screen.blit(background, (0, 0))  # Draw the background image
    pygame.draw.rect(screen, white, play_area, 2)  # Draw the play area
    pygame.draw.rect(screen, red, player1)
    pygame.draw.rect(screen, blue, player2)
    pygame.draw.ellipse(screen, orange, ball)

    player1_text = font.render(str(player1_score), True, white)
    screen.blit(player1_text, (screen_width // 2 + 50, screen_height // 2 - 70))

    player2_text = font.render(str(player2_score), True, white)
    screen.blit(player2_text, (screen_width // 2 - 100, screen_height // 2 - 70))

    screen.blit(game_title, (screen_width // 2 - game_title.get_width() / 2, 40))
    pygame.display.flip()
    clock.tick(60)
