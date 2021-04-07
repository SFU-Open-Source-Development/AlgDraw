# The main UIS
import pygame
import pygame_gui
import random

pygame.init()

pygame.display.set_caption('Algorthm Visualizer')

# Size
window_surface = pygame.display.set_mode((800, 600))


# color dictionary for r,g,b in tuple
colors = {
    "green": (0, 204, 102),
    "grey": (224, 224, 224),
    "blue": (66, 135, 245),
    "white": (255, 255, 255)
}

background = pygame.Surface((800, 600))
background.fill(colors["blue"])


# constant variables
ARRAY_LENGTH = 150
MAX_BAR_HEIGHT = 100

# initiate array bars
array = [0]*ARRAY_LENGTH
# arrya to hold bar color
arrayColor = [0]*ARRAY_LENGTH


def generateArray():
    # creates a random array
    for i in range(1, ARRAY_LENGTH):
        arrayColor[i] = colors["green"]
        array[i] = random.randrange(1, MAX_BAR_HEIGHT)


def draw():
    # Draw the array values as lines
    for i in range(1, MAX_BAR_HEIGHT):
        pygame.draw.line(
            # PARAMETERS: screen object, line color, starting position, ending position, width
            window_surface,
            colors["green"],
            (5 * i-3, MAX_BAR_HEIGHT),
            (5 * i-3, array[i]*2 + MAX_BAR_HEIGHT),
            3
        )

    # this for loop draws horizontal lines
    # for i in range(1, 100):
    #     pygame.draw.line(
    #         window_surface,
    #         colors["grey"],
    #         (0, 2 * i + 100),
    #         (800, 2 * i + 100),
    #         1
    #     )


def fill():
    draw()
    pygame.display.update()


# game loop
is_running = True

# generate rnadom array
generateArray()

while is_running:

    window_surface.fill(colors["white"])

    for event in pygame.event.get():

        # handles exit/close button
        if event.type == pygame.QUIT:
            is_running = False

        # handles return key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("key pressed.")
                draw()
                pygame.display.update()
                # fill()
    draw()
    # fill the screen with random bars
    # fill()

    # window_surface.blit(background, (0, 0))

    pygame.display.update()
