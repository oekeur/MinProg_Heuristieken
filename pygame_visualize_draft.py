# Problem Set 6:
# Visualization code for simulated robots.
#
# See the problem set for instructions on how to use this code.

import pygame

background_colour = (255, 255, 255)
(width, height) = (700, 600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rushhour, board 1")
screen.fill(background_colour)


pygame.draw.rect(screen, (0, 0, 255), (20, 20, (width - 40), (height - 40)), 2)
board_length = 6
for i in range (1, board_length):
    xposition = ((width-40)/(board_length)) * i
    yposition = ((height-40)/(board_length)) * i
    pygame.draw.line(screen, (0, 0, 255), (20 + xposition, 20), (20 + xposition, height -20))
    pygame.draw.line(screen, (0, 0, 255), (20, 20 + yposition), (width - 20, 20 + yposition))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
