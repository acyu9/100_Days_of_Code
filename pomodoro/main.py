from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- POP TIMER ------------------------------- # 
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    start_button.config(state="disabled")
    reset_button.config(state="normal")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
        focus_window("on")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
        focus_window("on")
    else:
        count_down(work_sec)
        timer_label.config(text="Work")
        focus_window("off")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # // is integer division; same as floor
    count_min = count // 60
    count_sec = count % 60

    # Rounds to 2 decimal places so 5:00 instead of 5:0
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        # Execute a command after a time delay. count-1 is the positional argument for the func
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# A way to read through a file and get a hold of an image at the location
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# Timer and check mark labels
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=1)
check_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

# Start and reset buttons
start_button = Button(text="Start", command=start_timer, state="normal")
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)

window.mainloop()

