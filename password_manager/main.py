from msilib.schema import File
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
#import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    #pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_file():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    if user == "" or website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    # else:
    #     # Proper way to break long line without extra indentation in second line
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"\
    #         f"Email: {user} \nPassword: {password} \nIs it ok to save?")

        #if is_ok:
    else:
        #with open("data.txt", "w") as file:
            #file.write(f"{website} | {user} | {password}\n")

        try:    
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)
                # Update old data with new data
                data.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        finally:            
            with open("data.json", "w") as file:
                # Save updated data - obj=what to write, file=file to save, indent=formatting so not one line
                json.dump(data, file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# -------------------------- SEARCH PASSWORD ----------------------------- #
def search_data():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:          
            messagebox.showinfo(title="Error", message=f"No details for {website} found.")
        website_entry.delete(0, END)      


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=(FONT_NAME, 12, "bold"), bg="white")
website_label.grid(row=1, column=0, sticky=E)
user_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"), bg="white")
user_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=(FONT_NAME, 12, "bold"), bg="white")
password_label.grid(row=3, column=0, sticky=E)

# Entry
website_entry = Entry(highlightthickness=2)
website_entry.grid(row=1, column=1, sticky=EW)
website_entry.focus()
user_entry = Entry(highlightthickness=2)
user_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
user_entry.insert(0, "example@email.com")
password_entry = Entry(highlightthickness=2)
password_entry.grid(row=3, column=1, sticky=EW)

# Buttons
generate_button = Button(text="Generate Password", font=(FONT_NAME, 8, "bold"), command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", font=(FONT_NAME, 8, "bold"), command=add_file)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)
search_button = Button(text="Search", font=(FONT_NAME, 8, "bold"), width=17, command=search_data)
search_button.grid(row=1, column=2)

window.mainloop()