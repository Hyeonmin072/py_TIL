import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
FPS=60

center = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/center.png')
heightNote = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/heightNote.png')
widthNote = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/widthNote.png')
Judgement = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/Judgment.png')
Judgement2 = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/Judgment2.png')
Judgement3 = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/Judgment.png')
Judgement4 = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/Judgment2.png')
#가로 라이트
light = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/1.png')
#세로 라이트
light2 = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/2.png')

light3 = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/1.png')
#세로 라이트
light4 = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/2.png')
# 센터 80 80

center_rect = center.get_rect() # 센터 위치 정보
center_rect.x = 350
center_rect.y = 350

heightNote_rect = heightNote.get_rect() # 세로 노트 위치 정보
heightNote_rect.x = 550
heightNote_rect.y = 350

widthNote_rect = widthNote.get_rect() #가로 노트 위치 정보
widthNote_rect.x = 350
widthNote_rect.y = 550

Judgement_rect = Judgement.get_rect() #우 판정
Judgement_rect.x = 430
Judgement_rect.y = 350
light_rect = light.get_rect()
light_rect.x = 430
light_rect.y = 350

Judgement2_rect = Judgement2.get_rect() #하 판정
Judgement2_rect.x = 350
Judgement2_rect.y = 430
light2_rect = light2.get_rect()
light2_rect.x = 350
light2_rect.y = 430

Judgement3_rect = Judgement3.get_rect() #좌 판정
Judgement3_rect.x = 330
Judgement3_rect.y = 350
light3_rect = light3.get_rect()
light3_rect.x = 330
light3_rect.y = 350

Judgement4_rect = Judgement4.get_rect() #상 판정
Judgement4_rect.x = 350
Judgement4_rect.y = 330
light4_rect = light4.get_rect()
light4_rect.x = 350
light4_rect.y = 330


HP=100

running = True

while running :
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("윗키 입력")
            screen.blit(light3, light3_rect)
            pygame.display.flip()
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            print("윗키 해제")
            # screen.blit(Judgement4,Judgement4_rect)
        
        
    
    
    
    
    
    
    screen.fill((255,255,255))
    screen.blit(center,center_rect)
    screen.blit(heightNote,heightNote_rect)
    screen.blit(widthNote,widthNote_rect)
    screen.blit(Judgement, Judgement_rect)
    screen.blit(Judgement2, Judgement2_rect)
    screen.blit(Judgement3, Judgement3_rect)
    screen.blit(Judgement4, Judgement4_rect)
    pygame.display.flip()