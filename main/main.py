import pyautogui as p
import numpy as np

board = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
])


def place_number(num, pos1, pos2):
    global board
    if num == one:
        board[pos2, pos1] = 1
    if num == two:
        board[pos2, pos1] = 2
    if num == three:
        board[pos2, pos1] = 3
    if num == four:
        board[pos2, pos1] = 4
    if num == five:
        board[pos2, pos1] = 5
    if num == six:
        board[pos2, pos1] = 6
    if num == seven:
        board[pos2, pos1] = 7
    if num == eight:
        board[pos2, pos1] = 8
    if num == nine:
        board[pos2, pos1] = 9



def new(num):
    for v in range(len(num)):
        row_one(num, v)
        row_two(num, v)
        row_three(num, v)
        row_four(num, v)
        row_five(num, v)
        row_six(num, v)
        row_seven(num, v)
        row_eight(num, v)
        row_nine(num, v)

def row_one(num, v):
    print(num[v])
    if 30 <= num[v][0] <= 70:
        if 160 <= num[v][1] <= 205:
            place_number(num, 0, 0)

    if 30 <= num[v][0] <= 70:
        if 215 <= num[v][1] <= 265:
            place_number(num, 0, 1)

    if 30 <= num[v][0] <= 70:
        if 270 <= num[v][1] <= 315:
            place_number(num, 0, 2)

    if 30 <= num[v][0] <= 70:
        if 325 <= num[v][1] <= 370:
            place_number(num, 0, 3)

    if 30 <= num[v][0] <= 70:
        if 375 <= num[v][1] <= 425:
            place_number(num, 0, 4)

    if 30 <= num[v][0] <= 70:
        if 430 <= num[v][1] <= 475:
            place_number(num, 0, 5)

    if 30 <= num[v][0] <= 70:
        if 485 <= num[v][1] <= 530:
            place_number(num, 0, 6)

    if 30 <= num[v][0] <= 70:
        if 540 <= num[v][1] <= 585:
            place_number(num, 0, 7)

    if 30 <= num[v][0] <= 70:
        if 590 <= num[v][1] <= 640:
            place_number(num, 0, 8)


def row_two(num, v):
    if 80 <= num[v][0] <= 130:
        if 160 <= num[v][1] <= 205:
            place_number(num, 1, 0)

    if 80 <= num[v][0] <= 130:
        if 220 <= num[v][1] <= 260:
            place_number(num, 1, 1)

    if 80 <= num[v][0] <= 130:
        if 270 <= num[v][1] <= 315:
            place_number(num, 1, 2)

    if 80 <= num[v][0] <= 130:
        if 325 <= num[v][1] <= 370:
            place_number(num, 1, 3)

    if 80 <= num[v][0] <= 130:
        if 375 <= num[v][1] <= 425:
            place_number(num, 1, 4)

    if 80 <= num[v][0] <= 130:
        if 430 <= num[v][1] <= 475:
            place_number(num, 1, 5)

    if 80 <= num[v][0] <= 130:
        if 485 <= num[v][1] <= 530:
            place_number(num, 1, 6)

    if 80 <= num[v][0] <= 130:
        if 540 <= num[v][1] <= 585:
            place_number(num, 1, 7)

    if 80 <= num[v][0] <= 130:
        if 590 <= num[v][1] <= 640:
            place_number(num, 1, 8)


def row_three(num, v):
    if 135 <= num[v][0] <= 180:
        if 160 <= num[v][1] <= 205:
            place_number(num, 2, 0)

    if 135 <= num[v][0] <= 180:
        if 220 <= num[v][1] <= 260:
            place_number(num, 2, 1)

    if 135 <= num[v][0] <= 180:
        if 270 <= num[v][1] <= 315:
            place_number(num, 2, 2)

    if 135 <= num[v][0] <= 180:
        if 325 <= num[v][1] <= 370:
            place_number(num, 2, 3)

    if 135 <= num[v][0] <= 180:
        if 375 <= num[v][1] <= 425:
            place_number(num, 2, 4)

    if 135 <= num[v][0] <= 180:
        if 430 <= num[v][1] <= 475:
            place_number(num, 2, 5)

    if 135 <= num[v][0] <= 180:
        if 485 <= num[v][1] <= 530:
            place_number(num, 2, 6)

    if 135 <= num[v][0] <= 180:
        if 540 <= num[v][1] <= 585:
            place_number(num, 2, 7)

    if 135 <= num[v][0] <= 180:
        if 590 <= num[v][1] <= 640:
            place_number(num, 2, 8)


