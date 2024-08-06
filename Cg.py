import pygame   
import sys

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode ((screen_width, screen_height))
pygame.display.set_caption(('Animação de elemento gráfico'))

white = (255,255,255)
red = (255, 0, 0)

circle_x = 5
circle_y = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

circle_x += speed_x
circle_y += speed_y

if circle_x + circle_radius > screen_width or circle_x - circle_radius < 0:
    speed_x = -speed_x
if circle_y = circle_radius > screen_height or circle_y - circle_radius < 0:
    speed_y = -speed_y

screen.fill(white)

pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius)

pygame.display.flip()

pygame.time.Cloack()
