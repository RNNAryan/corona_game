import pygame,random,sys,math
from pygame import mixer
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Mission Sanitizer')
icon=pygame.image.load('coronavirus.png')
pygame.display.set_icon(icon)
player_img=pygame.image.load('profile (1).png')
enemy_img=pygame.image.load('coronavirus.png')
background=pygame.image.load('anonymous_hacker_computer-wallpaper-800x600.jpg') #just we have to load image
playerx=375
playery=500
playerx_change=0
playery_change=0
enemyx=[]  
enemyy=[]
enemyx_change=[]
enemyy_change=[]
bullet_img=pygame.image.load('water-droplet.png')
bulletx=0
bullety=500
bulletx_change=0
bullety_change=10
bullet_state='ready'
t=playerx
score=0
font=pygame.font.Font('freesansbold.ttf',32)   
textx=10
texty=10

y=[]
p='Score : '
er=0
pq=0
# background music edition
mixer.music.load('background.wav')   
mixer.music.play(-1)    

# creating text 'game over':
over_font=pygame.font.Font('freesansbold.ttf',64)

pp=pygame.font.Font('freesansbold.ttf',64)

# setting masked man background to display before play
masked_man_background=pygame.image.load('masked_man_background.jpg')
def player(x,y):
    screen.blit(player_img,(x,y))
