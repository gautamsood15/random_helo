import pygame 

black = (0,0,0)
white = (255,255,255)

pygame.init()
surface = pygame.display.set_mode((800,400))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

# Function area

def helicopter(x,y,image):
    surface.blit(image, (x,y))

img = pygame.image.load('Helicopter.png')
x = 150
y = 200


#game loop


game_over = False

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    surface.fill(black)
    helicopter(x,y,img)

    pygame.display.update()

    clock.tick(60)   #means this  game will be 60 frames per sec

pygame.quit()
quit()


