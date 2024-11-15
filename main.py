import UI
import pygame
import functions

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

    note_buttons = []
    circles = []
    rythm_nl_buttons = functions.r_necklace_button_create(width=rect_width, height=rect_height) 
    sampler_buttons = []
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
            
            relative_prime_count_index = functions.relative_prime_count(step_input, relative_prime_count_index, mouse_pos, click, sampler_buttons[1])
            UI.sampler_position(screen, rect_width, rect_height, note_buttons, mouse_pos, click)
            new_step_num = UI.rythm_necklace_menu(screen, width = rnm_width, height = rnm_height, buttons = rythm_nl_buttons, mouse_pos = mouse_pos, click = click, step_input=step_input, relative_prime_count_index = relative_prime_count_index)
            step_input = new_step_num
            UI.rythm_necklace(screen, width = crcl_width, height = crcl_height, dot_count = step_input, mouse_pos = mouse_pos, click = click)
            UI.sampler_menu(screen, width = rect_width, height = rect_height, buttons = sampler_buttons, mouse_pos=mouse_pos, click=click)
               


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
