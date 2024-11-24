import UI
import pygame
import rythm_nl_functions
import sampler_functions
import save_load

def main():

    pygame.init()
    pygame.mixer.init()
    
    PLAYBACK_EVENT = pygame.USEREVENT + 1

    is_playing = False
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

    step_number = 3
    relative_prime_count_index = 0
    note_count = 0
    
    rythm_nl_menu_buttons = rythm_nl_functions.r_necklace_menu_button_create(width=rnm_width, height=rnm_height) 
    relative_primes = []
    small_circle_buttons = rythm_nl_functions.small_rythm_circles_button_gen(step_number=step_number, width = crcl_width, height=crcl_height)
    
    sampler_buttons = sampler_functions.empty_sampler_button_gen(width=rect_width, height=rect_height)
    sampler_menu_buttons = sampler_functions.sampler_menu_button_gen(width=rect_width, height=rect_height)
    input_box_button = sampler_functions.input_box_button_gen(second_sampler_menu_button=sampler_menu_buttons[1])
    last_sampler_button_index = None 
    
    while run:
        mouse_pos = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pattern = True
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

            if event.type == PLAYBACK_EVENT:
                note_count = rythm_nl_functions.note_playing(note_count=note_count, sampler_buttons=sampler_buttons, step_number=step_number)
                        
            #sampler-hez tartozó dolgok
            rythm_nl_functions.active_event_circle_button(circles=small_circle_buttons, sampler_buttons=sampler_buttons)
            sampler_functions.existing_sampler_buttons(screen, sampler_buttons=sampler_buttons, small_circle_buttons=small_circle_buttons, mouse_pos=mouse_pos, click=click)
            sampler_button_index = sampler_functions.active_sampler_button(sampler_buttons)
            UI.sampler_menu(screen, width = rect_width, height = rect_height, menu_buttons = sampler_menu_buttons, sampler_buttons=sampler_buttons, input_box_button=input_box_button, sampler_button_index=sampler_button_index, mouse_pos=mouse_pos, click=click)
            UI.sampler_position(screen, rect_width, rect_height, sampler_buttons)
            sampler_functions.play_button(sampler_buttons=sampler_buttons, sampler_menu_buttons=sampler_menu_buttons[0], mouse_pos=mouse_pos, click=click)
            sampler_functions.delete_button(sampler_buttons=sampler_buttons, sampler_menu_buttons=sampler_menu_buttons[2], mouse_pos=mouse_pos, click=click)

            if sampler_button_index is not None and sampler_menu_buttons[1].active:
                sampler_functions.input_box(screen, input_box_button=input_box_button, sampler_buttons=sampler_buttons, sampler_button_index=sampler_button_index, mouse_pos=mouse_pos, click=click)

            if event.type == pygame.KEYDOWN and input_box_button.active:
                index = sampler_button_index #így rövidebb
                text = sampler_buttons[index].file_name_text

                if sampler_buttons[index].file_name_text != "":
                    text = sampler_buttons[index].file_name_text

                if event.key == pygame.K_RETURN:
                    pass

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    sampler_functions.input_box(screen, input_box_button=input_box_button, sampler_buttons=sampler_buttons, sampler_button_index=sampler_button_index, mouse_pos=mouse_pos, click=click)
                
                else:
                    text += event.unicode
                    
                if last_sampler_button_index != sampler_button_index:
                    last_sampler_button_index = sampler_button_index
                    input_box_button.active = False
                    input_box_button.active = True

                sampler_buttons[index].file_name_text = text
                
            
            #rythm neckklace-hez tartozó dolgok
            
            if click and (rythm_nl_menu_buttons[0].x <= mouse_pos[0] <= rythm_nl_menu_buttons[0].x + rythm_nl_menu_buttons[0].width) and (rythm_nl_menu_buttons[0].y <= mouse_pos[1] <= rythm_nl_menu_buttons[0].y + rythm_nl_menu_buttons[0].height):
                if mouse_pos[0] < rythm_nl_menu_buttons[0].x + rythm_nl_menu_buttons[0].width / 2 and step_number > 2:
                    step_number -= 1
                    small_circle_buttons = rythm_nl_functions.small_rythm_circles_button_gen(step_number=step_number, width = crcl_width, height=crcl_height)
                    
                if mouse_pos[0] > rythm_nl_menu_buttons[0].x + rythm_nl_menu_buttons[0].width / 2 and step_number < 12:
                    step_number += 1
                    small_circle_buttons = rythm_nl_functions.small_rythm_circles_button_gen(step_number=step_number, width = crcl_width, height=crcl_height)
            
            #save button
            if click and (rythm_nl_menu_buttons[3].x <= mouse_pos[0] <= rythm_nl_menu_buttons[3].x + rythm_nl_menu_buttons[3].width) and (rythm_nl_menu_buttons[3].y <= mouse_pos[1] <= rythm_nl_menu_buttons[3].y + rythm_nl_menu_buttons[3].height):
                save_load.save_button(sampler_buttons=sampler_buttons, step_number=step_number)
            
            #load button
            if click and (rythm_nl_menu_buttons[4].x <= mouse_pos[0] <= rythm_nl_menu_buttons[4].x + rythm_nl_menu_buttons[4].width) and (rythm_nl_menu_buttons[4].y <= mouse_pos[1] <= rythm_nl_menu_buttons[4].y + rythm_nl_menu_buttons[4].height):
                step_number = save_load.load_button(sampler_buttons=sampler_buttons)
                small_circle_buttons = rythm_nl_functions.small_rythm_circles_button_gen(step_number=step_number, width = crcl_width, height=crcl_height)
            
            #start button
            if click and (rythm_nl_menu_buttons[2].x <= mouse_pos[0] <= rythm_nl_menu_buttons[2].x + rythm_nl_menu_buttons[2].width) and (rythm_nl_menu_buttons[2].y <= mouse_pos[1] <= rythm_nl_menu_buttons[2].y + rythm_nl_menu_buttons[2].height):
                is_playing = rythm_nl_functions.start_button(width=rnm_width, height=rnm_height, is_playing=is_playing, mouse_pos=mouse_pos, click=click)
            

            relative_primes = rythm_nl_functions.relative_primes(step_number=step_number)
            relative_prime_count_index = rythm_nl_functions.relative_prime_index(step_number=step_number, button=rythm_nl_menu_buttons[1], relative_prime_count_index=relative_prime_count_index, mouse_pos=mouse_pos, click=click)
            
            if relative_prime_count_index > len(relative_primes):
                relative_prime_count_index = 0
            
            chosen_relative_prime = relative_primes[relative_prime_count_index]

            UI.rythm_necklace_menu(screen, width = rnm_width, height = rnm_height, buttons = rythm_nl_menu_buttons, mouse_pos = mouse_pos, click = click, step_input=step_number, chosen_relative_prime = chosen_relative_prime)

            UI.rythm_circle(screen, width = crcl_width, height = crcl_height)
            rythm_nl_functions.existing_small_rythm_circles(screen, circles=small_circle_buttons, mouse_pos=mouse_pos, click=click)
            


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
