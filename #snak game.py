#snak game

import random
import curses

screen= curses.initscr()
curses.cur_set(0)

screen_h,screen_w=screen.getmaxy()

window=curses.newwin(screen_h,screen_w,0,0)
#user can use keypoard the function can take buttons
window.keypad(1)
#sareen refrush above 100ms
window.timeout(100)
#dedect where the snake will apper
snk_x=screen_w//4
snk_y=screen_h//2
snake=[
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk_x-2]

]
#the food
#in the meddel of screen
food=[screen_h//2,screen_w//2]
#paint the char food on the coordinate
window.addch(food[0,food[1],curses.circle])

#the direction of the snake when the game start
key=curses.KEY_RIGHT

#the loop true to be alwayes run
while True:
    #what the next move by user 
    next_key=window.getch()
    #if user not enter any key
    key=key if next_key==-1  else next_key

    #
    if snake[0][0] in [0,screen_h] or snake[0][1] in [0, screen_w] or snake[0] in snake[1:]:
        
        curses.endwin()
        quit()
    new_head=[snake[0][0],snake[0],[1]]
    if key==curses.KEY_DOUN:
        new_head[0]+=1
    if key==curses.KEY_UP:
        new_head[0]-=1
    if key==curses.KEY_RIGHT:
        new_head[0]+=1
    if key==curses.KEY_LEFT:
        new_head[0]-=1
    snake.insert(0,new_head)

    if snake[0]==food:
        food =None
        while food is None:
            #initialize new food random
            nf=[
                random.randint(1,screen_h-1),random.randint(1,screen_w-1)
            ]
            food=nf if nf not in snake else None
        window.addch(food[0],food[1],curses.ACScircle)
    else:
        tail=snake.pop()
        window.addch(tail[0],tail[1],'')

    window.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)


