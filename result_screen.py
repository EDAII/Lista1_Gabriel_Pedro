import pygame
from pygame.locals import *
import time
import start_game

def begin(result, steps_machine, steps_user):
    time.sleep(1)
    screen_size = (400, 150)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(result)
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    my_font = pygame.font.SysFont('bold', 80)
    result_font = pygame.font.SysFont('bold', 22)
    steps_font = pygame.font.SysFont('bold', 25)

    start_button_skin = pygame.Surface((100, 35))
    start_button_skin.fill((255, 255, 255))
    start_count = 0
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 286 and pygame.mouse.get_pos()[1]>=124:
                    if pygame.mouse.get_pos()[0] <= 384 and pygame.mouse.get_pos()[1]<=146:
                        start_game.start()
        pygame.display.update()
        screen.fill((150, 65, 200))
        text_surface = my_font.render(result, False, (255, 255, 255))
        if steps_machine!=steps_user:
            if steps_machine == 1:
                text2_surface = steps_font.render('Encontrei em ' + str(steps_machine) + ' passo,', False, (255, 255, 255))
            else:
                text2_surface = steps_font.render('Encontrei em ' + str(steps_machine) + ' passos,', False, (255, 255, 255))
            text3_surface = steps_font.render('você encontrou em ' + str(steps_user)+'.', False, (255, 255, 255))
            screen.blit(text2_surface, (75, 110))
            screen.blit(text3_surface, (75, 125))
        start_text_surface = result_font.render("PLAY AGAIN", False, (255, 0, 0))
        screen.blit(text_surface, (20,20))
        screen.blit(start_button_skin, (286, 125))

        if start_count > 100:
            screen.blit(start_text_surface, (290, 130))
        if start_count > 200:
            start_count = 0
        start_count+=1

        clock.tick(120)