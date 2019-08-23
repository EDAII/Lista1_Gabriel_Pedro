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
mouse_position = ()
print(card_pos)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_position = (pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
            last = [screen_size[0], screen_size[1]]
            card_selected = (ceil((mouse_position[0])/67),ceil((mouse_position[1])/47))
            print(card_selected)
            #print(card_selected)

    screen.fill((0,0,0))
    for pos in card_pos:
        screen.blit(card_skin, pos)
    pygame.display.update()