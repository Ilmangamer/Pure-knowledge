import tkinter as Tk
import time


root = Tk.Tk()
root.geometry("200x100")

INPUT, focused = False,False

def maine(event):
    global INPUT,focused
    focused = True
    while focused:
        x = ""
        INPUT = True
        quit = 
        while INPUT and focused:
            #Here we update our code, get our input, wiping it, inserting, updating, deleting and sleeping.
            root.update()
            x += Sv.get()
            Sv.delete(0,len(Sv.get()))
            Sv.insert(0,"*"*len(x))
            root.update()
            Sv.delete(0,len(Sv.get()))
            time.sleep(1/30)
        Sv.delete(0,'end')
        print(x)
        x = ""
        del x



# When our process has run, our event = False
# We go global to call on our functions
def disfocus(event):
    global focused
    focused = False

def Inner(event):
    global INPUT
    INPUT = False

def quit(event):
    print ("You are an idiot")
root.quit()

# we are binding it to our output. "Temprarily"
Sv = Tk.Entry(root)
Sv.place(x=0, y=0, height=20, width=89)
Sv.bind("<FocusIn>", maine)
Sv.bind("<FocusOut>", disfocus)
Sv.bind("<Return>", Inner)
Sv.bind("<Control-backslash>", quit)

# keep it displayed
root.mainloop()
