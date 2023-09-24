# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:12:15 2021

@author: Souvik Bhukta
"""

import pygame
import random
import os

pygame.init()
pygame.mixer.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
border_color=(173,255,47)
light_green=(128,232,0)
c1=(0,255,127)
c2=(255,222,173)
c3=(152,251,152)
crimpson_red=(220,20,60)

scr_width=1200
scr_height=630

game_window=pygame.display.set_mode((scr_width,scr_height))
pygame.display.set_caption("Snake By Souvik")
pygame.display.update()
clock=pygame.time.Clock()
fps=45

font1=pygame.font.SysFont('curlz', 80)
font2=pygame.font.SysFont('ravie', 40)
#font3=pygame.font.SysFont('Leelawadee UI',80)

bgimg=pygame.image.load("./snake files/final_back.jpg")
bgimg=pygame.transform.scale(bgimg,(scr_width,scr_height)).convert_alpha()

head_up=pygame.image.load("./snake files/head_up.png")
head_up=pygame.transform.scale(head_up,(80,130)).convert_alpha()

head_down=pygame.image.load("./snake files/head_down.png")
head_down=pygame.transform.scale(head_down,(80,130)).convert_alpha()

head_left=pygame.image.load("./snake files/head_left.png")
head_left=pygame.transform.scale(head_left,(130,80)).convert_alpha()

head_right=pygame.image.load("./snake files/head_right.png")
head_right=pygame.transform.scale(head_right,(130,80)).convert_alpha()

welcome_pic=pygame.image.load("./snake files/welcome_back.png")
welcome_pic=pygame.transform.scale(welcome_pic,(scr_width,scr_height)).convert_alpha()

gameover_pic=pygame.image.load("./snake files/game_over_pic.jpg")
gameover_pic=pygame.transform.scale(gameover_pic,(scr_width,scr_height)).convert_alpha()

inst=pygame.image.load("./snake files/snk_instructions.png")
inst=pygame.transform.scale(inst,(scr_width,scr_height)).convert_alpha()

snk_icon=pygame.image.load("./snake files/snake_icon.jpg")
pygame.display.set_icon(snk_icon)

head_pic=head_right

def text_screen(text,color,x,y,font):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(game_window,snk_list):
    global head_pic
    for x,y in snk_list:
       game_window.blit(head_pic,(x,y))


    
def welcome():
    pygame.mixer.music.load("./snake files/welcome.mp3")
    pygame.mixer.music.play()
    a=False
    exit_game1=False
    global temp
    temp=False
    game_window.blit(welcome_pic,(0,0))
    text_screen("Welcome To Snakes!", black, 260, 250,font1)
    text_screen("Press Space Bar To Play..", black, 260, 350,font1)
    pygame.display.update()
    
    while not exit_game1:
       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game1=True
                pygame.quit()
                
            if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        exit_game1=True
                        pygame.quit()
                        
                    if event.key==pygame.K_SPACE:
                        a=True
                    else:
                        a=False
                    if a:
                        game_window.blit(inst,(0,0))
                        pygame.display.update()
                    if event.key==pygame.K_RETURN:
                        temp=True
                        exit_game1=True
    if temp:
       pygame.mixer.music.load("./snake files/snake_moving.mp3")
       pygame.mixer.music.play()                    
       gameloop()
       
        
        
      
    
def gameloop():
    
    global head_pic
    global exit_game
    exit_game=False
    game_over=False
    a=random.randint(20,1000)
    b=random.randint(70,450)
    snake_x=a
    snake_y=b
    vel_x=0
    vel_y=0
    
    if(not os.path.exists("./snake files/snake_hiscore.txt")):
        with open("./snake files/snake_hiscore.txt","w") as f:
            f.write("0")
    
    with open("./snake files/snake_hiscore.txt","r") as f:
        hiscore=f.read()
    
    food_x=random.randint(20,1000)
    food_y=random.randint(70,450)
    t=random.randint(0,6)
    score=0
    snk_list=[]
    snk_length=1

    while not exit_game:
        
        
        if game_over:
            
            with open("./snake files/snake_hiscore.txt","w") as f:
                f.write(str(hiscore))
                
            game_window.blit(gameover_pic,(0,0))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    pygame.quit()
                if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        exit_game=True
                        pygame.quit()
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load("./snake files/snake_moving.mp3")
                        pygame.mixer.music.play()
                        pygame.display.update()
    
                        gameloop()
                        
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    
                    exit_game=True
                    pygame.quit()
                
                if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        exit_game=True
                        pygame.quit()
                    if event.key==pygame.K_RIGHT:
                        vel_x=4
                        vel_y=0
                        head_pic=head_right
                    if event.key==pygame.K_LEFT:
                        vel_x=-4
                        vel_y=0
                        head_pic=head_left
                    if event.key==pygame.K_UP:
                        vel_y=-4
                        vel_x=0
                        head_pic=head_up
                    if event.key==pygame.K_DOWN:
                        vel_y=4
                        vel_x=0
                        head_pic=head_down
            snake_x+=vel_x
            snake_y+=vel_y
            if abs(snake_x-food_x)<40 and abs(snake_y-food_y)<40:
                m=pygame.mixer.Sound("./snake files/food_eat.mp3")
                m.play()
                score+=10
                food_x=random.randint(20,1000)
                food_y=random.randint(70,450)
                t=random.randint(0,6)
                snk_length+=4
                pygame.display.update()
                
                if score>int(hiscore):
                    hiscore=score
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]
                
            if head in snk_list[:-1]:
                pygame.mixer.music.load("./snake files/snake_crash.mp3")
                pygame.mixer.music.play()
                game_over=True
            if snake_x<8 or snake_x>scr_width-150 or snake_y<60 or snake_y>500:
                pygame.mixer.music.load("./snake files/snake_crash.mp3")
                pygame.mixer.music.play()
                game_over=True
                
            if exit_game==False:
            
                game_window.blit(bgimg,(0,0))
                text_screen("Score: "+str(score)+"    Highest: "+str(hiscore),c1,20,20,font2)
                
                for i in range(30,scr_width-50):
                    pygame.draw.rect(game_window,border_color,[i,80,15,15])
                    pygame.draw.rect(game_window,border_color,[i,600,15,15])
                    
                for i in range(80,600):
                    pygame.draw.rect(game_window,border_color,[30,i,15,15])
                    pygame.draw.rect(game_window,border_color,[1150,i,15,15])
                
                plot_snake(game_window,snk_list)
                food=["./snake files/food1.png","./snake files/food2.png","./snake files/food3.png","./snake files/food4.png","./snake files/food5.png","./snake files/food6.png","./snake files/food7.png"]
                
                
                snk_food=pygame.image.load(food[t])
                snk_food=pygame.transform.scale(snk_food,(50,60)).convert_alpha()
                game_window.blit(snk_food,(food_x,food_y))
                pygame.display.update()
    clock.tick(fps)
        
        
    pygame.quit()
    
welcome()
