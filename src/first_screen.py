import pygame
from pygame.locals import *

def begin():
    pygame.init()

    init_sound = pygame.mixer.Sound("snd/init.wav")
    init_sound.play()

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

    # INSTRUCTIONS
    ins_font = pygame.font.SysFont('bold', 25)
    ins_texts = []
    ins_texts.append(ins_font.render("Como jogar:", False, (255, 255, 255)))
    ins_texts.append(ins_font.render("Seu objetivo é encontrar uma carta antes do computador.", False, (255, 255, 255)))
    ins_texts.append(ins_font.render("As cartas estão organizadas na seguinte ordem: ", False, (255, 255, 255)))
    ins_texts.append(ins_font.render("A ordem é crescente porém a distribuição é aleatória.", False, (255, 255, 255)))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                init_sound.stop()
                if pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[1]>=390:
                    if pygame.mouse.get_pos()[0] <= 647 and pygame.mouse.get_pos()[1]<=425:
                        return
        pygame.display.update()
        screen.fill((150, 65, 200))
        text_surface = my_font.render("Where is the Card?", False, (255, 255, 255))
        start_text_surface = start_font.render("START", False, (255, 0, 0))
        screen.blit(text_surface, (80,10))
        screen.blit(start_button_skin, (599, 390))
        #SHOW INSTRUCTIONS:
        image = pygame.image.load('img/game.png')
        image = pygame.transform.scale(image, (440, 320))
        pos_y = 60
        for ins in ins_texts[:-1]:
            screen.blit(ins, (100,pos_y))
            pos_y+=20
        screen.blit(image, (130,120))
        screen.blit(ins_texts[-1], (100, 442))
        if start_count > 100:
            screen.blit(start_text_surface, (600, 400))
        if start_count > 200:
            start_count = 0
        start_count+=1

        clock.tick(120)
