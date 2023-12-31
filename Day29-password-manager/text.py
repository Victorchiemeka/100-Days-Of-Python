from tkinter import *
import json
import random
import subprocess

# Your code here that uses pyperclip

from tkinter import messagebox

# ---------------------- PASSWORD GENERATOR --------------------------- #
# Implement your password generator logic here

# Password Generator Project


def copy_to_clipboard(text):
    try:
        subprocess.run(["xsel", "-b", "-i"], input=text.encode("utf-8"), check=True)
        print("Text copied to clipboard successfully.")
    except subprocess.CalledProcessError:
        print("Error: Unable to copy text to clipboard.")


def generatepas():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for i in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)

    password = "".join(password_list)

    passentry.insert(0, password)

    copy_to_clipboard(password)


# ---------------------- SAVE PASSWORD ------------------------------- #
# Implement your function to add and save passwords securely
from tkinter import messagebox, END


def save():
    website = webentry.get()
    email = emailentry.get()
    password = passentry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure no fields are empty"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?",
        )
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Read old data
                    data = json.load(data_file)
                    # update old with new new file
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as datafile:
                    # Saving updated data
                    json.dump(data, datafile, indent=4)

            # with open("data.json", "w") as datafile:
            #     json.dump(new_data, datafile, indent=4)
            webentry.delete(0, END)
            emailentry.delete(0, END)
            passentry.delete(0, END)


def find_password():
    website = webentry.get()
    try:
        with open("data.json", "r") as data_file:
            # Read old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERRO", message="No Data File found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title="Website", message=f"Email: {email}\nPassword:{password}"
            )
        else:
            if len(website) == 0:
                messagebox.showinfo(
                    title="Error", message="Enter the website you want Find"
                )
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo)
canvas.grid(column=2, row=1)

# Labels and entry fields for website, email, and password
web = Label(text="Website")
web.grid(column=1, row=2)
webentry = Entry(width=35)
webentry.focus()
webentry.grid(column=2, columnspan=1, row=2)

web_btn = Button(text="Find Password", command=find_password)
web_btn.grid(column=3, row=2, padx=(0, 10))


email = Label(text="Email/Username")
email.grid(column=1, row=3)
emailentry = Entry(width=35)
emailentry.insert(0, "hoskenvic@gmail.com")
emailentry.grid(column=2, row=3)

password = Label(text="Password")
password.grid(column=1, row=4)
passentry = Entry(width=35)
passentry.grid(column=2, row=4)

generate = Button(text="Generate Password", command=generatepas)
generate.grid(column=3, row=4, padx=(0, 10))

add = Button(text="Add", command=save)
add.grid(column=2, row=5)
# ---------------------- End of UI Setup ------------------------------ #

window.mainloop()
