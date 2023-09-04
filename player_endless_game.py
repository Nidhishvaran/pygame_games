#--imported-modules-
import pygame
import random

#--functions-
def bg_moving():
    screen.blit(bg_image, (bg_move,0))
    screen.blit(bg_image, (bg_move + 600,0))
    
def player_animation():
    new_player = player_frames[player_index]
    new_player_rect = new_player.get_rect(center = (140, player_rect.centery))
    return new_player, new_player_rect

def create_obstacle():
    rand_y = random.choice(rand)
    obstacle_rect = obstacle_image.get_rect(center =(800, rand_y))
    return obstacle_rect

def move_obstacle(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)
    return obstacles

def draw_obstacle(obstacles):
    for obstacle in obstacles:
        obstacle.centerx += -3
    return obstacles

def collision(obstacles):
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return False
    return True

def game_over():
    screen.blit(game_over_image, (0,0))
    
def score():
    score_image = game_font.render("Score "+str(int(score_)),True,(255,100,255))
    score_rect = score_image.get_rect(center = (300, 18))
    screen.blit(score_image, score_rect)

def your_score():
    color_text = (0,0,0)
    score_image_ = game_font_.render("Your score "+str(int(score_)), True, (color_text))
    score_image_rect = score_image_.get_rect(center = (300, 440))
    screen.blit(score_image_, score_image_rect)
    restart()
    
def restart():
    restart_image = restart_font.render("Press 'r' for restart and 'esc' for exit", True, (0,0,0))
    restart_rect = restart_image.get_rect(midbottom = (300, 50))
    screen.blit(restart_image, restart_rect)

'''def jump_animate():
    new_jump = player_jump_frame[player_jump_index]
    new_jump_rect = new_jump.get_rect(center = (140, player_rect.centery))
    return new_jump, new_jump_rect'''

#--variables-
pygame.init()
pygame.mixer.init()
#pygame.KEYDOWN.__init__()
pygame.mouse.set_visible(False)

rand = [375, 190]
bg_move = 0
active_game = True
score_ = 0 
game_font = pygame.font.Font("SF Atarian System Extended.ttf", 40)
game_font_ = pygame.font.Font("SF Atarian System Extended.ttf", 60)
restart_font = pygame.font.Font("SF Atarian System Extended.ttf", 29)
#--iported-musics-
game_over_p = pygame.mixer.Sound("game_over.mp3")
bg_music = pygame.mixer.Sound("bg_music.mp3")

#--window-settings-
icon = pygame.image.load("icon.ico")
pygame.display.set_icon(icon)
screen_width = 600
screen_height = 500
player_x_pos = 110
player_y_pos = 360
player_y_movement = 0
gravity = 0.15
fps = 200
pygame.display.set_caption("survivor_runner_2d")
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#--obstacle-
obstacle_image = pygame.image.load("rock_image.png").convert_alpha()
obstacle_list = []
SPAWN_OBSTACLE = pygame.USEREVENT + 1

pygame.time.set_timer(SPAWN_OBSTACLE,1300)
#--imported-images-
game_over_image = pygame.image.load("game_over.png").convert()
bg_image = pygame.image.load("bg_image.png").convert()

#--player-animation-
player_1 = pygame.image.load("player_image.png").convert_alpha()
player_2 = pygame.image.load("player_image_2.png").convert_alpha()
player_3 = pygame.image.load("player_image_3.png").convert_alpha()
player_4 = pygame.image.load("player_image_4.png").convert_alpha()
player_frames = [player_1, player_2, player_3, player_4]
player_index = 0
player_image = player_frames[player_index]
player_rect = player_image.get_rect(center = (player_x_pos, player_y_pos))
PLAYER_ANIMATION = pygame.USEREVENT
pygame.time.set_timer(PLAYER_ANIMATION, 90)

#--bool-
N = False
run = True

#--main-loop-
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.centery==360:
                
                '''if event.type == PLAYER_JUMP:
                    if player_jump_index < 1:
                        player_jump_index += 1
                    else:
                        player_jump_index = 0
                        
                    player_image, player_rect = jump_animate()'''
                player_y_movement = gravity - 7
                
            if event.key == pygame.K_r and active_game == False:
                obstacle_list.clear()
                player_rect.centery = player_y_pos
                score_ = 0
                active_game = True
                
            if event.key == pygame.K_ESCAPE:
                run = False
                
                
        if event.type == PLAYER_ANIMATION and N and active_game:
            if player_index < 3:
                player_index += 1
            else:
                player_index = 0
    
            player_image,player_rect = player_animation()
            
        if event.type ==  SPAWN_OBSTACLE:
            obstacle_list.append(create_obstacle())
            
     
    if active_game:
        bg_music.set_volume(0.3)
        bg_music.play()
        game_over_p.stop()
        score_ += 0.01 
        bg_move -= 3        
        bg_moving()
        if bg_move <= -600:
            bg_move = 0 
            
        player_y_movement += gravity
        player_rect.centery += player_y_movement 
        if player_rect.centery >= 360:
            player_y_movement = 0
            player_rect.centery = 360
            N = True
        else:
            N = False
        obstacle_list = move_obstacle(obstacle_list) 
        draw_obstacle(obstacle_list)   
        screen.blit(player_image, player_rect)
        active_game = collision(obstacle_list) 
        score()
        
    else:
        bg_music.stop()
        game_over_p.set_volume(0.3)
        game_over_p.play()
        
        game_over()
        your_score()     
    pygame.display.update()
    clock.tick(fps)
 