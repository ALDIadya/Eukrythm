import pygame
import UI

def existing_sampler_buttons(screen, buttons, mouse_pos=None, click=False):
    #színek
    dark = (94, 80, 63)
    light = (234, 224, 213)

    for i, button in enumerate(buttons):
        x, y = button.x, button.y

        #ellenőrizzük, hogy gombra kattintott-e a user
        if click and (x <= mouse_pos[0] <= (x + 80)) and (y <= mouse_pos[1] <= (y + 80)):
            for button2 in (buttons):
                button2.active = False
            button.active = True
        button.button_color = light if button.active else dark

def empty_sampler_button_gen(width, height): #TODO: ACTIVITY
    buttons = []

    for row in range(2):
        for col in range(3):
            x = width + 15 + col * 90
            y = height + 15 + row * 90
            buttons.append(UI.Button(x=x, y=y, active=False, width=width, height=height))
    
    return buttons

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

def sampler_menu_button_activity(buttons, mouse_pos=None, click=False):
    dark = (94, 80, 63)
    light = (234, 224, 213)

    for i, button in enumerate(buttons):
        x, y = button.x, button.y

        if click and (x <= mouse_pos[0] <= (x + 80)) and (y <= mouse_pos[1] <= (y + 80)):
            for button2 in (buttons):
                button2.active = False
            button.active = True
        button.button_color = light if button.active else dark
        button.symbol_color = dark if button.active else light
    
    return

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
    color = light if input_box_button.active else dark
    existing_sampler_buttons(screen, sampler_buttons, mouse_pos=None, click=False)
    x, y, w, h = input_box_button.x, input_box_button.y, input_box_button.width, input_box_button.height

    text = ""
    if sampler_button_index is not None:
        text = sampler_buttons[sampler_button_index].file_name_text
            
    font = pygame.font.Font(None, 28)
    
    if click and (input_box_button.x <= mouse_pos[0] <= input_box_button.x + input_box_button.width) and (input_box_button.y <= mouse_pos[1] <= input_box_button.y + (input_box_button.height )):
        input_box_button.active = not input_box_button.active

    if sampler_button_index is not None and sampler_buttons[sampler_button_index].active and input_box_button.active:
        black_box = pygame.draw.rect(screen, (0, 0, 0), (x, y, w, h), width=4)
        text_rect = pygame.draw.rect(screen, color, (x, y, w, h), width=4, border_radius=10)
        text_surface = font.render(text, True, ((94, 80, 63)))
        screen.blit(text_surface, black_box)
        screen.blit(text_surface, text_rect)

    return 

def active_upload_button_message(screen, sampler_menu_button):
    upload_butt_font = pygame.font.SysFont(None, 28)
    upload_butt_text = "Enter the name of your music file: "
    button = sampler_menu_button

    text_surface = upload_butt_font.render(f"{upload_butt_text}", False, (234, 224, 213))
    text_rect = text_surface.get_rect(center=(button.x + (button.width-27), button.y + (button.height + 35)))
    screen.blit(text_surface, text_rect)
                
    return upload_butt_text

def play_button(sampler_button, sampler_menu_button, mouse_pos=None, click=False):
    index = active_sampler_button(sampler_button, mouse_pos, click)
    
    if sampler_menu_button[0].active and sampler_button[index].active:
            pygame.mixer.music.play(loops=0)
    if not (sampler_menu_button[0].active and sampler_button[index].active):
            pygame.mixer.music.pause()

    return

def delete_button():
    pass