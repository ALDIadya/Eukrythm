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
            button.active = not button.active

        button.color = light if button.active else dark

        if i == 0:
        #ideiglenes - később módosítani
            pygame.mixer.music.load("Euk1.wav") 

    return buttons

def empty_sampler_button_gen(width, height): #TODO: ACTIVITY
    buttons = []

    for row in range(2):
        for col in range(3):
            x = width + 15 + col * 90
            y = height + 15 + row * 90
            buttons.append(UI.Button(x=x, y=y, active=False, width=width, height=height))
    
    return buttons

def input_box_button_gen(sampler_menu_button):
    x = (sampler_menu_button[1].x-145)
    y = (sampler_menu_button[1].y + 120)
    w = (sampler_menu_button[1].width + 300)
    h = (sampler_menu_button[1].height-10)

    button = UI.Button(x, y, active=False, width=w, height=h)

    return button

def active_sampler_button(sampler_buttons, mouse_pos=None, click=False):
    active_button_index = None

    for i, button in enumerate(sampler_buttons):
        if click and (button.x <= mouse_pos[0] <= button.x + button.width) and (button.y <= mouse_pos[1] <= button.y + button.height):
            button.active = not button.active
            if button.active:
                active_button_index = i
            else:
                active_button_index = None
                 
    return active_button_index

def input_box(screen, input_box_button, mouse_pos=None, click=False):
    dark = (198, 172, 143)
    light = (234, 224, 213)
    color = light if input_box_button.active else dark

    text = input_box_button.text
    font = pygame.font.Font(None, 28)
    
    if input_box_button.active:
        text_rect = pygame.draw.rect(screen, color, (input_box_button.x, input_box_button.y, input_box_button.width, input_box_button.height), width=4, border_radius=10)
        text_surface = font.render(text, True, (94, 80, 63))
        screen.blit(text_surface, text_rect)

    if click and (input_box_button.x <= mouse_pos[0] <= input_box_button.x + input_box_button.width) and (input_box_button.y <= mouse_pos[1] <= input_box_button.y + input_box_button.height):
        input_box_button.active = not input_box_button.active

    return 



def active_upload_button_message(screen, sampler_menu_button):
    upload_butt_font = pygame.font.SysFont(None, 28)
    upload_butt_text = "Enter the name of your music file: "
    button = sampler_menu_button

    text_surface = upload_butt_font.render(f"{upload_butt_text}", False, (234, 224, 213))
    text_rect = text_surface.get_rect(center=(button.x + (button.width-27), button.y + (button.height + 35)))
    screen.blit(text_surface, text_rect)
                
    return upload_butt_text
        

def play_button(sampler_button, sampler_menu_button):
    index = active_sampler_button
    
    if sampler_menu_button[0].active and sampler_button[index].active:
            pygame.mixer.music.play(loops=0)
    if not (sampler_menu_button[0].active and sampler_button[index].active):
            pygame.mixer.music.pause()

    return