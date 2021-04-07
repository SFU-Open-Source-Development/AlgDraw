# The main UIS
import pygame
import pygame_gui
import random

pygame.init()


pygame.display.set_caption('Quick Start')

# create set size
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#6000A0'))

# initiate array bars
array = [0]*150
arrayColor = [0]*150

# create a color dictionary for r,g,b
colors = {
    "green": (0, 204, 102),
    "grey": (224, 224, 224)
}


def generateArray():
    for i in range(1, 150):
        arrayColor[i] = colors["green"]
        array[i] = random.randrange(1, 100)


generateArray()


def fill():
    draw()
    pygame.display.update()


def draw():
    # draw horizontal lines
    for i in range(1, 100):
        pygame.draw.line(
            window_surface,  # window
            colors["grey"],  # color
            (0, 2 * i + 100),       # start position
            (800, 2 * i + 100),     # end position
            1                       # width
        )

    # Draw the array values as lines
    for i in range(1, 100):
        pygame.draw.line(
            window_surface,
            colors["green"],
            (5 * i-3, 100),
            (5 * i-3, array[i]*2 + 100)
        )


# game loop
is_running = True

while is_running:

    window_surface.fill((255, 255, 255))

    for event in pygame.event.get():

        # handles close button
        if event.type == pygame.QUIT:
            is_running = False

        # handles keydown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                fill()
                draw()
    fill()
    draw()

    # window_surface.blit(background, (0, 0))

    pygame.display.update()
