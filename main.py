import pygame, sys # import modules
import math
import random

pygame.init()

print(pygame.font.get_fonts())

# create new window for graphics
screen = pygame.display.set_mode((800, 600))

# load custom icons
icon = pygame.image.load('icon/cherries.png')
pygame.display.set_icon(icon)

# custom window title
pygame.display.set_caption('Cherries')

# images
background = pygame.image.load("background/tree.jpg")

# score
score = 0
myfont = pygame.font.SysFont("comicsansms", 17)

# bucket
bucket_img = pygame.image.load("bucket/bucket.png")
bucket_x = 380
bucket_y = 538
bucket_x_change = 0

# cherry
cherry_img = pygame.image.load("cherry/cherry.png")
cherry_x = random.randint(87, 737)
cherry_y = random.randint(166, 314) #200
cherry_y_change = 0.2

print(cherry_y)
print(cherry_x)

#
##
### functions
##
#
def bucket(x, y):
    screen.blit(bucket_img, (x, y))

def cherry(x, y):
    screen.blit(cherry_img, (x, y))

def isCollision(bucket_x, bucket_y, cherry_x, cherry_y):
    distance = math.sqrt(math.pow(cherry_x - bucket_x, 2) + (math.pow(cherry_y - bucket_y, 2)))
    # distance between cherry and bucket
    if distance < 22:
        return True
    else:
        return False

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
                bucket_x_change += 0.5
            if event.key == pygame.K_LEFT:
                print("left arrow was pressed")
                bucket_x_change -= 0.5
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
    
    # Collision
    collision = isCollision(bucket_x, bucket_y, cherry_x, cherry_y)
    if collision:
        score += 1
        print(score)
        cherry_x = random.randint(87, 737)
        cherry_y = random.randint(166, 314)
    

    # score
    scoretext = myfont.render("Score {0}".format(score), 1, (0,0,0))
    screen.blit(scoretext, (7, 10))


    cherry(cherry_x, cherry_y)
    bucket(bucket_x, bucket_y)

    pygame.display.update()

