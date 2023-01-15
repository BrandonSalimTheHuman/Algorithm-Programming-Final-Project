import sys

import pygame


def load(chart):
    # loads the chart
    file = open(chart, "r")
    data = file.readlines()

    return data


def load_notes(data, offset, note_count, settings):
    # create three empty arrays
    notes = []
    invisible_notes = []
    y_values_of_timer_notes = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            # append notes to the notes array
            if data[i][j] == "0" or data[i][j] == "*":
                # x = 75 + j * 130 because the empty space at the left of the screen it 75
                # and each line has a width of 130
                # j refers to the positioning of the note (which lane it is in)
                # y = ((i - len(data)) * 50) since the height of each line in the txt file s 50px
                # this is important later on for the update function
                # 50 is multiplied by (i - len(data)) because the last line in the txt file
                # should be one with the highest y value in the chart
                if settings.song == "Final Hope":
                    notes.append(pygame.Rect(75 + j * 130, ((i - len(data)) * 50) + offset, 130, 50))
                if settings.song == "Cleyera":
                    notes.append(pygame.Rect(75 + j * 130, ((i - len(data)) * 100) + offset, 130, 50))
                note_count += 1
            # notes denoted with * will be used to time events later on
            if data[i][j] == "*":
                note = ""
                if settings.song == "Final Hope":
                    note = pygame.Rect(75 + j * 130, ((i - len(data)) * 50) + offset, 130, 50)
                if settings.song == "Cleyera":
                    note = pygame.Rect(75 + j * 130, ((i - len(data)) * 100) + offset, 130, 50)
                y_value = float(note.centery)
                y_values_of_timer_notes.append(y_value)
            # append "invisible" notes to the invisible notes array
            if data[i][j] == "-":
                invisible_notes.append(pygame.Rect(75 + j * 130, ((i - len(data)) * 50) + offset, 130, 50))
                note_count += 1
    return notes, invisible_notes, y_values_of_timer_notes, note_count


def create_float_for_note(notes):
    # create an array of floats since the rect is unable to hold float values
    list_of_floats = []
    for i in range(len(notes)):
        list_of_floats.append(float(notes[i].centery))
    return list_of_floats


def create_float_for_invisible_notes(invisible_notes):
    # same thing but for the invisible notes
    list_of_invisible_floats = []
    for i in range(len(invisible_notes)):
        list_of_invisible_floats.append(float(invisible_notes[i].centery))
    return list_of_invisible_floats


def check_timer_notes(special_notes_y, settings, distractions, image_switch, draw_image_switch, draw_rect_switch):
    # this function uses notes denoted with * to check for events
    # this first switch is for the "Remember this pattern" text
    switch = False
    # the second one is for the "Keep the pattern, no matter what!" text
    switch2 = False
    # return y_value of the distraction image
    image_y = distractions.return_image_centery()
    # turn the first switch on when the first part where the pattern is used starts
    if special_notes_y[6] > 750:
        switch = True
    # turn the first switch off for the 4 bars of downtime before the pattern is used again
    if special_notes_y[5] > 750:
        switch = False
    # turn the first switch on again to give the player a second chance to remember
    if special_notes_y[4] > 750:
        switch = True
    # first switch off, second switch on to tell the player to continue the pattern
    # start moving and drawing the image
    if special_notes_y[3] > 750:
        switch = False
        switch2 = True
        image_switch = True
        draw_image_switch = True
    # stops the image from moving when it's reached a certain y value
    if image_y > 200:
        image_switch = False
    # halfway through the hardcore part, make the player invisible by drawing the rectangle
    if special_notes_y[2] > 750:
        draw_rect_switch = True
    # hardcore part ends, turn everything off
    if special_notes_y[1] > 750:
        switch2 = False
        draw_image_switch = False
        draw_rect_switch = False
    # show result screen when the chart is done
    if special_notes_y[0] > 3000:
        settings.game_state = "Results"

    return switch, switch2, settings.game_state, image_switch, draw_image_switch, draw_rect_switch


def check_timer_notes_2(special_notes_y, settings):
    if special_notes_y[0] > 3000:
        settings.game_state = "Results"


def show_text_based_on_timer_notes(switch, switch2, text):
    # uses switches from the previous function to know when to show each text
    if switch:
        text.draw_text()
    if switch2:
        text.draw_text2()


