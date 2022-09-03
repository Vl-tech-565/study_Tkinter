# 2nd lesson. Label vidget

import tkinter as tk

init_sizes = '800x450'
offset = '+400+225'

root = tk.Tk()

photo = tk.PhotoImage(file='joystick.png')
root.iconphoto(False, photo)

root.config(bg='light cyan')
root.geometry(init_sizes+offset)
root.title('My first GUI app')
root.resizable(False, False)

root.mainloop()