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

label_1 = tk.Label(root, text='''Hello,
world!''',
                   bg = 'light cyan',           # background
                   fg= 'dark cyan',             # font-ground
                   font=('Arial', 20, 'italic'),
                   padx=0,                      # paddle x-axis
                   pady=0,                      # paddle y-axis
                   width=10,
                   height=14,
                   anchor='center',             # location of the text
                   # relief=tk.RAISED,            # border
                   # bd=1,                        # border depth
                   justify=tk.CENTER            # align the string
                   )
label_1.pack()                                  # show the label

root.mainloop()