import pygame
import rythm_nl_functions

class Button:
    def __init__(self, x, y, active, width, height, color=(94, 80, 63)):
        self.x = x
        self.y = y
        self.active = active
        self.width = width
        self.height = height
        self.color = color

class Circle:
    def __init__(self, x, y, active, radius):
        self.x = x
        self.y = y
        self.active = active
        self.radius = radius

def create_screen(): 
    screen_width = 1200
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    return screen

def sampler_position(screen, width, height, buttons): #nyomógombok rajza
    #keret
    pygame.draw.rect(screen, (94, 80, 63), ((width), (height), 290, 200), border_radius = 20, width = 3)

    for button in buttons:
        x, y = button.x, button.y

        pygame.draw.rect(screen, button.color, (x, y, 80, 80), border_radius=5)
   
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

    #fájl feltöltés text box
    upload_butt_font = pygame.font.SysFont(None, 24)
    upload_butt_texts = "Enter the file path of your music file: "

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
            
        if i == 1: #upload
            upload_sign_points = [(x + 20, y + 50), (x + 30, y + 10), (x + 40, y + 50)]
            pygame.draw.polygon(screen, (symbol_color), upload_sign_points)

            if button.active:
                pygame.draw.rect(screen, (198, 172, 143), ((x-70), (y + 70), (w + 300), (h-20)), border_radius=15)
                text_surface = upload_butt_font.render(f"{upload_butt_texts}", True, dark)
                text_rect = text_surface.get_rect(center=(x + (w + 30), y + (h + 30)))
                screen.blit(text_surface, text_rect)

            else:
                pygame.draw.rect(screen, (0, 0, 0), ((x-70), (y + 70), (w + 300), (h-20)))
                    


        if i == 2: #delete
            pygame.draw.line(screen, symbol_color, (x + 18, y + 10), (x + 40, y + 50), width=4 )  #bal felső-jobb alsó vonal
            pygame.draw.line(screen, symbol_color, (x + 18, y + 50), (x + 40, y + 10), width=4)  #bal alsó-jobb felső vonal

        

    return buttons

def rythm_circle(screen, width, height, dot_count, mouse_pos=None, click=False): #kör rajza 
    pygame.draw.circle(screen, (234, 224, 213), [(width), (height)], 150, width = 3)

    return

def rythm_necklace_menu(screen, width, height, buttons, step_input, chosen_relative_prime, mouse_pos=None, click=False):
    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)
    
    #keret méret
    border_width = 433
    border_height = 490

    # #menü elhelyezése   
    menu_x = width
    menu_y = height
            
    #szövegezése a Steps menünek
    step_menu_font = pygame.font.SysFont(None, 24)
    step_menu_texts = ["Steps", "Events", "Start", "Save"]
    step_menu_step_number = step_input
    
    #gombok megszámozása a funkciók hozzárendeléséhez
    for i, button in enumerate(buttons):
        x, y, w, h = button.x, button.y, button.width, button.height

        if click and (x <= mouse_pos[0] <= x + w) and (y <= mouse_pos[1] <= y + h):
            button.active = not button.active #állapot váltása

        pygame.draw.rect(screen, dark, (x, y, w, h), 
                        border_top_left_radius = 20 if i == 0 else 0, 
                        border_bottom_right_radius = 10, 
                        border_bottom_left_radius=10)
        if i == 0:
            text_num = rythm_nl_functions.step_count(step_menu_step_number, mouse_pos, click, button)
            pygame.draw.rect(screen, (0, 0, 0), (menu_x, menu_y + 100, border_width, border_height), border_radius = 20)      
            text_surface = step_menu_font.render(f"-   {text_num}   +", True, light)
            text_rect = text_surface.get_rect(center=(menu_x + i * (w + 10) + w / 2, menu_y + h / 2))
            screen.blit(text_surface, text_rect)

        #megjavítani!!!!!!
        elif i == 1:
                text_surface = step_menu_font.render(f"-   {chosen_relative_prime}   +", True, light)
                text_rect = text_surface.get_rect(center=(menu_x + i * (w + 10) + w / 2, menu_y + h / 2))
                screen.blit(text_surface, text_rect)
                
        else:
            text_surface = step_menu_font.render(step_menu_texts[i], True, light)
            text_rect = text_surface.get_rect(center=(menu_x + i * (w + 10) + w / 2, menu_y + h / 2))
            screen.blit(text_surface, text_rect)
   
    #keret
    pygame.draw.rect(screen, dark, (menu_x, menu_y, border_width, border_height), border_radius = 20, width = 5)
    
    return text_num


