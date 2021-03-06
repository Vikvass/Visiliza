from tkinter import *
import random

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
MARGIN = 100
BACKGROUND_COLOR = 'white'
label_word = []
btn_alpha = []

def start_position_pole():
    line_1 = canvas.create_line(MARGIN, WINDOW_HEIGHT-MARGIN, MARGIN, MARGIN, width=4)
    line_2 = canvas.create_line(MARGIN, MARGIN, WINDOW_WIDTH // 3, MARGIN, width=4)
    line_3 = canvas.create_line(WINDOW_WIDTH // 3, MARGIN, WINDOW_WIDTH // 3, MARGIN * 1.5, width=4)


def start_position_alpha(word):
    shift_x = shift_y = 0
    count = 0

    for c in range(ord('А'), ord('А') + 32):
        btn = Button(text=chr(c), bg='white', foreground='black', font='Arial 16', relief=SOLID)
        btn.place(x=WINDOW_HEIGHT - MARGIN * 2 + shift_x, y=MARGIN * 4.5 + shift_y)
        btn.bind('<Button-1>',
                 lambda event: check_alpha(event, word))  # привязываем левую кнопку мыши к каждой кнопке с буквой
        # при нажатии на букву вызывается функция check_alpha где мы проверяем есть ли данная буква в нашем слове
        shift_x += 50
        count += 1
        btn_alpha.append(btn)

        if (count == 8):
            shift_y += 50
            shift_x = count = 0


def start_position_word(word):
    shift = 0

def start_position_word(word):
    shift = 0

    for i in range(len(word)):
        label_under = Label(window, text='__', font='Arial 16', bg='white')
        label_under.place(x=WINDOW_HEIGHT-MARGIN*2+shift, y=MARGIN*3.5)
        shift += 50
        label_word.append(label_under)


def start_word():
    # выбор слова из файлика
    f = open('Слова к виселице.txt')
    count = 0

    for s in f:
        count += 1

    f.close()

    num_word = random.randint(1, count)
    word = ''
    count = 0

    f = open('Слова к виселице.txt', encoding='utf-8')

    for s in f:
        count += 1

        if (count == num_word):
            for i in range(len(s)):
                if (s[i].isalpha()):
                    word += s[i]

    f.close()

    word = word.upper()
    return word


def check_alpha(event, word):
    # event - буква (из нажатия на кнопку получим букву)
    alpha = event.widget['text']
    pos = []
    global lifes

    for i in range(len(word)):
        if (word[i] == alpha):
            pos.append(i)

    if (len(pos) == 0):
        lifes += 1
        draw_man(lifes)
        # рисуем: голова, тело, руки, ноги, gg
    else:
        for i in range(len(label_word)):
            if (i in pos):
                label_word[i].config(text=word[i])

        end = 0
        for i in range(len(label_word)):
            if (label_word[i].cget('text').isalpha() != 1):
                end = 1
                break

        if (end == 0):
            game_win()


def draw_man(lifes):
    if (lifes == 1):
        head = canvas.create_oval(WINDOW_WIDTH // 3 - 30, MARGIN * 1.5, WINDOW_WIDTH // 3 + 30, MARGIN * 2, fill='black')
    elif (lifes == 2):
        body = canvas.create_oval(WINDOW_WIDTH // 3 - 10, MARGIN * 2, WINDOW_WIDTH // 3 + 10, MARGIN * 4, fill='black')
    elif (lifes == 3):
        left_hand = canvas.create_line(WINDOW_WIDTH // 3 - 10, MARGIN * 2.5, WINDOW_WIDTH // 3 - 60, MARGIN * 2.6, width = 3)
        right_hand = canvas.create_line(WINDOW_WIDTH // 3 + 10, MARGIN * 2.5, WINDOW_WIDTH // 3 + 60, MARGIN * 2.6, width = 3)
    elif (lifes == 4):
        left_foot = canvas.create_line(WINDOW_WIDTH // 3 - 10, MARGIN * 3.5, WINDOW_WIDTH // 3 - 90, MARGIN * 4.5, width = 3)
        right_foot = canvas.create_line(WINDOW_WIDTH // 3 + 10, MARGIN * 3.5, WINDOW_WIDTH // 3 + 90, MARGIN * 4.5, width = 3)
    elif (lifes == 5):
        game_over()


def game_over():
    for btn in btn_alpha:
        btn.destroy()

        canvas.create_text(canvas.winfo_width() / 2 + 200, canvas.winfo_height() / 2 - 200, font='Arial 40',
                           text='Game Over Не расстраивайся)', fill='red')

def game_win():
    for btn in btn_alpha:
        btn.destroy()

        canvas.create_text(canvas.winfo_width() / 2 + 200, canvas.winfo_height() / 2 - 200, font='Arial 40',
                           text='Game Over - Ты молодец) ', fill='red')


window = Tk()
window.title('Виселица')
window.resizable(False, False)  # нельзя изменять по ширине и высоте окно

lifes = 0

canvas = Canvas(window, bg=BACKGROUND_COLOR,
                height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
canvas.place(x=0, y=0)

window.update()
window.geometry('1200x800')

start_position_pole()
word = start_word()
start_position_alpha(word)
start_position_word(word)

window.mainloop()