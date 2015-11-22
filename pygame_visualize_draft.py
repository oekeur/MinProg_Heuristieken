# Visualization for rushhour

import pygame

def VisualizeCars():
    background_colour = (255, 255, 255)
    (width, height) = (700, 600)
    padding = 20

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Rushhour, board 1")
    screen.fill(background_colour)

    # board frameword
    pygame.draw.rect(screen, (0, 0, 255), (padding, padding, (width - (padding + padding)), (height - (padding + padding))), 2)

    # board lines
    board_length = 6
    blocklength = (width- (padding + padding))/board_length
    blockheight = (height-(padding + padding))/board_length
    for i in range (1, board_length):
        xposition = blocklength * i
        yposition = blockheight * i
        pygame.draw.line(screen, (0, 0, 255), (padding + xposition, padding), (padding + xposition, height - padding))
        pygame.draw.line(screen, (0, 0, 255), (padding, padding + yposition), (width - padding, padding + yposition))

    # 1 car
    pygame.draw.rect(screen, (255, 0, 0), (padding, padding, blocklength, blockheight), 0)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # import cars - lists
    # iterate over this list
    # create a rectangle
        # pygame.draw.rect(screen, (0, 0, 255), (20, 20 + yposition), (width - 20, 20 + yposition))
        # for car in cars:
VisualizeCars()
