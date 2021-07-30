import random 
import pygame
from pygame.locals import *
import sys
import time
FPS = 15
SCREENWIDTH = 499*2
SCREENHEIGHT = 303*2
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

def render_background():
    bg = pygame.image.load('resources/background.jpg').convert()
    SCREEN.blit(bg,(0,0))
    
def display_score(score):
    font = pygame.font.SysFont('Chalkduster',30)
    score = font.render(f"Score: {score} ",True,(200,200,200))
    SCREEN.blit(score,(815,45))
    FPSCLOCK.tick(FPS)
    
def display_movie(movie):
    font = pygame.font.SysFont('Chalkduster',50)
    movie = font.render(f"{movie}", True,(200,200,200))
    Xoffset = SCREENWIDTH/2 - movie.get_width()/2
    Yoffset = movie.get_height()/2 + SCREENHEIGHT/2 
    X = Xoffset
    Y = SCREENHEIGHT - Yoffset
    SCREEN.blit(movie,(X,Y-100))
    FPSCLOCK.tick(FPS)

def WRONG_PRINT(movie):
    font = pygame.font.SysFont('Chalkduster',50)
    movie = font.render(f"{movie}", True,(171,0,0))
    Xoffset = SCREENWIDTH/2 - movie.get_width()/2
    Yoffset = movie.get_height()/2 + SCREENHEIGHT/2 
    X = Xoffset
    Y = SCREENHEIGHT - Yoffset
    SCREEN.blit(movie,(X,Y-100))
    FPSCLOCK.tick(FPS)

def display_live_count(bolly):
    font = pygame.font.SysFont('Chalkduster',30)
    score = font.render(f"lives: {len(bolly)}",True,(200,200,200))
    SCREEN.blit(score,(55,45))
    FPSCLOCK.tick(FPS)

def YOU_LOSE_WINDOW(scor,movie):
    font = pygame.font.SysFont('Chalkduster',90)
    score = font.render(f"YOU LOSE",True,(200,200,200))

    font1 = pygame.font.SysFont('Chalkduster',30)
    score1 = font1.render(f"You Scored: {scor}",True,(200,200,200))

    font2 = pygame.font.SysFont('Chalkduster',30)
    score2 = font2.render(f"Correct Answer: {movie}",True,(200,200,200))

    Xoffset = SCREENWIDTH/2 - score.get_width()/2
    Yoffset = score.get_height()/2 + SCREENHEIGHT/2 
    X = Xoffset
    Y = SCREENHEIGHT - Yoffset

    Xoffset = SCREENWIDTH/2 - score1.get_width()/2
    Yoffset = score1.get_height()/2 + SCREENHEIGHT/2 
    x = Xoffset
    y = SCREENHEIGHT - Yoffset

    Xoffset = SCREENWIDTH/2 - score2.get_width()/2
    Yoffset = score2.get_height()/2 + SCREENHEIGHT/2 
    x1 = Xoffset
    y1 = SCREENHEIGHT - Yoffset

    render_background()
    SCREEN.blit(score,(X,Y-70))
    SCREEN.blit(score1,(x,y+20))
    SCREEN.blit(score2,(x1,y1+50))
    FPSCLOCK.tick(FPS)

def YOU_WON():
    font = pygame.font.SysFont('Chalkduster',90)
    score = font.render(f"YOU WON",True,(200,200,200))

    Xoffset = SCREENWIDTH/2 - score.get_width()/2
    Yoffset = score.get_height()/2 + SCREENHEIGHT/2 
    X = Xoffset
    Y = SCREENHEIGHT - Yoffset
    render_background()
    SCREEN.blit(score,(X,Y-30))
    FPSCLOCK.tick(FPS)

def WELCOME_CLICK():
    sound = pygame.mixer.Sound('resources/enter.wav')
    pygame.mixer.Sound.play(sound)

def GAME_OVER():
    sound = pygame.mixer.Sound('resources/gameover.wav')
    pygame.mixer.Sound.play(sound)


def CORRECT_SOUND():
    sound = pygame.mixer.Sound('resources/pop.wav')
    pygame.mixer.Sound.play(sound)

def WON_SOUND():
    sound = pygame.mixer.Sound('resources/youwon.wav')
    pygame.mixer.Sound.play(sound)


def WRONG_SOUND():
    sound = pygame.mixer.Sound('resources/wrong.wav')
    pygame.mixer.Sound.play(sound)

def WELCOME():
    font = pygame.font.SysFont('Chalkduster',70)
    score = font.render(f"GUESS THE MOVIE",True,(200,200,200))

    font1 = pygame.font.SysFont('Chalkduster',40)
    score1 = font1.render(f"BY Rishabh Bilwal",True,(200,200,200))

    font2 = pygame.font.SysFont('Chalkduster',40)
    score2 = font2.render(f"Press Enter To Start",True,(200,200,200))


    Xoffset = SCREENWIDTH/2 - score.get_width()/2
    Yoffset = score.get_height()/2 + SCREENHEIGHT/2 
    X = Xoffset
    Y = SCREENHEIGHT - Yoffset

    Xoffset = SCREENWIDTH/2 - score2.get_width()/2
    Yoffset = score2.get_height()/2 + SCREENHEIGHT/2 
    x = Xoffset
    y = SCREENHEIGHT - Yoffset

    render_background()
    SCREEN.blit(score,(X,Y-220))
    SCREEN.blit(score1,(430,110))
    SCREEN.blit(score2,(x,y+50))
    FPSCLOCK.tick(FPS)
    
