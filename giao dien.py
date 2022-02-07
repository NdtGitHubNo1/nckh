#from tkinter.ttk import *
from tkinter import *
#from tkinter import Tk, Button, Entry, Frame

import numpy as np
import cv2

def donothing():
    x = 0

root = Tk()

root.title("Nhan dien")


menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = donothing)
filemenu.add_command(label = "Open", command = donothing)
filemenu.add_command(label = "Save", command = donothing)
filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)

editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label = "Copy", command = donothing)
editmenu.add_command(label = "Paste", command = None)
editmenu.add_command(label = "Cut", command = None)
editmenu.add_command(label = "Select all", command = None)
menubar.add_cascade(label = "Edit", menu = editmenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help index", command = donothing)
helpmenu.add_command(label = "About", command = donothing)
menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = menubar)

frameBox = LabelFrame(root, text = "Danh sach CAM")
frameBox.grid(row = 0, column = 4)
v = StringVar(frameBox, "0")

values = {"Camera 1" : "1",
          "Camera 2" : "2",
          "Camera 3" : "3",
          "Camera 4" : "4"}
for (text ,value) in values.items():
    Radiobutton(frameBox, text = text, variable = v,
                value = value, indicator = 0, background = "light blue").pack(fill = X, ipady = 5)


frame1 = LabelFrame(root, text = "CAM1", padx = 200, pady = 100)
frame1.grid(row = 0, column = 5)
cam1 = Button(frame1, text="Start")
cam1.pack()

frame2 = LabelFrame(root, text = "CAM2", padx = 200, pady = 100)
frame2.grid(row = 0, column = 25)
cam2 = Button(frame2, text = "Start")
cam2.pack()

frame3 = LabelFrame(root, text = "CAM3", padx = 200, pady = 100)
frame3.grid(row = 5, column = 5)
cam3 = Button (frame3, text = "Start")
cam3.pack()

frame4 = LabelFrame(root, text = "CAM4", padx = 200, pady = 100)
frame4.grid(row = 5, column = 25)
cam4 = Button (frame4, text = "Start")
cam4.pack()

frame5 = LabelFrame(root, text = "Hien thi chi tiet", padx = 100, pady = 100)
frame5.grid(row = 0, column = 50)

name = Label(frame5, text = "Ho ten")
name.grid(row = 0, column = 0, padx = 0, pady = 0)
name.pack()
#name.pack(side = LEFT)

gender = Label(frame5, text = "Gioi tinh")
gender.pack()

cap = cv2.VideoCapture('D:/video/video4.mp4')
while(cap.isOpened()):
    ret, frame1 = cap.read()
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGRGRAY)
    cv2.imshow(frame1, gray)
    if cv2.waitKey(1) & 0xFF == ord('2'):
        break

cap.release()
cv2.destroyAllWindows()

root.mainloop()
