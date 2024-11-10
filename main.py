import UI
import pygame

def main():

    pygame.init()
        
    run = True
    pattern = False
    active = False

    clock = pygame.time.Clock()
    screen = UI.create_screen()
    pygame.display.set_caption("Eukrythm")

    crcl_width, crcl_height = 885, 310
    rnm_width, rnm_height = 670, 40 #rythm necklace menu
    rect_width, rect_height = 120, 120

    note_buttons = []
    circles = []
    rythm_nl_buttons = []
    sampler_buttons = []   

    while run:
        mouse_pos = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pattern = True
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
            
            UI.sampler_position(screen, rect_width, rect_height, note_buttons, mouse_pos, click)
            UI.rythm_necklace(screen, width = crcl_width, height = crcl_height, user_input = 11, circles = circles, mouse_pos = mouse_pos, click = click)
            UI.rythm_necklace_menu(screen, width = rnm_width, height = rnm_height, buttons = rythm_nl_buttons, mouse_pos = mouse_pos, click = click)
            UI.sampler_menu(screen, width = rect_width, height = rect_height, buttons = sampler_buttons, mouse_pos=mouse_pos, click=click)
            


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