def play(comp_movie,bolly,score,hint):
    display_movie(comp_movie)
    display_live_count(bolly)
    display_score(score)
    HINT(hint)
    pygame.display.flip()

def HINT(hint):
    font = pygame.font.SysFont('Chalkduster',40)
    score = font.render(f"{hint}",True,(200,200,200))

    hintbox = pygame.image.load('resources/hintbox1.png')
    
    font1 = pygame.font.SysFont('Chalkduster',40)
    score1 = font1.render(f"Hint",True,(255,255,153))

    Xoffset = SCREENWIDTH/2 - score1.get_width()/2
    Yoffset = score1.get_height()/2 + SCREENHEIGHT/2 
    x = Xoffset
    y = SCREENHEIGHT - Yoffset


    Xoffset = SCREENWIDTH/2 - score.get_width()/2
    Yoffset = score.get_height()/2 + SCREENHEIGHT/2 
    X = Xoffset
    Y = SCREENHEIGHT - Yoffset

    SCREEN.blit(score,(X,Y+150))
    SCREEN.blit(hintbox,(0,0))
    SCREEN.blit(score1,(x,y+50))
    FPSCLOCK.tick(FPS)
 
def GAME_LOGIC(score,MOVIES):
    
    if len(MOVIES) == 0:
        YOU_WON()
        WON_SOUND()
        mainGame('you won')
    word = ' '
    ran = random.choice(MOVIES)
    hint = ran[1]
    MOVIES.remove((ran))
    bolly = ['b','o','l','l','y','w','o','o','d']
    s = list(ran[0])
    vowels = ['a','e','i','o','u',' ']
    for i in range(len(s)):
        if s[i] not in vowels:
            s[i] = '_'
    comp_movie = " ".join(s)
    render_background()
    play(comp_movie,bolly,score,hint)
    
    while len(bolly) > 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_a:
                    word = 'a'
                    
                if event.key == K_b:
                    word = 'b'

                if event.key == K_c:
                    word = 'c'
                
                if event.key == K_d:
                    word = 'd'
                
                if event.key == K_e:
                    word = 'e'
                
                if event.key == K_f:
                    word = 'f'

                if event.key == K_g:
                    word = 'g'

                if event.key == K_h:
                    word = 'h'

                if event.key == K_i:
                    word = 'i'

                if event.key == K_j:
                    word = 'j'

                if event.key == K_k:
                    word = 'k'

                if event.key == K_l:
                    word = 'l'

                if event.key == K_m:
                    word = 'm'

                if event.key == K_n:
                    word = 'n'

                if event.key == K_o:
                    word = 'o'

                if event.key == K_p:
                    word = 'p'

                if event.key == K_q:
                    word = 'q'
                
                if event.key == K_r:
                    word = 'r'
                
                if event.key == K_s:
                    word = 's'
                
                if event.key == K_t:
                    word = 't'
                
                if event.key == K_u:
                    word = 'u'

                if event.key == K_v:
                    word = 'v'
                
                if event.key == K_w:
                    word = 'w'

                if event.key == K_x:
                    word = 'x'

                if event.key == K_y:
                    word = 'y'

                if event.key == K_z:
                    word = 'z'
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            
            if word in ['a','e','i','o','u',' ']:
                #vowel entered error
                continue
            elif word in ran[0]:
                CORRECT_SOUND()
                arr = list(ran[0])
                for i in range(len(arr)):
                    if word == arr[i]:
                        s[i] = arr[i]
                        comp_movie = " ".join(s)
                        render_background()
                        play(comp_movie,bolly,score,hint)
                            
                    if s == arr:
                        score += 1
                        # congrats window
                        GAME_LOGIC(score,MOVIES)
                        break  
                word = ' '      
                
            else:
                bolly.pop()
                render_background()
                WRONG_SOUND()
                WRONG_PRINT(comp_movie)
                display_live_count(bolly)
                HINT(hint)
                display_score(score)
                pygame.display.flip()

                time.sleep(1)
                render_background()
                play(comp_movie,bolly,score,hint)
                word = ' '

        if len(bolly) == 0:
            GAME_OVER()
            YOU_LOSE_WINDOW(score,ran[0])
            mainGame('you lose')
                
def mainGame(evnt):
    while True:
        if evnt == 'you lose':
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_RETURN:
                        WELCOME_CLICK()
                        mainGame('start')
                        

                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.flip()
        
        elif evnt == 'you won':
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_RETURN:
                        WELCOME_CLICK()
                        mainGame('start')
                        

                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                YOU_WON()
                pygame.display.flip()
               
        else:
            WELCOME()
            MOVIES_dict = {'rocket singh':'Ranbir Kapoor','dangal':'Aamir Khan','war':'Hrithik Roshan','kesari':'Akshay kumar','raees':'Shah Rukh Khan','baaghi':'Tiger Shroff','diwale':'Shah Rukh Khan','padmavat':'Ranveer Singh','sholay':'Amitabh Bachchan','kabir singh':'shahid Kapoor','sanju':'Ranbir Kapoor','raazi':'Alia bhatt','kaabil':'Hrithik Roshan','dabangg':'Salman Khan'}
            MOVIES = []
            for i in range(7):
                movie = random.choice(list(MOVIES_dict.items()))
                MOVIES_dict.pop(movie[0])
                MOVIES.append(movie)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_RETURN:
                        score = 0
                        render_background()
                        display_score(score)
                        WELCOME_CLICK()
                        GAME_LOGIC(score,MOVIES)
                        

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
        
if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("GUESS THE MOVIE BY RISHABH BILWAL")
    mainGame('start')
