import pygame

def bg_moving():
    screen.blit(bg_image,(0,bg_move))
    screen.blit(bg_image, (0,bg_move - 500))


pygame.init()
pygame.mixer.init()
pygame.display.set_caption(":::car_game_2d:::")
screen_height = 500
screen_width = 600
player_left = -180
player_right = 180
player_x_movement = 0
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
bg_move = 0
player = pygame.image.load("car_image.png").convert_alpha()
player_rect = player.get_rect(center = (250,350))
bg_image = pygame.image.load("road.png").convert()


pygame.mouse.set_visible(False)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x_movement += player_left 
            
        if keys[pygame.K_RIGHT]:
            player_x_movement += player_right
    bg_move += 1
    if bg_move >= 500:
        bg_move = 0
    bg_moving()
    player_rect.centerx += player_x_movement
    if  player_rect.centerx >= 40 or player_rect.centerx <= -40:
        player_x_movement = 0
    
       
    screen.blit(player, player_rect)    
    pygame.display.update()
    clock.tick(200)
