import tkinter as tk

window = tk.Tk()

my_label = tk.Label(
    window,
    text = "Text stuff",
    background = "purple",
    foreground = "#34A2FE"
)

my_label.pack()

button = tk.Button(
    text = "It's a button wow you should click on it it does nothing though",
    background = "red"
)

button.pack()

entry = tk.Entry()
entry.pack()

name = entry.get()

window.mainloop()

