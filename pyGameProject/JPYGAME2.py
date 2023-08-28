import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((360, 720))

clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont(None, 72)
pygame.display.set_caption("GAME")
background = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/background.png') # 배경 이미지 로딩

#플레이어 
player = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/player.png') # 플레이어 이미지 로딩
player_rect = player.get_rect()
player_rect.x = screen.get_width()/2 - 25
player_rect.y = 660
player_speed = 15

#적
enemy = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/enemy.png')
enemy_rect = enemy.get_rect()
enemy_rect.x = random.randint(0,screen.get_width() - player_rect.width)
enemy_rect.y = 0
enemy_speed = 10

#총알
bullet = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/bullet.png')

num_enemies = 3



enemy_rects = [enemy.get_rect() for _ in range(num_enemies)]
for rect in enemy_rects:
    rect.x = random.randint(0,screen.get_width() - rect.width)
    rect.y = random.randint(-500, -rect.height)


running = True
game_over = False

game_over_text = font.render("Game Over", True, (255,0,0))
count_text = font.render("Count", True, (255,0,0))
count = 0
while running :
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
        if player_rect.x < 0:
            player_rect.x = 0
            
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
        if player_rect.x + player_rect.width > screen.get_width():
            player_rect.x = screen.get_width() - player_rect.width
        
    enemy_rect.y += enemy_speed
    
    if enemy_rect.y > screen.get_height()>=screen.get_height():
        enemy_rect.y = 0
        enemy_rect.x = random.randint(0, screen.get_width()-enemy_rect.width)
    
    for rect in enemy_rects:
        rect.y += enemy_speed
        if rect.y + rect.height >= screen.get_height():
            rect.y = -rect.height
            rect.x = random.randint(0, screen.get_width()-rect.width)
    
    
    if player_rect.colliderect(enemy_rect) and not game_over:
        game_over = True
        screen.fill((255,255,255))
        screen.blit(game_over_text,(screen.get_width()/2 - game_over_text.get_width()/2,
        screen.get_height()/2- game_over_text.get_height()/2))
        print("충돌")
        time.sleep(5)
        running = False 
        
        count +=1
        pygame.display.flip()
        print(count)
        
    if not game_over:
        screen.fill((255,255,255))
        screen.blit(background,(0,0))
        screen.blit(player, player_rect)
        screen.blit(enemy, enemy_rect)
        pygame.display.flip()