def collision(player, notes, invisible_notes, list_of_floats, list_of_invisible_floats, collision_counter):
    # check for collision and update the counter
    # for normal notes
    for note in notes:
        collide = player.rect.colliderect(note)
        if collide:
            index = notes.index(note)
            notes.remove(notes[index])
            list_of_floats.remove(list_of_floats[index])
            collision_counter += 1
    # for invisible notes
    for note in invisible_notes:
        collide = player.rect.colliderect(note)
        if collide:
            index = invisible_notes.index(note)
            invisible_notes.remove(invisible_notes[index])
            list_of_invisible_floats.remove(list_of_invisible_floats[index])
            collision_counter += 1

    return collision_counter


def update(notes, invisible_notes, difference, list_of_floats, list_of_invisible_floats, special_notes_y,
           distractions, image_switch, settings):
    # okay so for this part, the main thing I need to explain is where 1.1 comes from
    # difference is the amount of milliseconds since the last update
    # since the frames are inconsistent, and I need everything to be exact for a rhythm game
    # the amount each notes moves depends on the amount of milliseconds that have passed
    # now, to explain where the 1.1x multiplier comes from
    # the bpm of Final Hope is 220, bpm stands for "beats per minute"
    # in the txt file, one line has the length of 1/6th of a beat
    # I had to do that since the two fastest notes in the chart are quavers and quaver triplets
    # which are half or a beat and a third of a beat respectively
    # since there are 220 beats per minute, and 6 lines per beat
    # each line has the length of 1/22s, or 500/11 milliseconds
    # now, remember that each line has the height of 50px
    # this means that each note should move 50px every 500/11ms
    # which means 1px every 10/11ms
    # and finally, that means for each millisecond, the notes should move 1.1px
    for i in range(len(notes)):
        if settings.song == "Final Hope":
            list_of_floats[i] += 1.1 * difference
        if settings.song == "Cleyera":
            list_of_floats[i] += 1.28 * difference
        notes[i].centery = list_of_floats[i]

    for i in range(len(invisible_notes)):
        if settings.song == "Final Hope":
            list_of_invisible_floats[i] += 1.1 * difference
        if settings.song == "Cleyera":
            list_of_invisible_floats[i] += 1.28 * difference
        invisible_notes[i].centery = list_of_invisible_floats[i]

    for i in range(len(special_notes_y)):
        if settings.song == "Final Hope":
            special_notes_y[i] += 1.1 * difference
        if settings.song == "Cleyera":
            special_notes_y[i] += 1.28 * difference

    # move the image
    if image_switch:
        y_value = float(distractions.return_image_centery())
        y_value += 0.3 * difference
        distractions.update_image_centery(y_value)


def draw(screen, notes, invisible_notes):
    # draw all notes and invisible notes
    for note in notes:
        pygame.draw.rect(screen, (100, 0, 0), note)

    for note in invisible_notes:
        pygame.draw.rect(screen, (220, 204, 255), note)


def draw_counter(collision_class):
    collision_class.initialize_counter()
    collision_class.draw_counter()


def draw_lines(screen):
    # these five lines are for the four lanes
    pygame.draw.line(screen, (0, 0, 0), (75, 0), (75, 900))
    pygame.draw.line(screen, (0, 0, 0), (205, 0), (205, 900))
    pygame.draw.line(screen, (0, 0, 0), (335, 0), (335, 900))
    pygame.draw.line(screen, (0, 0, 0), (465, 0), (465, 900))
    pygame.draw.line(screen, (0, 0, 0), (595, 0), (595, 900))


def check_active_events(player):
    # responds to events
    for event in pygame.event.get():
        # exit the game
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # move one lane to the right
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if player.rect.centerx == 530:
                    player.rect.centerx -= 390
                else:
                    player.rect.centerx += 130
            # move one lane to the left
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if player.rect.centerx == 140:
                    player.rect.centerx += 390
                else:
                    player.rect.centerx -= 130


def check_inactive_events(settings):
    for event in pygame.event.get():
        # exit the game
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # show rules
            if settings.game_state == "Start" or settings.game_state == "Rules":
                if event.key == pygame.K_SPACE:
                    settings.game_state = "Rules"
                if event.key == pygame.K_RETURN:
                    settings.game_state = "Choice"
            if settings.game_state == "Choice":
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    time_tracker_file = open("time_tracker.txt", "w")
                    current_time = pygame.time.get_ticks()
                    time_tracker_file.write(str(current_time))
                    settings.game_state = "Preparation"
                    if event.key == pygame.K_1:
                        settings.song = "Final Hope"
                    if event.key == pygame.K_2:
                        settings.song = "Cleyera"
