import pygame
import time
from random import randint

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 43
imageWidth = 100

pygame.init()
surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()
img = pygame.image.load('Helicopter.png')




# Function area






def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, green, [x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface, green, [x_block,y_block+block_height+gap,block_width,surfaceHeight])


def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    
    return None



def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()



def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth/2 , surfaceHeight/2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = surfaceWidth/2 , ((surfaceHeight/2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()
    main()
    
    
    
    
    

def gameOver():
    msgSurface('Kaboom!')   


def helicopter(x,y,image):
    surface.blit(image, (x,y))





#game loop




def main():
    x = 150
    y = 200
    y_move = 0

    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0,(surfaceHeight/2))
    gap = imageHeight * 3
    block_move = 3
    

    game_over = False

    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -8  #pushing the helicopter upwards

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 3

        y += y_move
        
                    

                    

        surface.fill(black)
        helicopter(x,y,img)
        blocks(x_block,y_block,block_width,block_height,gap)
        x_block -= block_move                       #moving the block
        
        
        
        if y > surfaceHeight-40 or y < 0:  #if helicopter flies out of the surface
            gameOver()

        if x_block < (-1*block_width):   #if block is removed form screne introduce another block
            x_block = surfaceWidth
            block_height = randint(0,(surfaceHeight/2))

        #CRASH LOGIC UPPER BLOCK

        if x + imageWidth > x_block:     #check if the x coordinate the crossing
            if x < x_block + block_width:  #chick if we are still in/before the blocks or passed it
                print('possibly within the boundaries of x upper')
                if y < block_height:      # if its within the boundaries of y
                    print('y crossover UPPER!')
                    if x - imageWidth < block_width + x_block:  #if were within the block
                        print('game over hit upper')
                        gameOver()
                
        #CRASH LOGIC LOWER BLOCK

        if x + imageWidth > x_block:    #check if the x coordinate the crossing 
            print('x crossover')

            if y + imageHeight > block_height+gap:
                print('Possible y crossover LOWER!')

                if x < block_width + x_block:
                    print('game over hit lower')
                    gameOver()
            

        pygame.display.update()
        clock.tick(60)   #means this  game will be 60 frames per sec


main()
pygame.quit()
quit()


