import pygame
from math import ceil
from pygame.locals import *
import numbers_gen
pygame.init()
screen_size = (705, 462)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Where is the card?')

w = 7
h = 7
card_pos = []
while w < screen_size[0]:
    while h < screen_size[1]:
        card_pos.append((w, h))
        h+=67
    h = 7
    w+=47


card_skin = pygame.Surface((35, 50))
card_skin.fill((150, 65, 200))
card_skin_selected = pygame.Surface((35, 50))
card_skin_selected.fill((200, 35, 35))
card_found = pygame.Surface((35, 50))
card_found.fill((35, 200, 35))

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 18)



mouse_position = ()
card_selected = [()]
print(card_pos)

dict = {}
numbers = numbers_gen.numbers_gen()
number_to_find = numbers_gen.choose_number(numbers)
pygame.display.set_caption('Where is the ' + str(number_to_find) + ' card?')
i = 0
for p in card_pos:
    dict[p] = numbers[i]
    i+=1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_position = (pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
            last = [screen_size[0], screen_size[1]]
            card_selected_index = (ceil((mouse_position[0])/67)-1,ceil((mouse_position[1])/47)-1)
            card_selected.append(card_pos[card_selected_index[1]*7+card_selected_index[0]])


    screen.fill((0,0,0))

    for pos in card_pos:
        show = card_skin
        if pos in card_selected:
            if dict[pos] == number_to_find:
                show = card_found
            else:
                show = card_skin_selected
            textsurface = myfont.render(str(dict[pos]), False, (255, 255, 255))
        screen.blit(show, pos)
        if pos in card_selected:
            screen.blit(textsurface, (pos[0], pos[1]+18))



    pygame.display.update()