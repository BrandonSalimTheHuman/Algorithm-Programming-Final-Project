# import stuff
import pygame

from Settings import Settings
from Player import Player
from Collision import Collision
from Remember import RememberThisPattern
from Start import Start
from Rules import Rules
from Results import Results
from Distractions import Distractions
from Choice import Choice
import game_functions as gf


def run_game():
    # Initialize game and create screen
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Final Project")

    # Create player
    player = Player(screen)

    # load music
    pygame.mixer.init()

    # frame rate
    clock = pygame.time.Clock()

    # time set up
    time1 = 0

    # Momentary variables
    data = []
    notes = []
    invisible_notes = []
    list_of_floats = []
    list_of_invisible_floats = []
    special_notes_y = []
    distractions = []
    remember = ""
    note_count = 0

    # Set collision
    collision = Collision(screen)
    collision_counter = collision.return_counter()

    # Create text at start
    start = Start(screen)
    start.initialize_start_text()
    
    # Initialize rules
    rules = Rules(screen)

    # Initialize choice text
    choice = Choice(screen)

    # Set image switch, draw image switch and draw rect switch to False
    image_switch = False
    draw_image_switch = False
    draw_rect_switch = False

    # Main loop
    while True:
        # Redraw screen
        screen.fill(settings.bg_color)

        # for title screen
        if settings.game_state == "Start":
            # Draw button
            start.draw_start()

            # Check for inactive events
            gf.check_inactive_events(settings)

        # for rules screen
        if settings.game_state == "Rules":
            # Show rules
            rules.draw_rules()

            # Check for inactive events
            gf.check_inactive_events(settings)

        # for choice screen
        if settings.game_state == "Choice":
            # show choice
            choice.draw_text()

            # Check for inactive events
            gf.check_inactive_events(settings)

    # downtime to show the title before the song starts
        if settings.game_state == "Preparation":
            # Draw separator lines
            gf.draw_lines(screen)

            # draw collision counter
            gf.draw_counter(collision)

            # draw player
            player.blitme()

            # check for player movement
            gf.check_active_events(player)

            if settings.song == "Final Hope":
                data = gf.load("chart.txt")
                pygame.mixer.music.load("final_hope.mp3")

                # Create text
                remember = RememberThisPattern(screen)
                remember.initialize_text1()
                remember.initialize_text2()

                # Initialize distractions
                distractions = Distractions(screen)

                # Set image switch, draw image switch and draw rect switch to False
                image_switch = False
                draw_image_switch = False
                draw_rect_switch = False

                start.update_song_and_bpm("Final Hope", "220")

            if settings.song == "Cleyera":
                data = gf.load("chart2.txt")
                pygame.mixer.music.load("cleyera.mp3")
                start.update_song_and_bpm("Cleyera", "192")

            # draw the title screen
            start.draw_intro()

            note_count = 0
            notes, invisible_notes, special_notes_y, note_count = gf.load_notes(data, settings.offset, note_count,
                                                                                settings)
            list_of_floats = gf.create_float_for_note(notes)
            list_of_invisible_floats = gf.create_float_for_invisible_notes(invisible_notes)

            # read the time in the text file and get the current time
            time_tracker_file = open("time_tracker.txt", "r")
            previous_time = int(time_tracker_file.read())
            current_time = pygame.time.get_ticks()

            # check for 5 second preparation time
            if current_time - previous_time > 5000:
                # set game to active
                settings.game_state = "Active"

                # play the music
                pygame.mixer.music.play()

                # get time1
                time1 = pygame.time.get_ticks()

        # for when the game is being played
        if settings.game_state == "Active":
            # Check for active events
            gf.check_active_events(player)

            # Draw player
            player.blitme()

            # Update the chart
            time2 = pygame.time.get_ticks()
            difference = time2 - time1

            gf.update(notes, invisible_notes, difference, list_of_floats, list_of_invisible_floats, special_notes_y,
                      distractions, image_switch, settings)
            time1 = time2

            # Draw the chart
            gf.draw(screen, notes, invisible_notes)

            # Check for collision and update the counter
            collision_counter = gf.collision(player, notes, invisible_notes, list_of_floats, list_of_invisible_floats,
                                             collision_counter)
            collision.update_counter(collision_counter)

            # Draw collision counter
            gf.draw_counter(collision)

            # CHeck timer notes for Final Hope
            if settings.song == "Final Hope":
                switch, switch2, settings.game_state, image_switch, draw_image_switch, draw_rect_switch =\
                    gf.check_timer_notes(special_notes_y, settings, distractions, image_switch, draw_image_switch,
                                         draw_rect_switch)
                gf.show_text_based_on_timer_notes(switch, switch2, remember)

            # Check timer note to end song
            if settings.song == "Cleyera":
                gf.check_timer_notes_2(special_notes_y, settings)

            # Draw separator lines
            gf.draw_lines(screen)

            if settings.song == "Final Hope":
                # switch for the image
                if draw_image_switch:
                    # Draw image
                    distractions.draw_image()

                # switch for the rectangle with the screen's bg color
                if draw_rect_switch:
                    # make the player invisible
                    distractions.update_rect_center(player.rect.center)
                    distractions.draw_rect()

        # for results screen
        if settings.game_state == "Results":
            # show results
            results = Results(note_count, collision_counter, screen)
            results.draw_results()

            # check for the user to exit the game
            gf.check_inactive_events(settings)

        # Make screen visible
        pygame.display.flip()

        clock.tick(1080)


run_game()
