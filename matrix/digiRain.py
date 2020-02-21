from curses import *
from random import *

"""

Based on C ncurses version

http://rosettacode.org/wiki/Matrix_Digital_Rain#NCURSES_version

"""

try:
    # Characters to randomly appear in the rain sequence.
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    total_chars = len(chars)
    
    stdscr = initscr()
    noecho()
    curs_set(False)
    
    start_color()
    init_pair(1, COLOR_GREEN, COLOR_BLACK)
    stdscr.attron(color_pair(1))
    
    #max_x = 0
    #max_y = 0
     
    max_x = 80
    max_y = 24
     
    #getmaxyx(stdscr, max_y, max_x)
     
    # Create arrays of columns based on screen width.
    
    # Array containing the current row of each column.
    
    columns_row = []
    
    # Array containing the active status of each column.
    # A column draws characters on a row when active.
    
    columns_active = []
    
    for i in range(max_x):
        columns_row.append(-1)
        columns_active.append(0)

    for i in range(max_x):
        if columns_row[i] == -1:
            # If a column is at the top row, pick a
            # random starting row and active status.
            columns_row[i] = randrange(0, max_y)
            columns_active[i] = randrange(0, 1)
 
    # Loop through columns and draw characters on rows

    for i in range(max_x):
        if columns_active[i] == 1:
            # Draw a random character at this column's current row.
            char_index = randrange(0, total_chars)
            #mvprintw(columns_row[i], i, "%c", chars[char_index])
            stdscr.addstr(columns_row[i], i, chars[char_index])
        else:
            # Draw an empty character if the column is inactive.
            #mvprintw(columns_row[i], i, " ");
            stdscr.addstr(columns_row[i], i, " ");
 
        columns_row[i]+=1
 
        # When a column reaches the bottom row, reset to top.
        if columns_row[i] >= max_y:
            columns_row[i] = -1

        # Randomly alternate the column's active status.
        if randrange(0, 1000) == 0:
            if columns_active[i] == 0:      
                columns_active[i] = 1
            else:
                columns_active[i] = 0
 
        #usleep(ROW_DELAY)
        stdscr.refresh()
    
except Exception as err:
    endwin()
    print('Exception: '+str(err))
    raise err

endwin()
print('Successful')

    
