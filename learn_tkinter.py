# 4th lesson. Grid (how to arrange labels on the root window)
import tkinter as tk


# variables
ROWS = 10
COLUMNS = 10
init_sizes = "800x450"
offset = "+400+225"

# main body
root = tk.Tk()
root.geometry(init_sizes + offset)

photo = tk.PhotoImage(file='joystick.png')
root.iconphoto(False, photo)
root.title('My first GUI app')

tk.Button(text='Start').grid(row=0,column=0, columnspan=10,stick='we')

for i in range(1,ROWS):
    for j in range(1,COLUMNS):
        tk.Button(text='button').grid(row=i, column=j)

tk.Button(text='Finish').grid(row=11,column=0, columnspan=10,stick='we')

root.grid_columnconfigure(0, minsize=50)
root.grid_columnconfigure(3, minsize=100)

root.mainloop()
