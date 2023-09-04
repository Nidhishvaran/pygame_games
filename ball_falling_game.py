#-----------------------------------------------------------imported modules-----------------------------------------------------------
import pygame
import sys
import random

#---------------------------------------------------------------functions--------------------------------------------------------------


def bg_moving():
    screen.blit(bg_image,(0,bg_move))
    screen.blit(bg_image,(0,bg_move+500))
    

    
def create_obstacle():
    random_rect = random.choice(random_rect_obstacle)
    obstacle_rect = obstacle_image.get_rect( center = (random_rect, 700))
    return obstacle_rect

def move_obstacle(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)
    return obstacles

def draw_obstacle(obstacles):
    for obstacle in obstacles:
        if int(score_1)>10000:
            obstacle.centery -= 4
        obstacle.centery -= 3
    return obstacles

def collision(obstacles):
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return False
    return True
def falling_ball_ad():
    screen.blit(ad,(0, ad_move))

def game_over():
    if not active_game:
        screen.blit(game_over_image,(0,0))
    
def score():
    score_image = game_font.render("Score "+str(int(score_1)), True, (250,250,250))
    score_rect = score_image.get_rect(center = (300,18))
    screen.blit(score_image, score_rect)

def final_score():
    score_image = game_font.render("Your score "+ str(int(score_1)), True, (0,255,255))
    score_rect = score_image.get_rect(center = (300,120))
    if not active_game :
        screen.blit(score_image, score_rect)
        
def restart():
    restart_image = game_font.render("Press 'R' to restart the game!", True, (255,255,0))
    restart_rect = restart_image.get_rect(midbottom = (300,500))
    screen.blit(restart_image, restart_rect)
    
def esc():
    esc_img = game_font.render("press 'esc for quit'", True, (255,255,0))
    esc_rect = esc_img.get_rect( midbottom = (300, 460))
    screen.blit(esc_img, esc_rect)   
    
    
def create_power():
    random_rect = random.choice(random_power)
    power_rect = power_image.get_rect( center = (random_rect,800))
    return power_rect

def draw_power(powers):
    for power in powers:
        if int(score_1)>10000:
            power.centery -= 4
        power.centery -= 3
    return powers

def move_power(powers):
    for power in powers:
        n = screen.blit(power_image, power)
        n
    return powers

def power_collision(powers):
    for power in powers:
        if player_rect.colliderect(power):
            bg_music.stop()
            coin.play()
            global score_1
            score_1 += int(1)
            global n 
            n = 1
    


#----------------------------------------------------------------variables--------------------------------------------------------------
pygame.init()
pygame.mixer.init()
y_bullet = 0
icon = pygame.image.load("icon.ico")
bg_move = 0
N = True
player_x_movement = 0
right_movement = 140
left_movement = -140
random_rect_obstacle = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600]
obstacle_list = []
spawn_obstacle = pygame.USEREVENT
pygame.time.set_timer(spawn_obstacle, 1000) 
active_game = True
score_1 = 0
ad_move = 0
power_list = []
spawn_power = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_power, 5000)
random_power = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600]

#---------------------------------------------------------------game window------------------------------------------------------------
screen = pygame.display.set_mode((600, 500))
fps = pygame.time.Clock()
pygame.display.set_caption("falling ball 2d")
pygame.display.set_icon(icon)

#--------------------------------------------------------------imported images----------------------------------------------------------
bg_image = pygame.image.load('bg_image.png').convert()
player_image = pygame.image.load("player_image.png").convert_alpha()
obstacle_image = pygame.image.load("obstacle_image_1.png").convert_alpha()
game_over_image = pygame.image.load("game_over.png").convert()
ad = pygame.image.load("ad_image.png").convert()
power_image = pygame.image.load("power_image.png").convert_alpha()
bullet_image = pygame.image.load("bullet.png.png").convert_alpha()

#------------------------------------------------------------------rect----------------------------------------------------------------
player_rect = player_image.get_rect(center = (300,190))

#--------------------------------------------------------------game font---------------------------------------------------------------
game_font = pygame.font.Font("BalooBhai-Regular.ttf",37)

#--------------------------------------------------------------imported audios----------------------------------------------------------
coin = pygame.mixer.Sound("coin.mp3")
bg_music = pygame.mixer.Sound("bg_music.mp3")
game_over_mp3 = pygame.mixer.Sound("game_over.mp3")

pygame.mouse.set_visible(False)

#-----------------------------------------------------------------main loop--------------------------------------------------------------
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_x_movement += left_movement
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_x_movement += right_movement 
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
               
            
            if event.key == pygame.K_r and active_game == False:
                obstacle_list.clear()
                power_list.clear()
                score_1 = 0
                active_game = True
                player_rect.centerx = 300
                
        if event.type == spawn_obstacle:
            obstacle_list.append(create_obstacle())
            
        if event.type == spawn_power:
            power_list.append(create_power())
        
    if active_game: 
        
        y_bullet += 1
        ad_move -= 4
        game_over_mp3.stop()
        score_1 += 0.01 
        if int(score_1)>10000:
            bg_move -= 4
             
        bg_move -= 3
        if bg_move <= -500:
            bg_move = 0
        bg_moving()
        bg_music.play()
    
        #player_rect.center = pygame.mouse.get_pos()
        player_rect.centerx += player_x_movement
        if player_rect.centerx >= 40 or player_rect.centerx <= -40:
            player_x_movement = 0
        if player_rect.centerx >= 600:
            player_x_movement -= 10
        if player_rect.centerx <= 0:
            player_x_movement += 15
        screen.blit(player_image, player_rect) 
        obstacle_list = move_obstacle(obstacle_list)
        draw_obstacle(obstacle_list)
        active_game = collision(obstacle_list)
        power_list = move_power(power_list)
        draw_power(power_list)
        score()
        power_collision(power_list)
        falling_ball_ad()
        
        
    else:
        bg_music.stop()
        game_over()
        final_score()
        game_over_mp3.play()
        restart()
        esc()
        
    pygame.display.flip()
    fps.tick(100)
    