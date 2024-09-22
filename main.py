from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(300)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=120, pady=100, bg=YELLOW)

label = Label(text="Pomodoro Timer", font=("Courier", 20, "bold"), fg=RED, bg=YELLOW)
label.grid(column=1, row=0)

btn1 = Button(text="Start", bg=GREEN, font=("Courier", 12, "normal"), command=start_timer)
btn1.grid(column=0, row=2)

btn2 = Button(text="Reset", bg=GREEN, font=("Courier", 12, "normal"))
btn2.grid(column=2, row=2)

label = Label(text="✅", font=("Courier", 15, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, text="25:00", fill="yellow", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
