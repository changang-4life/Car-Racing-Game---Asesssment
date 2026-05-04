""" Car Racing Game
v1 - Program Setup
    - Import and Initialise the Pygame module
    - Screen window
    - Image imports
"""

import pygame
pygame.init()

icon = pygame.image.load("game_icon.png")

screen = pygame.display.set_mode((1100, 550))

font = pygame.font.SysFont("",40) # placeholder for text
test_text = font.render(f"Testing, testing 123", True, (255, 255, 255))

#                         --- Car Images ---                           
car1 = pygame.image.load("car_1.png")
car2 = pygame.image.load("car_2.png")
car3 = pygame.image.load("car_3.png")
car4 = pygame.image.load("car_4.png")
car5 = pygame.image.load("car_5.png")
car6 = pygame.image.load("car_6.png")

pygame.display.set_icon("game_icon.png")

def game_loop():
    quit_game = False
    screen.blit(test_text, (400, 260))
    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

        pygame.display.update()

game_loop()