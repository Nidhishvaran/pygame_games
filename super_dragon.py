#..................................................................imported modules................................................................
import pygame
import sys
import random
#.....................................................................functions....................................................................
def bg_moving():
    screen.blit(bg,(bg_move,0))
    screen.blit(bg,(bg_move+600,0))
    screen.blit(bg,(bg_move,0))
    screen.blit(bg,(bg_move+600,0))
    
def ad():
    screen.blit(ad_image,(ad_move,0))
    screen.blit(ad_image,(ad_move+600,0))
    screen.blit(ad_image,(ad_move,0))
    screen.blit(ad_image,(ad_move+600,0))
    
def create_obstacle():
    random_obstacle = random.choice(obstacle_random)
    obstacle_rect = obstacle_img.get_rect(center = (800 ,random_obstacle))
    return obstacle_rect

def draw_obstacle(obstacles):
    for obstacle in obstacles:
        random_speed = -5
        obstacle.centerx+=random_speed
    return obstacles

def move_obstacle(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_img,obstacle)
    return obstacles

def collision(obstacles):
      
    for obstacle in obstacles:
        #  n=screen.blit(health_3_heart,health_3_heart_rect) 
        #health_scr = 0
        if player_rect.colliderect(obstacle):
            return False
    return True

def game_over():
    screen.blit(game_over_image,(0,0))
    
def score():
    score_text = game_font.render('Score '+str(int(score_int)),True,(255 ,255,255))
    score_rect = score_text.get_rect(center = (300,29))
    screen.blit(score_text,score_rect)

def final_score():
    score_text1 = game_font.render('Your score '+str(int(score_int)), True, (100,200,255))
    score_rect_f = score_text1.get_rect(center = (300,115))
    screen.blit(score_text1,score_rect_f)
    
def create_power():
    random_power = random.choice(random_pwr)
    power_rect = power_image.get_rect(center = (800,random_power))
    return power_rect

def move_power(powers):
    for power in powers:
        screen.blit(power_image,power)
    return powers
        
def draw_power(powers):
    for power in powers:
        speeed = -5
        power.centerx += speeed
    return powers

def check_power(powers):
    for power in powers:
        if player_rect.colliderect(power):
            
            
            '''scr = score_int 
            score_int = scr +10'''
            pass
        
def health():
    if score_int<10:
        pass
        
    
    
  
    

#......................................................................variables......................................................................
pygame.init()
score_int = 0
health_3_heart = pygame.image.load("3_heart.png")
health_2_heart = pygame.image.load("2_heart.png")
health_1_heart = pygame.image.load("1_heart.png")
health_3_heart_rect = health_3_heart.get_rect(topleft = (0,0))
health_2_heart_rect = health_2_heart.get_rect(topleft = (0,10))
health_1_heart_rect = health_1_heart.get_rect(topleft = (0,0))
random_pwr = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490]
game_font = pygame.font.Font("C:/Users/hp/Videos/python games(pygame)/dragon game/Lato-Italic.ttf",40)
game_over_image = pygame.image.load("game_over.png")
active_game = True
pygame.display.set_caption(":::SUPER DRAGON:::")
obstacle_random = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490]
screen = pygame.display.set_mode((600,500))
clock = pygame.time.Clock()
ad_image = pygame.image.load("dragon_ad.png")
player_y_movement = 0
bg = pygame.image.load("bg_image.png")
bg_move = 0
ad_move = 0
player_img = pygame.image.load("player_dragon.png")
player_rect = player_img.get_rect(center = (120,100))
gravity = 0.5
obstacle_img = pygame.image.load("obstacle_image.png")
obstacle_list = []
spawn_obstacle = pygame.USEREVENT
spd = 1400
pygame.time.set_timer(spawn_obstacle,spd)
power_image = pygame.image.load("power_image..png")
power_list = []
spawn_power = pygame.USEREVENT + 1
pwrspd = 3000
pygame.time.set_timer(spawn_power,pwrspd)




#....................................................................main loop.........................................................................


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_y_movement = gravity-10
        if event.type==spawn_obstacle:
            obstacle_list.append(create_obstacle())
        '''if event.type == spawn_power:
                power_list.append(create_power())'''
                
            
    if active_game: 
          
        score_int += 0.02 
        if score_int >= 100:
            spd = 1000 
        if score_int >= 300:
            spd = 800  
        ad_move+=4
        bg_move-=2
        if bg_move<=-600:
            bg_move = 0
        bg_moving()
        
        player_y_movement += gravity
        player_rect.centery+=player_y_movement
        screen.blit(player_img,player_rect)
        if player_rect.centery<=0:
            player_y_movement = 1
        if player_rect.centery>=600:
            player_y_movement = -13
        
        #power_list = move_power(power_list)
        #draw_power(power_list)
        obstacle_list = move_obstacle(obstacle_list)
        draw_obstacle(obstacle_list)
        active_game = collision(obstacle_list)
        #check_power(power_list)
        score()
        #health()
        ad()
    else:
        game_over()
        final_score()
    
    pygame.display.update()
    clock.tick(350)
#........................................................................end............................................................................
#......................................................................details..........................................................................
#.                                           1)days required to finish:-                                                                               .
#.                                                       1 day                                                                                         .
#.                                           2)strated date:-                                                                                          .
#.                                                       09-06-2022                                                                                    .
#.                                           3)ended date:-                                                                                            .
#.                                                        09-06-2022                                                                                             .
#.                                                                                                                                                     .
#.                                                                                                                                                     .
#.                                                                                                                                                     .
#.                                                                                                                                                     .
#.                                                                                                                                                     .
#.......................................................................................................................................................