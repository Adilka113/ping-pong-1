import pygame
from pygame.locals import *


pygame.init()


width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")


bg_color = pygame.Color("black")
player_color = pygame.Color("white")


player_width, player_height = 15, 60
player1_pos = (10, height / 2 - player_height / 2)
player2_pos = (width - player_width - 10, height / 2 - player_height / 2)


player_speed = 5
player1_direction = 0
player2_direction = 0


ball_radius = 10
ball_speed_x = 4
ball_speed_y = 4
ball_pos = [width / 2, height / 2]


def draw_player(player_pos):
    pygame.draw.rect(screen, player_color, Rect(player_pos, (player_width, player_height)))


def draw_ball(ball_pos):
    pygame.draw.circle(screen, player_color, ball_pos, ball_radius)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                player1_direction = -1
            elif event.key == K_s:
                player1_direction = 1
            if event.key == K_UP:
                player2_direction = -1
            elif event.key == K_DOWN:
                player2_direction = 1
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                player1_direction = 0
            if event.key == K_UP or event.key == K_DOWN:
                player2_direction = 0


    player1_pos = (player1_pos[0], player1_pos[1] + player1_direction * player_speed)
    player2_pos = (player2_pos[0], player2_pos[1] + player2_direction * player_speed)


    if player1_pos[1] < 0:
        player1_pos = (player1_pos[0], 0)
    if player1_pos[1] > height - player_height:
        player1_pos = (player1_pos[0], height - player_height)
    if player2_pos[1] < 0:
        player2_pos = (player2_pos[0], 0)
    if player2_pos[1] > height - player_height:
        player2_pos = (player2_pos[0], height - player_height)


    ball_pos[0] += ball_speed_x
    ball_pos[1] += ball_speed_y


    if ball_pos[1] >= height - ball_radius or ball_pos[1] <= ball_radius:
        ball_speed_y = -ball_speed_y
    if ball_pos[0] >= width - ball_radius or ball_pos[0] <= ball_radius:
        ball_speed_x = -ball_speed_x


    if player1_pos[0] <= ball_pos[0] <= player1_pos[0] + player_width and player1_pos[1] <= ball_pos[1] <= player1_pos[1] + player_height:
        ball_speed_x = -ball_speed_x
    if player2_pos[0] <= ball_pos[0] <= player2_pos[0] + player_width and player2_pos[1] <= ball_pos[1] <= player2_pos[1] + player_height:
        ball_speed_x = -ball_speed_x


    screen.fill(bg_color)
    draw_player(player1_pos)
    draw_player(player2_pos)
    draw_ball(ball_pos)
    pygame.display.flip()
    pygame.time.delay(10)
