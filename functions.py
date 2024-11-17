import UI
import math
import pygame

def step_count(step_num, mouse_pos, click, button):
    if click and (button.x <= mouse_pos[0] <= button.x + button.width) and (button.y <= mouse_pos[1] <= button.y + button.height):
        if mouse_pos[0] < button.x + button.width / 2 and step_num > 2:
            step_num -= 1
        if mouse_pos[0] > button.x + button.width / 2 and step_num < 12:
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

def relative_prime_index(step_number, relative_prime_count_index, mouse_pos, click, button):
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

def r_necklace_button_create(width, height):
    border_width = 433
    border_height = 490

    #menü elhelyezése   
    menu_x = width
    menu_y = height
            
    #menü
    buttons = []
    width = (border_width) / 5
    height = (border_height) / 10

    for i in range(4): 
        button_x = menu_x + i * (width + 10)
        button_y = menu_y
        buttons.append(UI.Button(x=button_x, y=button_y, active=False, width=width, height=height))

    return buttons
    
def small_rythm_circles(screen, step_number, width, height, mouse_pos, click):
    dark = (94, 80, 63)
    light = (234, 224, 213)

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

    #kisebb körök kirajzolása
    for circle in circles:
        x, y = circle.x, circle.y

        if click and (x - small_radius <= mouse_pos[0] <= x + small_radius) and (y - small_radius <= mouse_pos[1] <= y + small_radius):
            circle.active = not circle.active  #állapot váltása
        
        #szín beállítása az aktív állapot szerint
        color = light if circle.active else dark
        pygame.draw.circle(screen, color, (x, y), small_radius)

    return circles

def event_marker(screen, step_number, mouse_pos, click, circles):
    list_counter = len(relative_primes(step_number))
    chosen_circles = [] * list_counter
    
    for circle in circles:
        if click and intersect(circle, mouse_pos):
            chosen_circles.append(circle)
            pygame.draw.circle(screen, (198, 172, 143), (circle.x, circle.y), circle.radius)

    return chosen_circles

def intersect(circle, mouse_pos):
    distance = math.sqrt((circle.x - mouse_pos[0])**2 + (circle.y - mouse_pos[1])**2)
    return distance <= circle.radius