import pygame, sys # import modules

pygame.init()

# create new window for graphics
screen = pygame.display.set_mode((800, 600))

#
##
### Game loop
##
#
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

