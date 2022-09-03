import tkinter as tk

if __name__ != '__main__':
    init_sizes = '800x450'
    offset = '+400+225'
    min_x, min_y = 160, 90
    max_x, max_y = 960, 540

    root = tk.Tk() # initialization of the window
    root.config(bg='#1AEEE6')
    root.title('My first GUI app')
    photo = tk.PhotoImage(file='joystick.png')
    root.iconphoto(False, photo)
    root.geometry(init_sizes + offset)
    root.minsize(min_x, min_y)
    root.maxsize(max_x, max_y)

    root.mainloop() # show the basic window