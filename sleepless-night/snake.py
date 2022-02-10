import threading
import time
import os
import keyboard
import random
os.system('cls||clear')

snake, snake_body, empty, apple="■  ", "▩  ", "□  ", "▣  "
route="r"
xyz=[7,7]
apple_xyz=[7,7]
times,apples=-1,-1

codered=[[empty]*15 for i in range(15)]
codered[xyz[0]][xyz[1]-2] = snake_body
codered[xyz[0]][xyz[1]-1] = snake_body
codered[xyz[0]][xyz[1]] = snake

snake_all=[[7,6],[7,5]]


keyboard.add_hotkey('up', lambda: change_route("u"))
keyboard.add_hotkey('down', lambda: change_route("d"))
keyboard.add_hotkey('right', lambda: change_route("r"))
keyboard.add_hotkey('left', lambda: change_route("l"))

def gen_apple():
    global apple_xyz, snake_all, apples
    if apples>=117:
        print("You win!!! Your scored points:",apples)
        exit()
    while apple_xyz in snake_all or apple_xyz == xyz:
        apple_xyz = [random.randint(2, 12), random.randint(2, 12)]
    apples+=1
    codered[apple_xyz[0]][apple_xyz[1]] = apple

def change_route(r):
    global route
    if (r == "r" and route != "l") or (r == "l" and route != "r") or (r == "u" and route != "d") or (r == "d" and route != "u"):
        route = r
def update():
    global times
    times+=1
    time.sleep(1-times/500 if times < 400 else 0.2)
    if route=="r":
        codered[xyz[0]%15][xyz[1]%15]=snake_body
        xyz[1] += 1
        if xyz != apple_xyz:
            codered[snake_all[-1][0] % 15][snake_all[-1][1] % 15] = empty
            del (snake_all[-1])
        else:
            gen_apple()
        snake_all.insert(0, [xyz[0],xyz[1]-1])
        codered[xyz[0]%15][xyz[1]%15]=snake
    if route=="l":
        codered[xyz[0]%15][xyz[1]%15]=snake_body
        xyz[1] -= 1
        if xyz != apple_xyz:
            codered[snake_all[-1][0] % 15][snake_all[-1][1] % 15] = empty
            del (snake_all[-1])
        else:
            gen_apple()
        snake_all.insert(0, [xyz[0],xyz[1]+1])
        codered[xyz[0]%15][xyz[1]%15]=snake
    if route=="u":
        codered[xyz[0] % 15][xyz[1] % 15] = snake_body
        xyz[0] -= 1
        if xyz != apple_xyz:
            codered[snake_all[-1][0] % 15][snake_all[-1][1] % 15] = empty
            del (snake_all[-1])
        else:
            gen_apple()
        snake_all.insert(0, [xyz[0]+1,xyz[1]])
        codered[xyz[0]%15][xyz[1]%15]=snake
    if route=="d":
        codered[xyz[0]%15][xyz[1]%15]=snake_body
        xyz[0] += 1
        if xyz != apple_xyz:
            codered[snake_all[-1][0] % 15][snake_all[-1][1] % 15] = empty
            del (snake_all[-1])
        else:
            gen_apple()
        snake_all.insert(0, [xyz[0]-1,xyz[1]])
        codered[xyz[0]%15][xyz[1]%15]=snake
    os.system('cls||clear')
    [print(*i, sep="") for i in codered]
    if xyz in snake_all:
        print("Oooooops :( Game over. Your scored points:", apples)
        exit()
    else:
        print("Очков набрано:", apples)
    update()

gen_apple()
threading.Thread(target=update()).start()