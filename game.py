import pygame
from math import ceil
from pygame.locals import *
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
card_skin_selected.fill((255, 0, 0))
mouse_position = ()
card_selected = [()]
print(card_pos)

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
        if pos in card_selected:
            screen.blit(card_skin_selected, pos)
        else:
            screen.blit(card_skin, pos)

    pygame.display.update()