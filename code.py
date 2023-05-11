import math
import random
import pygame
from pygame import mixer

mixer.init()
pygame.init()

mixer.music.load('Goblin_-_Stay_With_Me_Melody4Arab.Com.mp3')      #any song or music of your choice
mixer.music.play(-1)

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('space shooter')
bg=pygame.image.load('bg2.jpg')
fg=pygame.image.load('2.png')

kg=[]
alienX=[]
alienY=[]
alienspeedX=[]
alienspeedY=[]

noofaliens=6

for i in range(noofaliens):
 kg.append(pygame.image.load('spaceshipenemy1.png'))
 alienspeedX.append(-1)
 alienspeedY.append(40)
 alienX.append(random.randint(0,736))
 alienY.append(random.randint(30,150))

score=0

bulletimg=pygame.image.load('bullet.png')
check=False
bulletX=390
bulletY=409

spaceshipX=370
spaceshipY=480
changeX=0
running=True
font=pygame.font.SysFont('ARIAL',32,'bold')

def scoretext():
    img=font.render(f'score:{score}',True,'white')
    screen.blit(img,(10,10))

fontgameover=pygame.font.SysFont('ARIAL',32,'bold')

def gameover():
    imggameover=fontgameover.render('game over',32,'white')
    screen.blit(imggameover,(200,250))

while running:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeX=-2
            if event.key==pygame.K_RIGHT:
                changeX=2
            if event.key==pygame.K_SPACE:
               if check is False:
                check=True
                bulletX=spaceshipX+16

        if event.type==pygame.KEYUP:
            changeX=0
    spaceshipX+=changeX
    if spaceshipX<=0:
        spaceshipX=0
    elif spaceshipX>=736:
        spaceshipX=736
   
    for i in range(noofaliens):
        if alienY[i]>420:
            for j in range(noofaliens):
              alienY[j]=2000
            gameover()
            break
        alienX[i]+=alienspeedX[i]
        if alienX[i]<=0:
            alienspeedX[i]=0.5
            alienY[i]+=alienspeedY[i]
        if alienX[i]>=736:
            alienspeedX[i]=-0.5
            alienY[i]+=alienspeedY[i]
        distance=math.sqrt(math.pow(bulletX-alienX[i],2)+math.pow(bulletY-alienY[i],2))
        if distance<27:
            bulletY=480
            check=False
            alienX[i]=random.randint(0,736)
            alienY[i]=random.randint(30,150)
            score+=1
        screen.blit(kg[i],(alienX[i],alienY[i]))
        
    if bulletY<=0:
        bulletY=409
        check=False
    if check:
       screen.blit(bulletimg,(bulletX,bulletY))
       bulletY-=2


    screen.blit(fg,(spaceshipX,spaceshipY))
    scoretext()

    pygame.display.update()



