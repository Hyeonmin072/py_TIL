import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((600, 600))
#윈도우의 좌표는 300x300 기준
#좌상단 끝 점은 0,0 우상단 끝 점은 300,0
#좌하단 끝 점은 0,300 우하단 끝 점은 300,30a0이 된다.

pygame.display.set_caption("Game") # 게임 이름


background = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/background.png') # 배경 이미지 로딩
player = pygame.image.load('C:/Users/gusal/Desktop/project/png/player.png') # 플레이어 이미지 로딩
player_rect = player.get_rect() # 플레이어의 위치 호출
player_rect.x = 100 # x 위치 조정
player_rect.y = 100 # y 위치 조정
player_speed = 8 # 플레이어 스피드 (x픽셀 만큼 움직이게한다)

enemy = pygame.image.load('C:/Users/gusal/Desktop/project/png/heal.png')
enemy_rect = enemy.get_rect()
enemy_rect.x = 250
enemy_rect.y = 250

# x축과 y축을 통해 사각형을 만들 때 사각형은 오른쪽 하단에 위치함
# 축이 왼쪽 상단에 존재
#
clock = pygame.time.Clock()
FPS = 60
timer = 15
run = True
font = pygame.font.Font(None,36)
count = 0

while run :
    
    dt = (clock.tick(FPS) / 1000) * 2
    timer -= dt
    if timer <= 0 :
        run = False
        print('TIME OUT !')
        screen.blit(counter,(screen.get_width()/2 - counter.get_width()/2,
        screen.get_height()/2- counter.get_height()/2))
        time.sleep(3)
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
         
#        else:
#            print(event)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
        if player_rect.x < 0:
            player_rect.x = 0
                 
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
        if player_rect.x + player_rect.width > screen.get_width():
            player_rect.x = screen.get_width() - player_rect.width
                 
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
        if player_rect.y < 0:
            player_rect.y = 0
                 
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed
        if player_rect.y + player_rect.height > screen.get_height():
            player_rect.y = screen.get_height() - player_rect.height
    
    if keys[pygame.K_SPACE]:
        print("대쉬")
        player_speed = 30
        
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            player_speed = 8
            

    if player_rect.colliderect(enemy_rect):
        print("충돌")           
        enemy_rect.y = random.randint(0, screen.get_height()-enemy_rect.height)
        enemy_rect.x = random.randint(0, screen.get_width()-enemy_rect.width)
        print(enemy_rect.y)
        print(enemy_rect.x)
        count += 1
        timer+=0.3
        print(count)
        
            
    screen.blit(background, (0,0))
    timer_text = font.render("TIME: "+str(round(timer,2))+"s",True,(0,0,0))
    counter = font.render(str(round(count,2))+"COUNT",True,(0,0,0))
    dash_text = font.render("DASH : SPACE BAR",True,(0,0,0))
    screen.blit(timer_text, (10,10))
    screen.blit(counter, (screen.get_width()/2+180,10))
    screen.blit(dash_text, (350,560))
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)
    pygame.display.flip()
         
#


pygame.quit()


