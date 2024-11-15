import UI

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


#MEGJAVÍTANI!!!!
def relative_prime_count(step_number, relative_prime_count_index, mouse_pos, click, button):
    relative_prime = relative_primes(step_number)
    index = relative_prime_count_index
    width = (button.width) / 5
    height = (button.height) / 10

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
    