# 3rd lesson. Homework

import tkinter as tk
import random

colors = ('black', 'white', 'cyan', 'gray', 'purple', 'pink', 'orange', 'light yellow')


def change_bg_color():
    global colors
    root['bg'] = colors[random.randint(0, len(colors) - 1)]


# init root window
init_sizes = "800x450"
offset = '+400+225'

root = tk.Tk()

photo = tk.PhotoImage(file='joystick.png')
root.iconphoto(False, photo)

root.geometry(init_sizes + offset)
root.title('My first GUI app')
root.resizable(False, False)

# Test button
btn_chg_clr = tk.Button(text='change bg color',
                        bg='light green',
                        command=change_bg_color
                        )
btn_chg_clr.pack(pady=150)
root.mainloop()
