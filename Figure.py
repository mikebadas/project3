from tkinter import *
from tkinter.colorchooser import *
import math as m

root = Tk()
root.geometry("1070x600")
root.resizable(0,0)
root["bg"] = "lightblue"
canvas = Canvas(root, width=500, height=500)
canvas.place(x=-2, y=-2)
lbl1 = Label(root, text="Starting angle")
lbl1.place(x=550, y=0)
lbl2 = Label(root, text="Quantity")
lbl2.place(x=650, y=0)
lbl3 = Label(root, text="Angle change")
lbl3.place(x=750, y=0)
lbl4 = Label(root, text="Starting length")
lbl4.place(x=850, y=0)
lbl5 = Label(root, text="Length change")
lbl5.place(x=950, y=0)
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

def startangle(event):
	global a
	a = scale1.get()
	
def quantity(event):
	global b
	b = scale2.get()

def anglechange(event):
	global c
	c = scale3.get()
	
def startlength(event):
	global d
	d = scale4.get()
	
def lengthchange(event):
	global e
	e = scale5.get()


scale1 = Scale(root, orient=VERTICAL, length=300, from_=0, to=360, tickinterval=50, resolution=1)
scale1.place(x=550, y=30)
scale1.bind("<ButtonRelease-1>", startangle)

scale2 = Scale(root, orient=VERTICAL, length=300, from_=0, to=100, tickinterval=10, resolution=1)
scale2.place(x=650, y=30)
scale2.bind("<ButtonRelease-1>", quantity)

scale3 = Scale(root, orient=VERTICAL, length=300, from_=0, to=360, tickinterval=50, resolution=1)
scale3.place(x=750, y=30)
scale3.bind("<ButtonRelease-1>", anglechange)

scale4 = Scale(root, orient=VERTICAL, length=300, from_=0, to=100, tickinterval=10, resolution=1)
scale4.place(x=850, y=30)
scale4.bind("<ButtonRelease-1>", startlength)

scale5 = Scale(root, orient=VERTICAL, length=300, from_=0, to=100, tickinterval=10, resolution=1)
scale5.place(x=950, y=30)
scale5.bind("<ButtonRelease-1>", lengthchange)

def draw():
	canvas.delete("all")
	x1 = 250
	y1 = 250
	global a
	global b
	global c
	global d
	global e
	a = scale1.get()
	b = scale2.get()
	c = scale3.get()
	d = scale4.get()
	e = scale5.get()
	for x in range(1,b+1):
		x += 1
		x2 = x1 + d*m.sin(a*m.pi/180)
		y2 = y1 + d*m.cos(a*m.pi/180)
		a += c
		d += e
		canvas.create_line(x1, y1, x2, y2, fill=r)
		x1 = x2
		y1 = y2
					
def delete():
	canvas.delete("all")

def color():
	global r
	f = askcolor(parent=root, initialcolor=(255,255,255))
	r = f[1]

btn = Button(root, text="Draw", font="34", width=12, command=draw)
btn.place(x=70, y=520)

btn2 = Button(root, text="Clear", font="34", width=12, command=delete)
btn2.place(x=270, y=520)

btn3 = Button(root, text="Choose color", font="34", width=12, command=color)
btn3.place(x=713, y=380)
canvas.mainloop()