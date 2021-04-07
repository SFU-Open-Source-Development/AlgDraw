# The main UIS
import pygame
import pygame_gui
import random


pygame.init()
pygame.font.init()  # initialize font in order to use fonts

pygame.display.set_caption('Algorthm Visualizer')  # set caption

window_surface = pygame.display.set_mode((800, 600))  # set size

# initialize ariel font
arielFont = pygame.font.SysFont("Ariel", 30)

# color dictionary for r,g,b in tuple
colors = {
    "green": (0, 204, 102),
    "grey": (224, 224, 224),
    "blue": (66, 135, 245),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
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

    # render text
    # parameters: (text, antialias, color, background=None)
    text = arielFont.render("Press SPACE BAR to sort.", True, colors["black"])
    window_surface.blit(text, (100, 0))

    # Draw the array values as bars
    for i in range(1, MAX_BAR_HEIGHT):
        pygame.draw.line(
            # parameters: screen object, line color, starting position, ending position, width
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


def updateScreenWhenSorting():
    window_surface.fill(colors["white"])    # clear all bars
    draw()                                  # redraw all the bars
    pygame.display.update()                 # refresh the screen
    pygame.time.delay(30)                   # wait time for screen refresh


def selection_sort(arr):
    # Selection sort for testing

    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        updateScreenWhenSorting()           # update the visuals


is_running = True
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
                print("Space key pressed.")
                generateArray()
                selection_sort(array)
                pygame.display.update()  # redundant?
    draw()
    # initializes pygame's screen
    pygame.display.update()

    # window_surface.blit(background, (0, 0)) # redundant?
