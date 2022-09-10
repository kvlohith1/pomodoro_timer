import math
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
countdown = None

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    global reps
    reps = 0
    window.after_cancel(countdown)
    canvas.itemconfig(timer, text='00:00')
    checkmark.config(text='')
    timer_title.config(text='Timer', fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_title.config(text='Break', fg=RED)
        window.after(1000, count_down, LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_title.config(text='Break', fg=PINK)
        checkmark.config(text='✔' * math.ceil(reps / 2))
        window.after(1000, count_down, int(SHORT_BREAK_MIN * 60))
    else:
        timer_title.config(text='Work', fg=GREEN)
        window.after(1000, count_down, WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        text = f'{minutes}:0{seconds}'
    else:
        text = f'{minutes}:{seconds}'
    canvas.itemconfig(timer, text=text)
    if count > 0:
        global countdown
        countdown = window.after(1000, count_down, count - 1)
    else:
        checkmark_text = '✔'
        checkmark.config(text=checkmark_text * math.ceil(reps/2))
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro timer')
window.config(padx=70, pady=70, background=YELLOW)
timer_title = Label(text='Timer', font=(FONT_NAME, 40, 'bold'))
timer_title.config(fg=GREEN, bg=YELLOW)
timer_title.grid(row=0, column=2)
canvas = Canvas(width=200, height=210, background=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 90, image=image)
timer = canvas.create_text(102, 120, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=2, column=2)
checkmark = Label(text='', bg=YELLOW)
checkmark.grid(row=4, column=2)
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=1)
reset_button = Button(text='Reset', highlightthickness=0, command=timer_reset)
reset_button.grid(row=3, column=3)
window.mainloop()
