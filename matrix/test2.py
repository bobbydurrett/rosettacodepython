import curses

# Characters to randomly appear in the rain sequence.
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

total_chars = len(chars)

    
stdscr = curses.initscr()

print(curses.LINES)
print(curses.COLS)

curses.noecho()
curses.curs_set(False)

stdscr.addstr(5, 5, 'Here')

import time

curses.endwin()
print('Successful')

    
