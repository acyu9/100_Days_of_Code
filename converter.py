from tkinter import *

# AttributeError: partially initialized module 'tkinter' has no attribute 'Tk' if file name is tkinter.py
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# Miles input
input = Entry(width=10)
input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="miles", font=("Arial", 18, "normal"))
miles_label.grid(column=2, row=0)

# Label 2
miles_label = Label(text="is equal to", font=("Arial", 18, "normal"))
miles_label.grid(column=0, row=1)

# Km label
miles_label = Label(text="km", font=("Arial", 18, "normal"))
miles_label.grid(column=2, row=1)


# Button
def button_clicked():
    miles = input.get()
    kilometer = round(float(miles) * 1.6, 2)
    # Converted km
    miles_label = Label(text=kilometer, font=("Arial", 18, "normal"))
    miles_label.grid(column=1, row=1)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()