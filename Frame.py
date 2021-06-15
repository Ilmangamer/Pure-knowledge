

#class Imutable():
	#def __init__(self, var, x):



		#def var(self, var):
			#self.var
			#print(id(x))


		#def x(self, x):
			#"self.x
			#print(id(x))



#Imutable()
#x = 13
#def func(x):
	#print('x is ', x)

	#x = 3
	#print(id(x))
	#print('x has changed value', x)

#func(x)
#print('x came back local automatically when you called it', x)
#print('x id is', (id(x)))



# using pack

import tkinter as tk

newin = tk.Tk()

top_frame = tk.Frame(newin).pack()
bottom_frame = tk.Frame(newin).pack(side = "bottom")




fbtn1 =tk.Button(top_frame, text='click me fore', fg= 'black', bg= 'white').pack()

fbtn2 =tk.Button(top_frame, text='click me foreh', fg= 'black', bg= 'white').pack()

btn1= tk.Button(bottom_frame, text = 'hey', fg = 'black', bg=  'blue').pack(side = "right")
btn2= tk.Button(bottom_frame, text = 'minnesota', fg = 'grey', bg= 'red').pack(side = "left")


newin.mainloop()




import Tkinter

main = tk.Tk()

w = tkinter.Button(text = '')





