import UI
import math
import pygame
import sampler_functions

def step_count(step_num, mouse_pos, click, button):
    if click and (button[0].x <= mouse_pos[0] <= button[0].x + button[0].width) and (button[0].y <= mouse_pos[1] <= button[0].y + button[0].height):
        if mouse_pos[0] < button[0].x + button[0].width / 2 and step_num > 2:
            step_num -= 1
        if mouse_pos[0] > button[0].x + button[0].width / 2 and step_num < 12:
            step_num += 1
    return step_num

def is_being_divisor(step_number, divisors): #relativ_primes-hoz vizsgálja, hogy az adott "i" érték osztható-e bármely step_number osztójával
    for elem in divisors:
        if step_number % elem == 0:
            return False
    return True

def relative_primes(step_number):
    step_number_divisors = []
    relative_primes = []
    divisor = 2

    while divisor <= step_number:
        if step_number % divisor == 0:
            step_number_divisors.append(divisor)
        divisor += 1

    for i in range(2, step_number):
        div = is_being_divisor(i, step_number_divisors)
        if div:
            relative_primes.append(i)
    return relative_primes

def relative_prime_index(step_number, relative_prime_count_index, button, mouse_pos, click):
    relative_prime = relative_primes(step_number)
    index = relative_prime_count_index
    width = (button.width)
    height = (button.height)

    if click and (button.x <= mouse_pos[0] <= button.x + width) and (button.y <= mouse_pos[1] <= button.y + height):
        if mouse_pos[0] < button.x + width / 2 and index > 0:
            index -= 1

        if mouse_pos[0] > button.x + width / 2 and index < (len(relative_prime)-1):
            index += 1
            
    return index

def r_necklace_menu_button_create(width, height):
    border_width = 433
    border_height = 490

    #menü elhelyezése   
    menu_x = width
    menu_y = height
            
    #menü
    buttons = []
    width = (border_width) / 5.5
    height = (border_height) / 10

    for i in range(5): 
        button_x = menu_x + i * (width + 10)
        button_y = menu_y
        buttons.append(UI.Button(x=button_x, y=button_y, active=False, width=width, height=height, circle_indices=None))

    return buttons
    
def small_rythm_circles_button_gen(step_number, width, height):
    radius = 150
    
    #szög kiszámításához
    angle_step = 360 / step_number

    #kis kör sugár
    small_radius = 15

    #kisebb körök inicializálása
    circles = []
    for i in range(step_number):
        #szög átváltása radiánra
        angle_rad = math.radians(i * angle_step - 90)

        #kisebb kör középpontjainak koordinálása
        x = width + int(radius * math.cos(angle_rad))
        y = height + int(radius * math.sin(angle_rad))  

        circles.append(UI.Circle(x=x, y=y, active=False, radius=small_radius))
    
    return circles

def existing_small_rythm_circles(screen, circles, chosen_relative_prime, mouse_pos=None, click=False):
    dark = (94, 80, 63)
    light = (234, 224, 213)
    small_radius = 15
    
    #kisebb körök kirajzolása
    for circle in circles:
        x, y = circle.x, circle.y
        distance = math.sqrt((circle.x - mouse_pos[0])**2 + (circle.y - mouse_pos[1])**2)

        active_circles = 0
        for circle2 in circles:
            if circle2.active:
                active_circles += 1

        if click and (distance <= circle.radius) and active_circles < chosen_relative_prime: #TODO: nem lehet deszelektálni
            circle.active = not circle.active  #állapot váltása
        
        #szín beállítása az aktív állapot szerint
        color = light if circle.active else dark
        pygame.draw.circle(screen, color, (x, y), small_radius)

    return 

def active_event_circle_button(circles, sampler_buttons):
    chosen_circles_indices = []
    sampler_button_index = sampler_functions.active_sampler_button(sampler_buttons)

    if sampler_button_index is not None:
        if sampler_buttons[sampler_button_index].active:
            for i, circle in enumerate(circles):
                if circle.active:
                    chosen_circles_indices.append(i)
    
        sampler_buttons[sampler_button_index].circle_indices = chosen_circles_indices

    return 

def start_button(width, height, is_playing, mouse_pos=None, click=False):
    menu_buttons = r_necklace_menu_button_create(width, height)
    start_button = menu_buttons[2]
    PLAYBACK_EVENT = pygame.USEREVENT + 1
    bpm = 360
    millis = int(1 / (bpm / 60) * 1000)

    if click and (start_button.x <= mouse_pos[0] <= start_button.x + start_button.width) and (start_button.y <= mouse_pos[1] <= start_button.y + start_button.height):
        if is_playing == False:
            pygame.time.set_timer(PLAYBACK_EVENT, millis)
        else:
            pygame.time.set_timer(PLAYBACK_EVENT, 0)
        is_playing = not is_playing

    return is_playing

def note_playing(note_count, sampler_buttons, step_number): #elkapja az eventet TODO: ha lejár a munkamenet, összefossa magát a lejátszó
    for i, button in enumerate(sampler_buttons):
        if button.file_name_text != "":
            current_note = note_count % step_number
            if current_note in button.circle_indices:
                channel = pygame.mixer.find_channel()
                #print(str(channel), current_note, i)
                channel.play(pygame.mixer.Sound(button.file_name_text))

    return note_count + 1