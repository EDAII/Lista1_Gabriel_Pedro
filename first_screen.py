import pygame
from math import ceil
from pygame.locals import *
import numbers_gen
import find


def begin():
    pygame.init()
    screen_size = (705, 462)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Where is the card?')
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    my_font = pygame.font.SysFont('bold', 80)
    start_font = pygame.font.SysFont('bold', 22)

    start_button_skin = pygame.Surface((50, 35))
    start_button_skin.fill((255, 255, 255))
    start_count = 0
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[1]>=390:
                    if pygame.mouse.get_pos()[0] <= 647 and pygame.mouse.get_pos()[1]<=425:
                        return
        pygame.display.update()
        screen.fill((150, 65, 200))
        text_surface = my_font.render("Where is the Card?", False, (255, 255, 255))
        start_text_surface = start_font.render("START", False, (255, 0, 0))
        screen.blit(text_surface, (50,50))
        screen.blit(start_button_skin, (599, 390))
        if start_count > 100:
            screen.blit(start_text_surface, (600, 400))
        if start_count > 200:
            start_count = 0
        start_count+=1

        clock.tick(120)