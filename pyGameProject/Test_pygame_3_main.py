import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Test game")

clock = pygame.time.Clock()

#배경이미지
background = pygame.image.load("C:/Users/gusal/Desktop/project/pyGameProject/background.png")

#캐릭터 불러오기
character = pygame.image.load("C:/Users/gusal/Desktop/project/pyGameProject/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height

character_to_x = 0
character_speed = 5

enemy = pygame.image.load("C:/Users/gusal/Desktop/project/pyGameProject/character.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width/2)
enemy_y_pos = (screen_height / 2) - (enemy_height/2)

game_font = pygame.font.Font(None, 40)

total_time = 50

start_ticks = pygame.time.get_ticks()


to_x = 0
to_y = 0

character_speed = 0.6


running = True

while running:
    dt = clock.tick(60)
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                to_y += character_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        
    character_x_pos += character_to_x
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen.width - character_width:
        character_x_pos = screen.width - character_width
            
     character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    if character_rect.colliderect(enemy_rect):
        print('충돌')
        running = False
    
    
    #screen.fill((0,0,255))
    screen.blit(background, (0, 0 ))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
    
    timer = game_font.render(str(int(total_time-elapsed_time)), True, (255,255,255))
    
    screen.blit(timer, (10, 10))
    
    if total_time - elapsed_time <=10:
        print('타임아웃')
        running = False
        
    pygame.display.update()
    
pygame.time.delay(2000) #2초 정도 대기 후 종료
    
    
pygame.quit()