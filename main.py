import pygame, sys # import modules

pygame.init()

# create new window for graphics
screen = pygame.display.set_mode((800, 600))

# images
background = pygame.image.load("background/tree.jpg")

# bucket
bucket = pygame.image.load("bucket/bucket.png")
bucketx = 399
buckety = 600

#
##
### Game loop
##
#
running = True
while running:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            print(event)
    
    pygame.display.update()