def row_four(num, v):
    if 190 <= num[v][0] <= 235:
        if 160 <= num[v][1] <= 205:
            place_number(num, 3, 0)

    if 190 <= num[v][0] <= 235:
        if 220 <= num[v][1] <= 260:
            place_number(num, 3, 1)

    if 190 <= num[v][0] <= 235:
        if 270 <= num[v][1] <= 315:
            place_number(num, 3, 2)

    if 190 <= num[v][0] <= 235:
        if 325 <= num[v][1] <= 370:
            place_number(num, 3, 3)

    if 190 <= num[v][0] <= 235:
        if 375 <= num[v][1] <= 425:
            place_number(num, 3, 4)

    if 190 <= num[v][0] <= 235:
        if 430 <= num[v][1] <= 475:
            place_number(num, 3, 5)

    if 190 <= num[v][0] <= 235:
        if 485 <= num[v][1] <= 530:
            place_number(num, 3, 6)

    if 190 <= num[v][0] <= 235:
        if 540 <= num[v][1] <= 585:
            place_number(num, 3, 7)

    if 190 <= num[v][0] <= 235:
        if 590 <= num[v][1] <= 640:
            place_number(num, 3, 8)


def row_five(num, v):
    if 245 <= num[v][0] <= 290:
        if 160 <= num[v][1] <= 205:
            place_number(num, 4, 0)

    if 245 <= num[v][0] <= 290:
        if 220 <= num[v][1] <= 260:
            place_number(num, 4, 1)

    if 245 <= num[v][0] <= 290:
        if 270 <= num[v][1] <= 315:
            place_number(num, 4, 2)

    if 245 <= num[v][0] <= 290:
        if 325 <= num[v][1] <= 370:
            place_number(num, 4, 3)

    if 245 <= num[v][0] <= 290:
        if 375 <= num[v][1] <= 425:
            place_number(num, 4, 4)

    if 245 <= num[v][0] <= 290:
        if 430 <= num[v][1] <= 475:
            place_number(num, 4, 5)

    if 245 <= num[v][0] <= 290:
        if 485 <= num[v][1] <= 530:
            place_number(num, 4, 6)

    if 245 <= num[v][0] <= 290:
        if 540 <= num[v][1] <= 585:
            place_number(num, 4, 7)

    if 245 <= num[v][0] <= 290:
        if 590 <= num[v][1] <= 640:
            place_number(num, 4, 8)


def row_six(num, v):
    if 295 <= num[v][0] <= 345:
        if 160 <= num[v][1] <= 205:
            place_number(num, 5, 0)

    if 295 <= num[v][0] <= 345:
        if 220 <= num[v][1] <= 260:
            place_number(num, 5, 1)

    if 295 <= num[v][0] <= 345:
        if 270 <= num[v][1] <= 315:
            place_number(num, 5, 2)

    if 295 <= num[v][0] <= 345:
        if 325 <= num[v][1] <= 370:
            place_number(num, 5, 3)

    if 295 <= num[v][0] <= 345:
        if 375 <= num[v][1] <= 425:
            place_number(num, 5, 4)

    if 295 <= num[v][0] <= 345:
        if 430 <= num[v][1] <= 475:
            place_number(num, 5, 5)

    if 295 <= num[v][0] <= 345:
        if 485 <= num[v][1] <= 530:
            place_number(num, 5, 6)

    if 295 <= num[v][0] <= 345:
        if 540 <= num[v][1] <= 585:
            place_number(num, 5, 7)

    if 295 <= num[v][0] <= 345:
        if 590 <= num[v][1] <= 640:
            place_number(num, 5, 8)


def row_seven(num, v):
    if 350 <= num[v][0] <= 395:
        if 160 <= num[v][1] <= 205:
            place_number(num, 6, 0)

    if 350 <= num[v][0] <= 395:
        if 220 <= num[v][1] <= 260:
            place_number(num, 6, 1)

    if 350 <= num[v][0] <= 395:
        if 270 <= num[v][1] <= 315:
            place_number(num, 6, 2)

    if 350 <= num[v][0] <= 395:
        if 325 <= num[v][1] <= 370:
            place_number(num, 6, 3)

    if 350 <= num[v][0] <= 395:
        if 375 <= num[v][1] <= 425:
            place_number(num, 6, 4)

    if 350 <= num[v][0] <= 395:
        if 430 <= num[v][1] <= 475:
            place_number(num, 6, 5)

    if 350 <= num[v][0] <= 395:
        if 485 <= num[v][1] <= 530:
            place_number(num, 6, 6)

    if 350 <= num[v][0] <= 395:
        if 540 <= num[v][1] <= 585:
            place_number(num, 6, 7)

    if 350 <= num[v][0] <= 395:
        if 590 <= num[v][1] <= 640:
            place_number(num, 6, 8)


