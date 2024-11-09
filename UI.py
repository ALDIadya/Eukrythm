import pygame
import math

def create_screen(): 
    screen_width = 1200
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    return screen

def note_position(screen, width, height, buttons, mouse_pos=None, click=False): #nyomógombok rajza, ha nem aktív
    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)
    
    #keret
    pygame.draw.rect(screen, (dark), ((width), (height), 290, 200), border_radius = 20, width = 3)
    
    #négyzetek kirajzolása 2 sorba, 3 oszlopba & állapot frissítése
    for button in buttons:
        x, y = button["x"], button["y"]
        #ellenőrizzük, hogy gombra kattintott-e a user
        if click and x <= mouse_pos[0] <= x + 80 and y <= mouse_pos[1] <= y + 80:
            button["active"] = not button["active"]

        color = light if button["active"] else dark
        pygame.draw.rect(screen, color, (x, y, 80, 80), border_radius=5)
    
    return buttons

def note_menu(screen, width, height): #samplerhez tartozó menü magában
    upload_sign_points = [(width+140, height+350), (width+150, height+310), (width+160, height+350)]
    play_sign_points = [(width+55, height+310), (width+55, height+350), (width+66, height+330)]
    
    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)

    #play/pause:
    pygame.draw.rect(screen, (dark), ((width + 45), (height + 300), 60, 60), border_radius = 5)
        #play jel
    pygame.draw.polygon(screen, (light), play_sign_points)
        #per jel
    pygame.draw.line(screen, (light), ((width + 67), ((height + 310) + 42)), ((width + 67) + 11, (height + 308)), width = 3)    
        #pause jel
    pygame.draw.line(screen, (light), ((width + 85), (height + 310)), ((width + 85) + 0, (height + 310) + 40), width = 3)
    pygame.draw.line(screen, (light), ((width + 92), (height + 310)), ((width + 92) + 0, (height + 310) + 40), width = 3)
   
    #feltölt gomb:
    pygame.draw.rect(screen, (dark), ((width + 120), (height + 300), 60, 60), border_radius = 5)
        #feltölt jel
    pygame.draw.polygon(screen, (light), upload_sign_points)
    
    #töröl gomb:
    pygame.draw.rect(screen, (dark), ((width + 195), (height + 300), 60, 60), border_radius = 5)
        #bal felső saroktól jobb alsó sarokig vonal 
    pygame.draw.line(screen, (light), ((width + 215), (height + 310)), ((width + 215) + 20, (height + 310) + 40), width = 5)
        #bal alsó saroktól jobb felső sarokig
    pygame.draw.line(screen, (light), ((width + 215), ((height + 310) + 40)), ((width + 195) + 40, (height + 310)), width = 5)    
    return

def rythm_necklace(screen, width, height, user_input): #kör rajza 
    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)
    radius = 150
    
    #nagy kör
    pygame.draw.circle(screen, light, [(width), (height)], radius, width = 3)
    
    #szög kiszámításához
    angle_step = 360 / user_input

    #kis kör sugár
    small_radius = 15

    #kisebb körök rászámolása nagyra
    for i in range(user_input):
        #szög átváltása radiánra
        angle_rad = math.radians(i * angle_step - 90)

        #kisebb kör középpontjainak koordinálása
        x = width + int(radius * math.cos(angle_rad))
        y = height + int(radius * math.sin(angle_rad))    

        #kisebb körök kirajzolása
        pygame.draw.circle(screen, dark, (x, y), small_radius)

    return

def rythm_necklace_menu(screen, width, height):
    #elhelyezés
    x = (width)
    y = (height)

    #keret méret
    rect_w = 433
    rect_h = 490

    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)

    #menü méret
    w = (rect_w)/5
    h = (rect_h)/10

    #szövegezés
    font = pygame.font.SysFont(None, 24)
    texts = ["Steps", "Events", "Start", "Save"]

    #menü
    for i in range(4):
        pygame.draw.rect(screen, dark, (x + i * (w + 10), y, w, h), 
                         border_top_left_radius = 20 if i == 0 else 0, 
                         border_bottom_right_radius = 10, 
                         border_bottom_left_radius=10)
        text_surface = font.render(texts[i], True, light)
        text_rect = text_surface.get_rect(center=(x + i * (w + 10) + w / 2, y + h / 2))
        screen.blit(text_surface, text_rect)
    
    #keret
    pygame.draw.rect(screen, dark, (x, y, rect_w, rect_h), border_radius = 20, width = 5)
    
    return
