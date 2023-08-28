import pygame

pygame.init()

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("GAME")

clock =pygame.time.Clock()

background = pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/background.png')
player =pygame.image.load('C:/Users/gusal/Desktop/project/pyGameProject/player.png')
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = (screen_width/2) - (player_width/2)
player_y_pos = (screen_height - player_height/2)

running = True

while running :
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(player, (player_x_pos, player_y_pos))
    screen.blit(background, (0,0))
    pygame.display.update()