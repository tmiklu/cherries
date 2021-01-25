import pygame, sys # import modules

pygame.init()

# create new window for graphics
screen = pygame.display.set_mode((800, 600))

# load custom icons
icon = pygame.image.load('icon/cherries.png')
pygame.display.set_icon(icon)

# custom window title
pygame.display.set_caption('Cherries')

# images
background = pygame.image.load("background/tree.jpg")

# bucket
bucket_img = pygame.image.load("bucket/bucket.png")
bucket_x = 380
bucket_y = 538
bucket_x_change = 0

# cherry
cherry_img = pygame.image.load("cherry/cherry.png")
cherry_x = 380
cherry_y = 200
cherry_y_change = 0.2

#
##
### functions
##
#
def bucket(x, y):
    screen.blit(bucket_img, (x, y))

def cherry(x, y):
    screen.blit(cherry_img, (x, y))

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right arrow was pressed")
                bucket_x_change += 0.3
            if event.key == pygame.K_LEFT:
                print("left arrow was pressed")
                bucket_x_change -= 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                print('key was released')
                # if key is release, stop moving (0)
                bucket_x_change = 0

    
    # game border
    if bucket_x <= 0:
        bucket_x = 0
    if bucket_x >= 736:
        bucket_x = 736
    
    # movement of bucket
    bucket_x += bucket_x_change

    # movement of cherry
    cherry_y += cherry_y_change
    if cherry_y >= 601:
        cherry_y_change = 0

    cherry(cherry_x, cherry_y)
    bucket(bucket_x, bucket_y)

    pygame.display.update()

