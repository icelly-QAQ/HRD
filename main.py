from lib import data
from lib import tc

import tkinter as tk
import random

# 初始化地图
_map_tuple = data.create_map(11, 11)

_map_data  = data.create_map(11, 11)

map_y, map_x = data.map_size(_map_data)

item = 0

root = tk.Tk()
root.title("数字华容道")

def is_GameOver():  # 判断游戏是否胜利
    return _map_data == _map_tuple


def left_move_check(x, y):  # 左移可行性检测
    return x > 0 and _map_data[y][x - 1] == 0


def right_move_check(x, y):  # 右移可行性检测
    return x < map_x - 1 and _map_data[y][x + 1] == 0


def up_move_check(x, y):  # 上移可行性检测
    return y > 0 and _map_data[y - 1][x] == 0


def down_move_check(x, y):  # 下移可行性检测
    return y < map_y - 1 and _map_data[y + 1][x] == 0


def move_number(x, y):  # 移动函数
    global item

    if left_move_check(x, y):
        _map_data[y][x], _map_data[y][x - 1] = _map_data[y][x - 1], _map_data[y][x]
        item += 1
    elif right_move_check(x, y):
        _map_data[y][x], _map_data[y][x + 1] = _map_data[y][x + 1], _map_data[y][x]
        item += 1
    elif up_move_check(x, y):
        _map_data[y][x], _map_data[y - 1][x] = _map_data[y - 1][x], _map_data[y][x]
        item += 1
    elif down_move_check(x, y):
        _map_data[y][x], _map_data[y + 1][x] = _map_data[y + 1][x], _map_data[y][x]
        item += 1


def random_map():  # 打乱地图
    for i in range(random.randint(1000, 10000)):
        zero_x, zero_y = get_zero()
        orientation = random.randint(1, 4)
        if orientation == 1 and zero_y != 0:
            move_number(zero_x, zero_y - 1)
        elif orientation == 2 and zero_y != map_y - 1:
            move_number(zero_x, zero_y + 1)
        elif orientation == 3 and zero_x != 0:
            move_number(zero_x - 1, zero_y)
        elif orientation == 4 and zero_x != map_x - 1:
            move_number(zero_x + 1, zero_y)


def get_zero():  # 查询0（空位）所在的位置并输出
    for y in range(map_y):
        for x in range(map_x):
            if _map_data[y][x] == 0:
                return x, y


def get_user_input(info):
    for y in range(map_y):
        for x in range(map_x):
            if _map_data[y][x] == info:
                return x, y


def update_ui(buttons):  # 更新UI
    for y in range(map_y):
        for x in range(map_x):
            value = _map_data[y][x]
            if value == 0:
                buttons[y][x].config(text="", state=tk.DISABLED)
            else:
                buttons[y][x].config(text=str(value), state=tk.NORMAL)


def on_button_click(x, y, buttons):
    global item

    move_number(x, y)
    update_ui(buttons)
    fs(False)
    if is_GameOver():
        tc.i_send(str(item))


def save(x, y):  # 存档
    global item

    lib = open("./map.txt", "w")
    keys = []
    for i in range(y):
        for j in range(x):
            keysNow = (random.randint(1, 10))
            lib.write(str(_map_data[i][j] + keysNow) + '\n')
            keys.append(keysNow)
    for i in range(len(keys)):
        lib.write(str(keys[i]) + '\n')
    lib.write(str(item))
    lib.close()


def load(buttons):  # 读档
    global _map_data

    _map_data, marks = data.read_map('./map.txt', map_x, map_y)
    fs(marks == 0, marks)
    update_ui(buttons)


def fs(is_zero, now_fs = 0):
    global item
    global root

    if now_fs > 0:
        item = now_fs
    elif is_zero:
        item = 0

    fs = tk.Button(root, text=item, font=('Arial', 24), width=4, height=1)
    fs.grid(row=3, column=map_x)

    fs.config(text=str(item))


def main():
    global item
    global root

    buttons = [[None for _ in range(map_x)] for _ in range(map_x)]

    cd = tk.Button(root, text="存档", font=('Arial', 24), width=4, height=1, command=lambda: save(map_x, map_y))
    dd = tk.Button(root, text="读档", font=('Arial', 24), width=4, height=1, command=lambda: load(buttons))
    cd.grid(row=0, column=map_x)
    dd.grid(row=1, column=map_x)

    for y in range(map_y):
        for x in range(map_x):
            button = tk.Button(root, font=('Arial', 24), width=4, height=2,
                               command=lambda x=x, y=y: on_button_click(x, y, buttons))
            button.grid(row=y, column=x)
            buttons[y][x] = button

    random_map()
    fs(True)
    update_ui(buttons)

    root.mainloop()


if __name__ == "__main__":
    main()

# add to github
