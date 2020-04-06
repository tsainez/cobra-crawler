#
#  main.py
#
#  Created by Anthony Sainez on 7 February 2020
#  Copyright 2020 Anthony Sainez, Xavier Ybarra, Nathan Vasquez, Apsara Fite. All rights reserved.
#

# Check out these resources
# https://docs.python.org/3/howto/curses.html
# https://www.devdungeon.com/content/curses-programming-python#toc-8
# TODO: Draw actual walls

import random
import curses
import snake
import draw

#snakeCharater = 'x'
#foodCharacter = 'f'

screen = curses.initscr()    #initialize the screen.
curses.curs_set(0)      #turn off the cursor.
sh, sw = screen.getmaxyx()   #set height and width values of screento sh, sw.
w = curses.newwin(sh, sw, 0, 0) #open a new window with the height and width of sh and sw, set the 'cursor' to zero zero.
w.keypad(1)             #turns the keypad on. Allows the function keys to be interpreted. (the arrow keys are function keys). (Values that are higher than 256 ascii)
w.timeout(100)          #pauses the program for 100ms. if the value is negative the it will timeout until the next input.

d = draw.draw(w, sh, sw)
s = snake.snake([w, sh, sw])       #gives values to snake

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), 'f')

key = curses.KEY_RIGHT  #assign key to be a KEY constant. (Should work no matter what is entered here.


def key_check(current_key, proposed_key):
    return {
        -1: current_key,
        curses.KEY_RIGHT: 1 if current_key == 1 else 3,
        curses.KEY_LEFT: 3 if current_key == 3 else 1,
        curses.KEY_DOWN: 2 if current_key == 2 else 0,
        curses.KEY_UP: 0 if current_key == 0 else 2
        }[proposed_key]

while True:
    next_key = w.getch()    #get character. if not enough delay then -1 is returned when there isno input. otherwise it waits for key to be pressed.
    key = key_check(key, next_key)

    snake = s.move(key)
    if snake == -1:
        break

    if snake[0] == food or (snake[0][0] == food[0] and snake[1][0] == food[0] and (snake[0][1] + snake[1][1]) / 2 == food[1]):
        s.feed()
        w.addch(int(food[0]), int(food[1]), ' ')
        food = None
        
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randrange(1, sw-1, 2)
            ]
            food = nf if (nf not in snake and not (snake[0][0] == nf[0] and snake[1][0] == nf[0] and (snake[0][1] + snake[1][1]) / 2 == nf[1])) else None
        d.display([food[0], food[1]], 'f')

    d.display([int(snake[0][0]), int(snake[0][1])], 'x')



d.clear()
d.type([int(sh / 2), int(sw / 2)], "Game over")
d.type([int(sh / 2) + 1, int(sw / 2)], "Score: " + str(s.size - 3) + "\n")
next_key = -1
while(next_key == -1):
    next_key = w.getch()
quit()
# Code originated from https://github.com/engineer-man/youtube/blob/master/015/snake.py
