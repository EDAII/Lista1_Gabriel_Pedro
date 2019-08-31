import pygame
from math import ceil
from pygame.locals import *
from src import result_screen, find, numbers_gen

def start():
    pygame.init()

    pygame.mixer.music.load("snd/start.wav")
    pygame.mixer.music.play(-1)

    screen_size = (705, 512)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Where is the card?')

    w = 7
    h = 7
    card_pos = []
    # criando posições das cartas
    while w < 705:
        while h < 462:
            card_pos.append((w, h))
            h += 67
        h = 7
        w += 47
    # criando superfície das cartas
    card_skin = pygame.Surface((35, 50))
    card_skin.fill((150, 65, 200))
    card_skin_selected = pygame.Surface((35, 50))
    card_skin_selected.fill((200, 35, 35))
    card_found = pygame.Surface((35, 50))
    card_found.fill((35, 200, 35))

    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('bold', 18)
    mouse_position = ()
    card_selected = [()]

    dict = {}
    numbers = numbers_gen.numbers_gen()
    number_to_find = numbers_gen.choose_number(numbers)
    binary_search_result = find.binary_search(number_to_find, numbers)
    index_search_result = find.index_search(number_to_find, numbers)
    pygame.display.set_caption('Where is the ' + str(number_to_find) + ' card?')
    card_to_found_fount = pygame.font.SysFont('bold', 40)
    card_to_found = card_to_found_fount.render('Where is the ' + str(number_to_find) + ' card?', False, (255, 255, 255))

    i = 0
    for p in card_pos:
        dict[p] = numbers[i]
        i += 1
    machine_steps = min(binary_search_result, index_search_result)
    user_steps = 0
    result = ''
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = (pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
                if mouse_position[0] <= 462:
                    last = [screen_size[0], screen_size[1]]
                    card_selected_index = (ceil((mouse_position[0]) / 67) - 1, ceil((mouse_position[1]) / 47) - 1)
                    card_selected.append(card_pos[card_selected_index[1] * 7 + card_selected_index[0]])
                    user_steps += 1
        pygame.display.update()
        screen.fill((0, 0, 0))
        if result:
            result_screen.begin(result, machine_steps, user_steps)
        for pos in card_pos:
            show = card_skin
            if pos in card_selected:
                if dict[pos] == number_to_find:
                    show = card_found
                    screen.blit(show, pos)
                    if user_steps > machine_steps:
                        result = 'Você perdeu.'
                    elif user_steps < machine_steps:
                        # time.sleep(3)
                        result = ('Você ganhou.')
                    else:
                        result = ('Empatamos')
                else:
                    show = card_skin_selected
                textsurface = myfont.render(str(dict[pos]), False, (255, 255, 255))
            screen.blit(show, pos)
            if pos in card_selected:
                screen.blit(textsurface, (pos[0], pos[1] + 18))
            screen.blit(card_to_found, (150, 472))
