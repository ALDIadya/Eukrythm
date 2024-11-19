import UI
import pygame
import rythm_nl_functions
import sampler_functions

def main():

    pygame.init()
        
    run = True
    pattern = False
    active = False

    clock = pygame.time.Clock()
    screen = UI.create_screen()
    pygame.display.set_caption("Eukrythm")

    #kezdő pozíciók koordinátái
    crcl_width, crcl_height = 885, 310
    rnm_width, rnm_height = 670, 40 #rythm necklace menu
    rect_width, rect_height = 120, 120 

    sampler_buttons = sampler_functions.empty_sampler_button_gen(width=rect_width, height=rect_height)
    rythm_nl_buttons = rythm_nl_functions.r_necklace_button_create(width=rnm_width, height=rnm_height) 
    sampler_menu_buttons = []
    relative_primes = []

    step_input = 3
    relative_prime_count_index = 0


    while run:
        mouse_pos = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pattern = True
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
            
            #sampler-hez tartozó dolgok
            sampler_buttons = sampler_functions.existing_sampler_buttons(screen, buttons=sampler_buttons, mouse_pos=mouse_pos, click=click)
            UI.sampler_menu(screen, width = rect_width, height = rect_height, buttons = sampler_menu_buttons, mouse_pos=mouse_pos, click=click)
            UI.sampler_position(screen, rect_width, rect_height, sampler_buttons)
            
            play_button = sampler_functions.play_button(sampler_button=sampler_buttons, sampler_menu_button=sampler_menu_buttons)
            

            #rythm neckklace-hez tartozó dolgok
            relative_primes = rythm_nl_functions.relative_primes(step_number=step_input)
            relative_prime_count_index = rythm_nl_functions.relative_prime_index(step_input, relative_prime_count_index, mouse_pos, click, rythm_nl_buttons[1])
            
            if relative_prime_count_index > len(relative_primes):
                relative_prime_count_index = 0
            chosen_relative_prime = relative_primes[relative_prime_count_index]

            new_step_num = UI.rythm_necklace_menu(screen, width = rnm_width, height = rnm_height, buttons = rythm_nl_buttons, mouse_pos = mouse_pos, click = click, step_input=step_input, chosen_relative_prime = chosen_relative_prime)
            step_input = new_step_num

            UI.rythm_circle(screen, width = crcl_width, height = crcl_height, dot_count = step_input, mouse_pos = mouse_pos, click = click)
            small_circles = rythm_nl_functions.small_rythm_circles(screen=screen, step_number=step_input, width = crcl_width, height=crcl_height, mouse_pos=mouse_pos, click=click)
            events_marker = rythm_nl_functions.event_marker(screen, step_number=step_input, mouse_pos=mouse_pos, click=click, circles=small_circles)
            
            


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
