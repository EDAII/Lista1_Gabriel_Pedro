import pygame
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
print(len(card_pos))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    for pos in card_pos:
        screen.blit(card_skin, pos)
    pygame.display.update()