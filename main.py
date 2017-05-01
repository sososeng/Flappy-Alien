import pygame
import sys
import time
from random import randint

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000, 800))
background_sound = pygame.mixer.Sound('sounds/music.wav')
background_sound.play()

lose_sound = pygame.mixer.Sound('sounds/lose.wav')



def score(count):
    font = pygame.font.SysFont('arial', 50)
    text = font.render("Score: "+str(count), True, (210,105,30))
    screen.blit(text, [0,0])


def replay():
    event = pygame.event.poll()
      
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        return event.key

    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
 
    return None
    

def textobj(text, font):
    textSurface = font.render(text, True, (253,72,47))
    return textSurface, textSurface.get_rect()

def msg(text):
    stext = pygame.font.SysFont('arial', 20)
    ltext = pygame.font.SysFont('arial', 150)

    titleTextSurf, titleTextRect = textobj(text, ltext)
    titleTextRect.center =  500, 400
    screen.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = textobj('Press Space to continue', stext)
    typTextRect.center =  500, (400 + 100)
    screen.blit(typTextSurf, typTextRect)
    pygame.display.update()
    time.sleep(1)

    while replay() == None:
        clock.tick()

    lose_sound.stop()
    background_sound.play()
    main()
    


    

def load_bg(name):
    image = pygame.image.load(name).convert()
    image = pygame.transform.scale(image,(1000,800))
    return image

def load_img(name):
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (100, 100))
    return image

def load_bullet(name):
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (100, 75))
    return image

def game_over():
    background_sound.stop()
    lose_sound.play()
    msg('Wasted....')

def main():
    player = load_img('one.png')
    counter = 0
    playerX = 100
    playerY = 100
    bulletX =900
    bulletY = randint(100,700)
    score_count =0
    


    images = []
    images.append(load_img('one.png'))
    images.append(load_img('two.png'))
    images.append(load_img('three.png'))
    images.append(load_img('four.png'))
    dead_img = load_img('rtwo.png')
    bullet =load_bullet('bullet.png')

    gameover = False

    bg = load_bg('background.png')



    while not gameover:
        if bulletX <= 0:
            bulletY = randint(120,700)
            bulletX =900

        screen.blit(bg,(0,0))

        event = pygame.event.poll()

        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player = images[counter]
            counter = (counter + 1) % len(images)
            playerY = playerY - 120
        else:
            player = images[counter]
            counter = (counter + 1) % len(images)
            playerY = playerY + 5

        screen.blit(player, (playerX, playerY))

        bulletX-=10
        screen.blit(bullet, (bulletX, bulletY))


        if playerY + 100 > 800 or playerY  < 0:
            screen.blit(dead_img, (playerX, playerY))
            game_over()       

        a = pygame.Rect((playerX, playerY), (100, 100))
        b = pygame.Rect((bulletX,bulletY),(100,75))

        if a.colliderect(b):
            screen.blit(dead_img, (playerX, playerY))
            game_over()

        clock.tick(60)
        score_count += 1
        score(score_count)
        pygame.display.flip()



if __name__ == '__main__':
    main()