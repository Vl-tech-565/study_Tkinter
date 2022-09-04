# 3rd lesson. Button widget

import tkinter as tk

# set variables
count = 0
is_disabled = False


def change_4th_button():
    global is_disabled
    if is_disabled:
        btn4['state'] = tk.NORMAL
        is_disabled = False
    else:
        btn4['state'] = tk.DISABLED
        is_disabled = True


def add_label():
    label = tk.Label(root, text='New label',
                     bg='gray',

                     )
    label.pack()


def counter():
    global count
    count += 1
    btn4['text'] = f'Counter: {count}'


# init root window
init_sizes = "800x450"
offset = '+400+225'

root = tk.Tk()

photo = tk.PhotoImage(file='joystick.png')
root.iconphoto(False, photo)

root.geometry(init_sizes + offset)
root.title('My first GUI app')
root.resizable(False, False)

# Test buttons
btn1 = tk.Button(root, text='disable 4th',
                 command=change_4th_button
                 )

btn1.pack()

btn2 = tk.Button(root, text='Add label',
                 command=add_label
                 )
btn2.pack()

btn3 = tk.Button(root, text='Add label by lambda',
                 command=lambda: tk.Label(root, text='new lambda').pack()
                 )
btn3.pack()

btn4 = tk.Button(root, text=f'Counter: {count}',
                 command=counter,
                 activebackground='dark cyan',
                 bg='cyan'
                 )
btn4.pack()

root.mainloop()
