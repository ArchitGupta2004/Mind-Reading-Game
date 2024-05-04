""" Author - ARCHIT GUPTA
       Date - 19/03/2024
       Working - Mind Reading Game
"""

import sys
import pygame
from time import sleep

binary_string = ""
numbers = [
    [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
    [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31],
    [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31],
    [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31],
    [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
]
flag = False

pygame.init()
screen = pygame.display.set_mode((1500, 800))
screen_rect = screen.get_rect()
pygame.display.set_caption("Mind Reading Game")


clock = pygame.time.Clock()

screen.fill((5, 25, 59))
# Creating logo
logo_image = pygame.image.load("images/logo.png")
logo_image_rect = logo_image.get_rect()
logo_image_rect.center = screen_rect.center
screen.blit(logo_image, logo_image_rect)
i = 0

pygame.display.flip()
sleep(2)

timetaken = 0

while True :
    screen.fill((5, 25, 59))
    
    logo_image = pygame.image.load("images/slogo.png")
    logo_image_rect = logo_image.get_rect()
    logo_image_rect.top = screen_rect.top
    logo_image_rect.centerx = screen_rect.centerx
    screen.blit(logo_image, logo_image_rect)
    
    question = pygame.font.SysFont("verdana", 50)
    question_image = question.render("Is your birthday number in this list ?", True, (255, 215, 0), (0, 0, 0))
    question_image_rect = question_image.get_rect()
    question_image_rect.top = screen_rect.top + logo_image_rect.height + 10
    screen.blit(question_image, question_image_rect)
    
    date = pygame.font.SysFont("verdana", 25)
    date_image = date.render(f"{numbers[i]}", True, (255, 215, 0), (0, 0, 0))
    date_image_rect = date_image.get_rect()
    date_image_rect.top = screen_rect.top + question_image_rect.height + logo_image_rect.height + 20
    screen.blit(date_image, date_image_rect)
    
    if timetaken >= 60 :
        yes = pygame.font.SysFont("verdana", 100)
        yes_image = yes.render("yes".upper(), True, (255, 255, 255),(0, 255, 0))
        yes_image_rect = yes_image.get_rect()
        yes_image_rect.centery = screen_rect.centery + 200
        yes_image_rect.centerx = screen_rect.centerx - 200
        screen.blit(yes_image, yes_image_rect)

        no = pygame.font.SysFont("verdana", 100)
        no_image = no.render("no".upper(), True, (255, 255, 255),(255 , 0, 0))
        no_image_rect = no_image.get_rect()
        no_image_rect.centery = screen_rect.centery + 200
        no_image_rect.centerx = screen_rect.centerx + 200
        screen.blit(no_image, no_image_rect)
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN  :
            if event.key == pygame.K_ESCAPE :
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if  yes_image_rect.collidepoint(pygame.mouse.get_pos()) :
                i += 1
                binary_string += "1"
                timetaken = 0
            elif  no_image_rect.collidepoint(pygame.mouse.get_pos()) :
                i += 1
                binary_string += "0"
                timetaken = 0
            if  i == 5 :
                flag = True
                break
            
    if  flag:
        break
                         
    pygame.display.flip()
    
    if timetaken < 60 :
        timetaken +=1
                
    clock.tick(60)
    
decimal_number =int(binary_string,2)

if  decimal_number != 0 :
    while True :
        screen.fill((5, 25, 59))
        
        answer = pygame.font.SysFont("verdana", 100)
        answer_image = answer.render(f"Your birth date is : {decimal_number}", True, (255, 215, 0), (0, 0, 0))
        answer_image_rect = answer_image.get_rect()
        answer_image_rect.center = screen_rect.center
        screen.blit(answer_image, answer_image_rect)
        
        exit = pygame.font.SysFont("verdana", 100)
        exit_image = exit.render("exit".upper(), True, (255, 255, 255),(255 , 0, 0))
        exit_image_rect = exit_image.get_rect()
        exit_image_rect.top = screen_rect.top
        exit_image_rect.right = screen_rect.right
        screen.blit(exit_image, exit_image_rect)

        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN  :
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN :
                if   exit_image_rect.collidepoint(event.pos) :
                    sys.exit()
        
        pygame.display.flip()
        
        clock.tick(60)
else :
    while True :
        screen.fill((5, 25, 59))
        
        answer = pygame.font.SysFont("verdana", 100)
        answer_image = answer.render("Invalid Inputs", True, (255, 215, 0),  (0, 0, 0))
        answer_image_rect = answer_image.get_rect()
        answer_image_rect.center = screen_rect.center
        screen.blit(answer_image, answer_image_rect)
        
        exit = pygame.font.SysFont("verdana", 100)
        exit_image = exit.render("exit".upper(), True, (255, 255, 255),(255 , 0, 0))
        exit_image_rect = exit_image.get_rect()
        exit_image_rect.top = screen_rect.top
        exit_image_rect.right = screen_rect.right
        screen.blit(exit_image, exit_image_rect)

        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN  :
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN :
                if   exit_image_rect.collidepoint(event.pos) :
                    sys.exit()
        
        pygame.display.flip()
        
        clock.tick(60)    
        