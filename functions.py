def step_count(step_num, mouse_pos, click, x, y, w, h):
    if click and (x <= mouse_pos[0] <= x + w) and (y <= mouse_pos[1] <= y + h):
        if mouse_pos[0] < x + w / 2 and step_num > 2:
            step_num -= 1
        if mouse_pos[0] > x + w / 2 and step_num < 12:
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

def relative_prime_count(step_number, mouse_pos, click, x, y, w, h):
    relative_prime = relative_primes(step_number)
    index = 0
    
    if click and (x <= mouse_pos[0] <= x + w) and (y <= mouse_pos[1] <= y + h):
        if mouse_pos[0] < x + w / 2 and step_number >= 3:
            index -= 1
        if mouse_pos[0] > x + w / 2 and step_number <= 12:
            index += 1

    if 0 <= index < len(relative_prime):
        return relative_prime[index]