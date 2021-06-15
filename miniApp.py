


# I am going to add a pic in tkwindow
# I am going to use PhotoImage to 

import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk

root = tk.Tk() 

  

root.geometry("800x600") 
  




load = Image.open("C:/Most used/G&D/Discord1/miniApp-pic.jfif")
render = ImageTk.PhotoImage(load)


img = ttk.Label(root, image=render)
img.image = render
img.place(x=0, y=0)









Sv = ttk.Entry(root, justify='left').grid(column = 15, row= 3, ipady= 1, ipadx= 10, pady= 100, padx=440)

bean = ttk.Entry(root, justify='left')
bean.grid(column = 15, row = 2, ipadx=10, pady=100)
root.update()
print(root.winfo_width(), root.winfo_height(), root.winfo_geometry())


root.mainloop()


#padx and pady moves the object in x and y position
#ipady and ipadx stretches the object in the x and y posistion.
#winfor aka window info prints in the output about those attributes