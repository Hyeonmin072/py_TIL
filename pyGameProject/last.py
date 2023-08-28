import pygame
import random
import time


pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game")


player = pygame.image.load('C:/Users/gusal/Desktop/project/png/player.png')
player_rect = player.get_rect()
player_rect.x = 0
player_rect.y = 350


effect = pygame.image.load('C:/Users/gusal/Desktop/project/png/attack.png')
effect_rect = player.get_rect()
effect_rect.x = 100
effect_rect.y = 350


enemy = pygame.image.load('C:/Users/gusal/Desktop/project/png/slime.png')
enemy_rect = enemy.get_rect()
enemy_rect.x = 500
enemy_rect.y = 450

background = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/background1.png')

clock = pygame.time.Clock()
FPS=60
running = True
mob=5

while running:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('press')
                screen.blit(effect, effect_rect)

            elif event.key == pygame.KEYUP:
                if event.key == pygame.K.SPACE:
                    print('UP')
                    
        for i in range(mob):
            
        
            
    screen.blit(background ,(0,0))
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)
    pygame.display.flip() 
    
pygame.quit()