def row_eight(num, v):
    if 405 <= num[v][0] <= 450:
        if 160 <= num[v][1] <= 205:
            place_number(num, 7, 0)

    if 405 <= num[v][0] <= 450:
        if 220 <= num[v][1] <= 260:
            place_number(num, 7, 1)

    if 405 <= num[v][0] <= 450:
        if 270 <= num[v][1] <= 315:
            place_number(num, 7, 2)

    if 405 <= num[v][0] <= 450:
        if 325 <= num[v][1] <= 370:
            place_number(num, 7, 3)

    if 405 <= num[v][0] <= 450:
        if 375 <= num[v][1] <= 425:
            place_number(num, 7, 4)

    if 405 <= num[v][0] <= 450:
        if 430 <= num[v][1] <= 475:
            place_number(num, 7, 5)

    if 405 <= num[v][0] <= 450:
        if 485 <= num[v][1] <= 530:
            place_number(num, 7, 6)

    if 405 <= num[v][0] <= 450:
        if 540 <= num[v][1] <= 585:
            place_number(num, 7, 7)

    if 405 <= num[v][0] <= 450:
        if 590 <= num[v][1] <= 640:
            place_number(num, 7, 8)


def row_nine(num, v):
    if 455 <= num[v][0] <= 505:
        if 160 <= num[v][1] <= 205:
            place_number(num, 8, 0)

    if 455 <= num[v][0] <= 505:
        if 220 <= num[v][1] <= 260:
            place_number(num, 8, 1)

    if 455 <= num[v][0] <= 505:
        if 270 <= num[v][1] <= 315:
            place_number(num, 8, 2)

    if 455 <= num[v][0] <= 505:
        if 325 <= num[v][1] <= 370:
            place_number(num, 8, 3)

    if 455 <= num[v][0] <= 505:
        if 375 <= num[v][1] <= 425:
            place_number(num, 8, 4)

    if 455 <= num[v][0] <= 505:
        if 430 <= num[v][1] <= 475:
            place_number(num, 8, 5)

    if 455 <= num[v][0] <= 505:
        if 485 <= num[v][1] <= 530:
            place_number(num, 8, 6)

    if 455 <= num[v][0] <= 505:
        if 540 <= num[v][1] <= 585:
            place_number(num, 8, 7)

    if 455 <= num[v][0] <= 505:
        if 590 <= num[v][1] <= 640:
            place_number(num, 8, 8)


def centre(num):
    for b, item in enumerate(num):
        num[b] = p.center(num[b])

    print(num)


def solve(bo):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return i, j

    return None

def what_number(pos1, pos2):
    global board
    if board[pos2][pos1] == 1:
        p.press("1")
    if board[pos2][pos1] == 2:
        p.press("2")
    if board[pos2][pos1] == 3:
        p.press("3")
    if board[pos2][pos1] == 4:
        p.press("4")
    if board[pos2][pos1] == 5:
        p.press("5")
    if board[pos2][pos1] == 6:
        p.press("6")
    if board[pos2][pos1] == 7:
        p.press("7")
    if board[pos2][pos1] == 8:
        p.press("8")
    if board[pos2][pos1] == 9:
        p.press("9")
    p.press("right")

def reset_row():
    p.press("down")
    for i in range(8):
        p.press("left")

def draw_number(b):
    p.press("up")
    for o in range(0, len(b)):
        what_number(o, 0)
    reset_row()
    for o1 in range(0, len(b)):
        what_number(o1, 1)
    reset_row()
    for o2 in range(0, len(b)):
        what_number(o2, 2)
    reset_row()
    for o3 in range(0, len(b)):
        what_number(o3, 3)
    reset_row()
    for o4 in range(0, len(b)):
        what_number(o4, 4)
    reset_row()
    for o5 in range(0, len(b)):
        what_number(o5, 5)
    reset_row()
    for o6 in range(0, len(b)):
        what_number(o6, 6)
    reset_row()
    for o7 in range(0, len(b)):
        what_number(o7, 7)
    reset_row()
    for o8 in range(0, len(b)):
        what_number(o8, 8)



oneD = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/1D.png")
oneL = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/1L.png")
one = list(oneD) + list(oneL)
centre(one)

twoD = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/2D.png")
twoL = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/2L.png")
two = list(twoD) + list(twoL)
centre(two)

threeD = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/3D.png")
threeL = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/3L.png")
three = list(threeD) + list(threeL)
centre(three)

fourD = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/4D.png")
fourL = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/4L.png")
four = list(fourD) + list(fourL)
centre(four)

fiveD = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/5D.png")
fiveL = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/5L.png")
five = list(fiveD) + list(fiveL)
centre(five)

sixD = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/6D.png")
sixL = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/6L.png")
six = list(sixD) + list(sixL)
centre(six)

sevenD = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/7D.png")
sevenL = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/7L.png")
seven = list(sevenD) + list(sevenL)
centre(seven)

eightD = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/8D.png")
eightL = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/8L.png")
eight = list(eightD) + list(eightL)
centre(eight)

nineD = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/9D.png")
nineL = p.locateAllOnScreen("/Users/joelsmith/Desktop/Sudoku Numbers/9L.png")
nine = list(nineD) + list(nineL)
centre(nine)

new(one)
new(two)
new(three)
new(four)
new(five)
new(six)
new(seven)
new(eight)
new(nine)
print_board(board)
print("")
print("Solved puzzle: ")
solve(board)
print_board(board)
draw_number(board)
