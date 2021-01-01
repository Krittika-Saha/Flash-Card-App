from tkinter import *
import pandas as pds
from random import randint
BACKGROUND_COLOR = "#B1DDC6"
chosen_word = ''

#----------------------------RIGHT AND WRONG--------------


def change_french():
    global chosen_word
    chosen_word = randint(0, 100)
    data = pds.read_csv("data/french_words.csv")
    canvas.itemconfig(front_img, image=image)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(content, text=data['French'][chosen_word], fill='black')
    window.after(3000, change_english)


def change_english():
    data = pds.read_csv("data/french_words.csv")
    canvas.itemconfig(front_img, image=back_img)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(content, text=data['English'][chosen_word], fill='white')
#----------------------------UI SETUP--------------------------


window = Tk()
window.title("Flashy")
window.minsize(width=900, height=550)
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file='C:/Flash-Card-App/images/card_front.png')
back_img = PhotoImage(file='C:/Flash-Card-App/images/card_back.png')
front_img = canvas.create_image(400, 263, image=image)
#Text
title = canvas.create_text(400, 150, text='Are you ready?', font=('Ariel', 40, 'italic'))
content = canvas.create_text(400, 263, text='Click ✔ to start', font=("Ariel", 60, 'bold'))
#Buttons
unknown_button_img = PhotoImage(file='C:/Flash-Card-App/images/wrong.png')
unknown_button = Button(image=unknown_button_img, highlightthickness=0)
unknown_button.grid(row=1, column=0)
known_button_img = PhotoImage(file='images/right.png')
known_button = Button(image=known_button_img, highlightthickness=0, command=change_french)
known_button.grid(row=1, column=1)

canvas.grid(row=0, column=0, columnspan=2)

window.mainloop()

