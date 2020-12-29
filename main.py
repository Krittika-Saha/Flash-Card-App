from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

#----------------------------UI SETUP--------------------------


window = Tk()
window.title("Flashy")
window.minsize(width=900, height=550)
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='C:/Flash-Card-App/images/card_front.png')
canvas.create_image(400, 263, image=front_img)
#Text
canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='word', font=("Ariel", 60, 'bold'))
#Buttons
unknown_button_img = PhotoImage(file='C:/Flash-Card-App/images/wrong.png')
unknown_button = Button(image=unknown_button_img, highlightthickness=0)
unknown_button.grid(row=1, column=0)
known_button_img = PhotoImage(file='images/right.png')
known_button = Button(image=known_button_img, highlightthickness=0)
known_button.grid(row=1, column=1)

canvas.grid(row=0, column=0, columnspan=2)
window.mainloop()

