import pygame
import math

class Button:
    def __init__(self, x, y, active, width, height):
        self.x = x
        self.y = y
        self.active = active
        self.width = width
        self.height = height

def create_screen(): 
    screen_width = 1200
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    return screen

def sampler_position(screen, width, height, buttons, mouse_pos=None, click=False): #nyomógombok rajza
    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)
    
    #keret
    pygame.draw.rect(screen, (dark), ((width), (height), 290, 200), border_radius = 20, width = 3)
    
    #négyzetek kirajzolása 2 sorba, 3 oszlopba & állapot frissítése
    if not buttons:
        for row in range(2):
            for col in range(3):
                x = width + 15 + col * 90
                y = height + 15 + row * 90
                buttons.append(Button(x=x, y=y, active=False, width=width, height=height))

    for button in buttons:
        x, y = button.x, button.y

        #ellenőrizzük, hogy gombra kattintott-e a user
        if click and x <= mouse_pos[0] <= x + 80 and y <= mouse_pos[1] <= y + 80:
            button.active = not button.active

        color = light if button.active else dark
        pygame.draw.rect(screen, color, (x, y, 80, 80), border_radius=5)
    
    return buttons

def sampler_menu(screen, width, height, buttons, mouse_pos=None, click=False): #samplerhez tartozó menü
    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)
   
    #menü poz
    menu_x = [width + 45, width +120, width + 195]
    menu_y = height + 300

    #négyzetek dimenziói
    w = 60
    h = 60

    #gombok létrehozása
    if not buttons:
        for x in menu_x:
            buttons.append(Button(x = x, y = menu_y, active = False, width = w, height = h))

    #gombok megszámozása a funkciók hozzárendeléséhez
    for i, button in enumerate(buttons):
        x, y, w, h = button.x, button.y, button.width, button.height

        if click and x <= mouse_pos[0] <= (x + 60) and y <= mouse_pos[1] <= (y + 60):
            button.active = not button.active  #állapot váltása
    
        #színek beállítása az aktív állapot szerint
        box_color = light if button.active else dark
        symbol_color = dark if button.active else light
        
        pygame.draw.rect(screen, (box_color), (x, y, w, h), border_radius = 5)
        
        if i == 0: #play/pause jel
            play_sign_points = [(width+55, height+310), (width+55, height+350), (width+66, height+330)]
            pygame.draw.polygon(screen, (symbol_color), play_sign_points)
            pygame.draw.line(screen, (symbol_color), (x + 24, y + 10), (x + 24 + 11, y + 50), width = 2)
            pygame.draw.line(screen, (symbol_color), (x + 42, y + 10), (x + 42, y + 50), width = 3)
            pygame.draw.line(screen, (symbol_color), (x + 49, y + 10), (x + 49, y + 50), width = 3)
            
            #fixálni!!!!!!!
            pygame.mixer.music.load("Euk1.wav") 
            if button.active:
                pygame.mixer.music.play(loops=0)
            if not button.active:
                pygame.mixer.music.pause()

        if i == 1: #per jel
            upload_sign_points = [(x + 20, y + 50), (x + 30, y + 10), (x + 40, y + 50)]
            pygame.draw.polygon(screen, (symbol_color), upload_sign_points)

        if i == 2:
            pygame.draw.line(screen, symbol_color, (x + 20, y + 10), (x + 40, y + 50), width=5)  #bal felső-jobb alsó vonal
            pygame.draw.line(screen, symbol_color, (x + 20, y + 50), (x + 40, y + 10), width=5)  #bal alsó-jobb felső vonal

        

    return buttons

def rythm_necklace(screen, width, height, user_input, circles, mouse_pos=None, click=False): #kör rajza 
    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)
    
    #nagy kör
    radius = 150
    pygame.draw.circle(screen, light, [(width), (height)], radius, width = 3)
    
    #szög kiszámításához
    angle_step = 360 / user_input

    #kis kör sugár
    small_radius = 15

    #kisebb körök inicializálása
    if not circles:
        for i in range(user_input):
            #szög átváltása radiánra
            angle_rad = math.radians(i * angle_step - 90)

            #kisebb kör középpontjainak koordinálása
            x = width + int(radius * math.cos(angle_rad))
            y = height + int(radius * math.sin(angle_rad))  

            circles.append(Button(x=x, y=y, active=False, width=width, height=height))
    
    #kisebb körök kirajzolása
    for circle in circles:
        x, y = circle.x, circle.y

        if click and (x - small_radius <= mouse_pos[0] <= x + small_radius) and (y - small_radius <= mouse_pos[1] <= y + small_radius):
            circle.active = not circle.active  #állapot váltása
        
        #szín beállítása az aktív állapot szerint
        color = light if circle.active else dark
        pygame.draw.circle(screen, color, (x, y), small_radius)  

    return

def rythm_necklace_menu(screen, width, height, buttons, mouse_pos=None, click=False):
    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)
    
    #keret méret
    rect_w = 433
    rect_h = 490

    #menü elhelyezése   
    menu_x = width
    menu_y = height
            
    #szövegezés
    font = pygame.font.SysFont(None, 24)
    texts = ["Steps", "Events", "Start", "Save"]

    #menü
    if not buttons:
        #menü méret
        width = (rect_w) / 5
        height = (rect_h) / 10

        #gombok létrehozása
        for i in range(4): 
            button_x = menu_x + i * (width + 10)
            button_y = menu_y
            buttons.append(Button(x=button_x, y=button_y, active=False, width=width, height=height))
    
    #gombok megszámozása a funkciók hozzárendeléséhez
    for i, button in enumerate(buttons):
        x, y, w, h = button.x, button.y, button.width, button.height

        if click and (x <= mouse_pos[0] <= x + w) and (y <= mouse_pos[1] <= y + h):
            button.active = not button.active #állapot váltása
    
            #színek beállítása az aktív állapot szerint
        box_color = light if button.active else dark
        text_color = dark if button.active else light

        pygame.draw.rect(screen, box_color, (x, y, w, h), 
                        border_top_left_radius = 20 if i == 0 else 0, 
                        border_bottom_right_radius = 10, 
                        border_bottom_left_radius=10)
        
        text_surface = font.render(texts[i], True, text_color)
        text_rect = text_surface.get_rect(center=(menu_x + i * (w + 10) + w / 2, menu_y + h / 2))
        screen.blit(text_surface, text_rect)
   
    #keret
    pygame.draw.rect(screen, dark, (menu_x, menu_y, rect_w, rect_h), border_radius = 20, width = 5)
    
    return buttons