def enemy(x,y):
    screen.blit(enemy_img,(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bullet_img,(x,y))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
    if distance<50:
        return True
    else:
        return False
def show_score(x,y):
    score_text=font.render(p+str(score),True,(255,255,255))
    screen.blit(score_text,(x,y))     
# creating function named game_over():
def game_over():
    over=over_font.render('Game Over',True,(255,255,255))
    screen.blit(over,(200,270))

# this function is to display something 
def message_to_screen(text,x,y,z,a,b,c):
    pp=pygame.font.Font('freesansbold.ttf',z)
    score_text=pp.render(text,True,(a,b,c))        # (a,b,c) are RGB colors......
    screen.blit(score_text,(x,y))
# this is the function in which we are gonna do pause and unpause
def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_u:
                    paused=False
        screen.fill((0,0,0))      #fills the screen as black
        message_to_screen('Game Paused',200,200,64,255,255,255)
        message_to_screen('Press "q" to quit and "u" to unpause',150,300,32,255,255,255)
        pygame.display.update()
    
    
    
def mouse_button(text,x,y,w,h,aa):
    global nn
    global emh
    mouse= pygame.mouse.get_pos()       # this command will get the position of mouse in touple format
    click=pygame.mouse.get_pressed()     # this will returns tuple (x,y,z) where x= left click,y=scroll click,z=right click
                                            # if pressed the value is 1 , if not pressed the value is 0
    if x<mouse[0]<x+w and y<mouse[1]<y+h:           # this loop is for changing color when courser is in that bounds
        pygame.draw.rect(screen,(0,255,0),[x,y,w,h])
        if click[0]==1:
            emh=aa
            nn=False
    else:
        pygame.draw.rect(screen,(238,130,238),[x,y,w,h])
    message_to_screen(text,x,y,22,0,0,0)

def easy_medium_hard():
    global er          # variable er is for using easy_medium_hard() function only once
    global emh         # this variable is for no of corona particles (based on easy,medium,hard)
    global nn          # and nn is for the below while loop
    er=1
    nn=True
    while nn:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    emh=2
                    nn=False
                elif event.key==pygame.K_m:
                    emh=4
                    nn=False
                elif event.key==pygame.K_h:
                    emh=6
                    nn=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    sys.exit()
        screen.blit(masked_man_background,(0,0))
        message_to_screen('!!! Welcome to "MISSION_SANITIZER" game !!!',50,50,30,255,0,0)
        message_to_screen('INSTRUCTIONS :- ',50,100,28,0,100,0)
        message_to_screen('hit the corona virus with sanitizer as bullet with space bar',80,140,20,0,128,0)
        message_to_screen('note that left and right arrow keys are movement keys to player',80,165,20,0,128,0)
        message_to_screen('the more you hit, the more you score',80,190,20,0,128,0)
        message_to_screen('dont let the virus to cross red line,otherwise game over',80,215,20,0,128,0)
        message_to_screen('which level do you want :- ',250,250,28,255,255,255)
        
        # calling the function for the easy,medium,hard modes of the game
        mouse_button('  EASY  ',600,300,100,25,2)
        mouse_button('  MEDIUM  ',600,340,100,25,4)
        mouse_button('  HARD  ',600,380,100,25,6)
        pygame.display.update()
        
while True:  #main game loop
    screen.fill((0,0,0))
    
    if er==0:
        easy_medium_hard()
    screen.blit(background,(0,0))
    if pq==0:
        for i in range(emh):                      # this loop initializes enemy positions (emh=no of enemy)
            enemyx.append(random.randint(0,735))  # dont confuse in pq value... only in first iteration pq=0 after that pq=1
            enemyy.append(random.randint(0,20))
            enemyx_change.append(4)
            enemyy_change.append(0)
            y.append(0)
    pq=1
    pygame.draw.rect(screen, (255,0,0), [0,400,800,2])
    #pygame.draw.line(screen, (255,0,0), (0, 400), (799,400))      #used to draw a line from {(0,400) to (799,400)}
                                                                    #    with (0,0,0) as rgb values and on screen....
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key==pygame.K_p:           # pausing condition
                pause()
            if event.key == pygame.K_LEFT:
                playerx_change=-5
            if event.key == pygame.K_RIGHT:
                playerx_change=5
            if event.key == pygame.K_SPACE:
                if bullet_state=='ready':       
                    t=playerx
                    fire_bullet(t,bullety)
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change=0
                playery_change=0  
    playerx+=playerx_change
    playery+=playery_change
    if playerx<0:
        playerx=0
    elif playerx>736:
        playerx=736
    elif playery>536:
        playery=536
    elif playery<0:
        playery=0
    for i in range(emh):
        enemyx[i]+=enemyx_change[i]
        enemyy_change[i]=0
    # Game over conditions :
    
    
    for i in range(emh):
        if enemyx[i]<0:        
            enemyx_change[i]=4+y[i]
            enemyy_change[i]=10
        elif enemyx[i]>736:
            enemyx_change[i]=-4-y[i]
            enemyy_change[i]=10
        enemyy[i]=enemyy[i]+enemyy_change[i]
            
    if bullet_state is 'fire':  
        fire_bullet(t,bullety)  
        bullety-=bullety_change 
    if bullety<=0:              
        bullet_state='ready'
        bullety=500
    for i in range(emh):
        collision=iscollision(enemyx[i],enemyy[i],t,bullety)

        if collision:  
            bullety=500
            score=score+100   
            bullet_state='ready'
            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(0,20)
            y[i]=y[i]+1
            explosion_sound=mixer.Sound('explosion.wav')
            explosion_sound.play()
    show_score(textx,texty)
    player(playerx,playery)
    for i in range(emh):
        enemy(enemyx[i],enemyy[i])
        
        
    # Game over conditions :
    
    for i in range(0,emh):
        if enemyy[i]>340:
            for j in range(0,emh):
                enemyy[j]=2000    # displacing the enemy to the out of the screen
            game_over()    # calling the fuction named game_over()
            textx=2000
            texty=2000
            font=pygame.font.Font('freesansbold.ttf',32)
            p='Your Final Score : '
            show_score(300,350)
            message_to_screen('press and hold "r" to restart',200,450,32,255,255,255)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        er=0
                        pq=0
                        playerx=375
                        playery=500
                        playerx_change=0
                        playery_change=0
                        enemyx,enemyy,enemyx_change,enemyy_change=[],[],[],[]
                        bulletx=0
                        bullety=500
                        bulletx_change=0
                        bullety_change=10
                        bullet_state='ready'
                        t=playerx
                        score=0  
                        textx=10

                        texty=10
                        y=[]
                        p='Score : '
                        pygame.display.update()

            break
    pygame.display.update()