from tkinter import *
from tkinter import messagebox
import pandas
from random import choice
import os

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

# ------------------------ PREPARE CSV FILE --------------------------- #
try:
    data = pandas.read_csv(r"data\words_to_learn.csv")
except FileNotFoundError:
    # If there is no file / first time using the program
    data = pandas.read_csv(r"data\french_words.csv")
finally:
    # Change data to list of dictionary. Key is French, value is French word
    dictionary = data.to_dict(orient="records")


# ------------------------ CREATE NEW FLASHCARD --------------------------- #
def new_word():
    global random_word, flip_timer
    # Present card then start timer
    window.after_cancel(flip_timer)
    random_word = choice(dictionary)
    canvas.itemconfig(vocab, text=random_word["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    

# -------------------------- FLIP CARD ----------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(vocab, fill="white", text=random_word["English"])


# -------------------------- NEW DICTIONARY ----------------------------- #
def remove_word():
    if len(dictionary) > 1:
        dictionary.remove(random_word)
        data = pandas.DataFrame(dictionary)
        data.to_csv(r"data\words_to_learn.csv", index=False)
        new_word()
    else:
        messagebox.showinfo(title="Congratulations!", message="You've learned all the vocabs. Good job!")
        # Remove empty words_to_learn file so program doesn't crash. Start with full list instead
        os.remove(r"data\words_to_learn.csv")
        window.quit()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas with card images, English word, and French word
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=r"images\card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_back = PhotoImage(file=r"images\card_back.png")
canvas.grid(row=0, column=0, columnspan=2, rowspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
vocab = canvas.create_text(400, 280, text="", font=("Arial", 60, "bold"))

# Buttons
right_image = PhotoImage(file=r"images\right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=remove_word)
right_button.grid(row=2, column=1)
wrong_image = PhotoImage(file=r"images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=new_word)
wrong_button.grid(row=2, column=0)

new_word()

window.mainloop()