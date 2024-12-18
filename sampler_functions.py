import pygame
import UI
import os.path


def empty_sampler_button_gen(width, height):
    buttons = []

    for row in range(2):
        for col in range(3):
            x = width + 15 + col * 90
            y = height + 15 + row * 90
            buttons.append(UI.Button(x=x, y=y, active=False, width=width, height=height, circle_indices=[]))
    
    return buttons

def existing_sampler_buttons(screen, sampler_buttons, small_circle_buttons, mouse_pos=None, click=False):
    #színek
    dark = (94, 80, 63)
    middle = (198, 172, 143)
    light = (234, 224, 213)

    for i, button in enumerate(sampler_buttons):
        x, y = button.x, button.y

        #ellenőrizzük, hogy gombra kattintott-e a user
        if click and (x <= mouse_pos[0] <= (x + 80)) and (y <= mouse_pos[1] <= (y + 80)):
            for button2 in sampler_buttons:
                button2.active = False
            button.active = True


            button_index = active_sampler_button(sampler_buttons)
            if button_index is not None:
                circle_indices = sampler_buttons[button_index].circle_indices
                for circle in small_circle_buttons:
                    circle.active = False
                for j in circle_indices:
                    small_circle_buttons[j].active = True

        if button.active and button.file_name_text == "":
            button.color = light
        elif button.file_name_text != "":
            button.color = middle
        else:
            button.color = dark

def sampler_menu_button_gen(width, height):
    buttons = []
    
    menu_x = [width + 45, width +120, width + 195]
    menu_y = height + 250

    w = 60
    h = 60

    #gombok létrehozása
    for x in menu_x:
        buttons.append(UI.Button(x = x, y = menu_y, active = False, width = w, height = h))

    return buttons

def input_box_button_gen(second_sampler_menu_button):
    x = (second_sampler_menu_button.x-145)
    y = (second_sampler_menu_button.y + 120)
    w = (second_sampler_menu_button.width + 300)
    h = (second_sampler_menu_button.height-10)

    button = UI.Button(x, y, active=False, width=w, height=h)

    return button

def active_sampler_button(sampler_buttons):
    active_button_index = None

    for i, button in enumerate(sampler_buttons):
        if button.active:
            active_button_index = i
                 
    return active_button_index

def input_box(screen, input_box_button, sampler_button_index, sampler_buttons, mouse_pos=None, click=False):
    dark = (198, 172, 143)
    light = (234, 224, 213)
    x, y, w, h = input_box_button.x, input_box_button.y, input_box_button.width, input_box_button.height

    text = ""

    if sampler_button_index is not None:
        input_box_button.active = True
        text = sampler_buttons[sampler_button_index].file_name_text
    
    else:
        input_box_button.active = False

    if click and (input_box_button.x <= mouse_pos[0] <= input_box_button.x + input_box_button.width) and (input_box_button.y <= mouse_pos[1] <= input_box_button.y + (input_box_button.height )):
        input_box_button.active = True


    font = pygame.font.Font(None, 28)
    color = light if input_box_button.active else dark

    if sampler_button_index is not None and sampler_buttons[sampler_button_index].active and input_box_button.active:
        pygame.draw.rect(screen, (0, 0, 0), (x, y, w, h), border_radius=10)
        pygame.draw.rect(screen, color, (x, y, w, h), width=4, border_radius=10)
        
        if text:
            text_surface = font.render(text, True, dark)
            screen.blit(text_surface, (x+10, y+10))

    return

def active_upload_button_message(screen, sampler_menu_button):
    upload_butt_font = pygame.font.SysFont(None, 28)
    upload_butt_text = "Enter the name of your music file: "
    button = sampler_menu_button

    text_surface = upload_butt_font.render(f"{upload_butt_text}", False, (234, 224, 213))
    text_rect = text_surface.get_rect(center=(button.x + (button.width-27), button.y + (button.height + 35)))
    screen.blit(text_surface, text_rect)
                
    return upload_butt_text
        
def play_button(sampler_buttons, sampler_menu_buttons, mouse_pos=None, click=False): #TODO: pogram becrashel
    index = active_sampler_button(sampler_buttons)
    
    if index is not None:
        if click and (sampler_menu_buttons.x <= mouse_pos[0] <= sampler_menu_buttons.x + sampler_menu_buttons.width) and \
                    (sampler_menu_buttons.y <= mouse_pos[1] <= sampler_menu_buttons.y + (sampler_menu_buttons.height )) and \
                    sampler_buttons[index].active:
            if os.path.exists(sampler_buttons[index].file_name_text):
                pygame.mixer.music.load(sampler_buttons[index].file_name_text)
                pygame.mixer.music.play(loops=0)
            if not sampler_menu_buttons.active:
                pygame.mixer.music.pause()

    return

def delete_button(sampler_buttons, sampler_menu_buttons, mouse_pos=None, click=False):
    index = active_sampler_button(sampler_buttons)
    
    if index is not None:
        if click and (sampler_menu_buttons.x <= mouse_pos[0] <= sampler_menu_buttons.x + sampler_menu_buttons.width) and \
                    (sampler_menu_buttons.y <= mouse_pos[1] <= sampler_menu_buttons.y + (sampler_menu_buttons.height )) and \
                    sampler_buttons[index].active:
            sampler_buttons[index].file_name_text = ""
            sampler_buttons[index].circle_indices = None

    return