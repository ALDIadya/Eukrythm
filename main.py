import UI
import pygame

def active_note_button():
    pass

def main():

    pygame.init()
    
    run = True
    pattern = False
    active = False

    clock = pygame.time.Clock()
    screen = UI.create_screen()

    crcl_width, crcl_height = 885, 310
    rnm_width, rnm_height = 670, 40

    note_buttons = []
    rect_width, rect_height = 120, 120
    for row in range(2):
        for col in range(3):
            x = rect_width + 15 + col * 90
            y = rect_height + 15 + row * 90
            note_buttons.append({"x": x, "y": y, "active": False})

    while run:
        mouse_pos = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pattern = True
                run = False
            UI.rythm_necklace(screen, crcl_width, crcl_height, 11)
            UI.note_menu(screen, rect_width, rect_height)
            UI.rythm_necklace_menu(screen, rnm_width, rnm_height)
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
            
            note_buttons = UI.note_position(screen, rect_width, rect_height, note_buttons, mouse_pos, click)
            
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
