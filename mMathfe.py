from tkinter import *;
import time;
from random import randint;
import math;
root = Tk();
root.geometry("1000x1000");c = Canvas(master=root);c.place(x=0,y=0,width=1000,height=1000)
points = [[randint(0,1000),randint(0,1000),randint(-10,10),randint(-10,10)] for x in range(15)]
while True:
    c.delete("all")
    for e,x in enumerate(points):
        x[0],x[1]=((x[0]+x[2])%1000 if (x[0]+x[2])%1000 >= 0 else x[0]+x[2]+1000),((x[1]+x[3])%1000 
            if (x[1]+x[3])%1000 >= 0 else x[1]+x[3]+1000)
        for ee,y in enumerate(points):
            if e != ee:
                distance = math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
                if distance < 256:
                    _ = (str(hex(int(distance)))[2:] if len(str(hex(int(distance)))[2:]) == 2 else "0"+
                        str(hex(int(distance)))[2:])
                    c.create_line(x[0],x[1],y[0],y[1],width=2,fill="#"+_+_+_)
                    x[2],x[3]=x[2]+(y[0]-x[0])/700,x[3]+(y[1]-x[1])/700
        c.create_oval(x[0]-3,x[1]-3,x[0]+3,x[1]+3,fill="#000000")
    root.update();time.sleep(1/60)
root.mainloop()