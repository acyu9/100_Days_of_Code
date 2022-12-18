from tkinter import *

# AttributeError: partially initialized module 'tkinter' has no attribute 'Tk' if file name is tkinter.py
window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# Pack puts label on the screen, default is center
#my_label.pack()

# Alternative ways of changing label text
#my_label["text"] = "New Text"
#my_label.config(text="New Text")


#Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=0)
button.config(padx=20, pady=20)

#Entry
input = Entry(width=10)
#input.pack()
input.grid(column=1, row=1)






window.mainloop()