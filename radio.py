from tkinter import *

root = Tk()
root.title("Image")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")

#r = IntVar()
#r.set(None)

toppings = [
    ("pepperoni", "Pepperoni"),
    ("cheese", "Cheese"),
    ("mushroom", "Mushroom"),
    ("onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    label = Label(root, text=pizza.get())
    label.pack()

#Radiobutton(root, text="Option1", variable=r, value=1).pack()
#Radiobutton(root, text="Option2", variable=r, value=2).pack()

button = Button(root, text="Click me", command=lambda: clicked(pizza.get()))
button.pack()
root.mainloop()
