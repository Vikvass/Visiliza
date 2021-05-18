from tkinter import *

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
MARGIN = 100    # отступ
BACKGROUND_COLOR = '#556B2F'
label_word = []

def start_position_pole():
    line_1 = canvas.create_line(MARGIN, WINDOW_HEIGHT - MARGIN, MARGIN, MARGIN, width=4)
    line_2 = canvas.create_line(MARGIN, MARGIN, WINDOW_WIDTH // 3, MARGIN, width=4)
    line_3 = canvas.create_line(WINDOW_WIDTH // 3, MARGIN, WINDOW_WIDTH // 3, MARGIN * 1.5, width=4)

def start_position_alpha(word):
    shift_x = shift_y = 0
    count = 0

    for c in range(ord('А'), ord('А') + 32):
        btn = Button(text=chr(c), bg='#D8A903', foreground='black', font='Arial 16', relief=SOLID)
        btn.place(x=WINDOW_HEIGHT - MARGIN * 2 + shift_x, y=MARGIN * 4.5 + shift_y)
        btn.bind('<Button-1>',
                 lambda event: check_alpha(event, word))  # привязываем левую кнопку мыши к каждой кнопке с буквой
        # при нажатии на букву вызывается функция check_alpha где мы проверяем есть ли данная буква в нашем слове
        shift_x += 50
        count += 1

        if (count == 8):
            shift_y += 50
            shift_x = count = 0

def start_position_word(word):
    shift = 0

    for i in range(len(word)):
        label_under = Label(window, text='__', font='Arial 16', bg='#F39F18')
        label_under.place(x=WINDOW_HEIGHT - MARGIN * 2 + shift, y=MARGIN * 3.5)
        shift += 50
        label_word.append(label_under)

def start_word():
    # выбор слова из файлика
    word = 'космос'
    word = word.upper()
    return word

def check_alpha(event, word):
    # event - буква (из нажатия на кнопку получим букву)
    alpha = event.widget['text']
    pos = []

    for i in range(len(word)):
        if (word[i] == alpha):
            pos.append(i)

    if (len(pos) == 0):
        # уменьшаем жизни на 1 и рисуем человечка
        # можно так же блокировать кнопку
        pass
    else:
        for i in range(len(label_word)):
            if (i in pos):
                label_word[i].config(text=word[i])


window = Tk()
window.title('Виселица')
window.resizable(False, False)  # нельзя изменять по ширине и высоте окно

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
