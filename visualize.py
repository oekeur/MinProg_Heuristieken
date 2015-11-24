# Visualization for rushhour

import pygame

def VisualizeCars():
    background_colour = (255, 255, 255)
    (width, height) = (700, 600)
    padding = 20
    colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 150, 0), (150, 0, 0), (0, 0, 150), (150, 150, 150), (95, 10, 10), (10, 95, 10), (10, 10, 95)]

    # visualization screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Rushhour, board 1")
    screen.fill(background_colour)

    # board framework
    pygame.draw.rect(screen, (0, 0, 255), (padding, padding, (width - (padding + padding)), (height - (padding + padding))), 2)

    # board lines
    blocklength = (width- (padding + padding))/boardsize
    blockheight = (height-(padding + padding))/boardsize
    for i in range (1, boardsize):
        xposition = blocklength * i
        yposition = blockheight * i
        pygame.draw.line(screen, (0, 0, 255), (padding + xposition, padding), (padding + xposition, height - padding))
        pygame.draw.line(screen, (0, 0, 255), (padding, padding + yposition), (width - padding, padding + yposition))

    # draw cars
    i = 0
    # for each car
    for car in cars:
        # if orientation is horizontal update the tile to the right from last tile
        if cars[i][1] == 'h':
            if cars[i][2] == 2:
                pygame.draw.rect(screen, colours[i], (padding + (blocklength * (cars[i][4])), padding + (blockheight * (cars[i][3])), blocklength * 2, blockheight), 0)
            else:
                pygame.draw.rect(screen, colours[i], (padding + (blocklength * (cars[i][4])), padding + (blockheight *(cars[i][3])), blocklength * 3, blockheight), 0)
        else:
            if cars[i][2] == 2:
                pygame.draw.rect(screen, colours[i], (padding + (blocklength * (cars[i][4])), padding + (blockheight * (cars[i][3])), blocklength, blockheight * 2), 0)
            else:
                pygame.draw.rect(screen, colours[i], (padding + (blocklength * (cars[i][4])), padding + (blockheight * (cars[i][3])), blocklength, blockheight * 3), 0)
        i += 1

    pygame.display.flip()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                