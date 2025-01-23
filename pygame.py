import pygame
import sys
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CIRCLE GAME FOR CT")

circle_radius = 30
border_thickness = 2
circle_color = (255, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle_position = event.pos
                pygame.draw.circle(screen, circle_color, circle_position, circle_radius, border_thickness)

    pygame.display.flip()

pygame.quit()
sys.exit()