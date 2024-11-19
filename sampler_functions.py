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

def empty_sampler_button_gen(width, height):
    buttons = []

    for row in range(2):
        for col in range(3):
            x = width + 15 + col * 90
            y = height + 15 + row * 90
            buttons.append(UI.Button(x=x, y=y, active=False, width=width, height=height))
    
    return buttons

def play_button(sampler_button, sampler_menu_button):
    if sampler_menu_button[0].active and sampler_button[0].active:
            pygame.mixer.music.play(loops=0)
    if not (sampler_menu_button[0].active and sampler_button[0].active):
            pygame.mixer.music.pause()

    return