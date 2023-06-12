import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any fields empty.")

    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details that you entered\nEmail: {email}\nPassword:{password}\nIs it okay to save?")
        if is_okay:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, tkinter.END)
                pass_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = tkinter.Canvas(width=200, height=200)
img_logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(column=1, row=0)

# Website Label
web_label = tkinter.Label(text="Website:")
web_label.grid(column=0, row=1)

# Website Entry
web_entry = tkinter.Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

# Email label
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

# Email Entry
email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "engtechno25@gmail.com")

# Password Label
pass_label = tkinter.Label(text="Password:")
pass_label.grid(column=0, row=3)

# Password Entry
pass_entry = tkinter.Entry(width=21)
pass_entry.grid(row=3, column=1)

# Generate Button
gen_btn = tkinter.Button(text="Generate Password", command=generate_password)
gen_btn.grid(column=2, row=3)

# Add Button
add_btn = tkinter.Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
