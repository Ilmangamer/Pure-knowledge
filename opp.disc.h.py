
import tkinter  as tk
from tkinter import ttk


gui = tk.Tk()


# first label
vim = ttk.Label(gui, background = 'red')
vim.place(x=4, y =7, width= 180, height= 130)

nvim = ttk.Label(gui, background= 'blue')
nvim.place(x=5, y=9, width= 180, height= 130)


def hide_square():
	vim.bind("<Button-1>")
	vim.destroy()
def show_square():

	try:
		nvim.place()
		nvim.destroy()
	except NameError:
		print('eror ugh tcl')
	
	try:
		nvim.bind("<Button-2>")
	except NameError:
		print('TclError ughh')
			
btn1 = ttk.Button(gui, text= 'press', command=hide_square)
btn1.place(x= 19, y= 10, width=20, height= 12)
btn2 = ttk.Button(gui, text= 'new square', command=show_square)
btn2.place(x= 19, y= 15, width=20, height= 12)
				
#gui.configure(bg= 'orange')
#gui.wm_attributes("-transparentcolor", 'orange')
gui.mainloop()
