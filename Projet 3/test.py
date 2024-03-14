#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
import Tkinter as tk
from Tkinter import filedialog
from PIL import Image, ImageTk
 
 
def openfile():
    global photo
    im = filedialog.askopenfilename(filetypes=[('png files', '.png'), ('jpg files', '.jpg')])
    image = Image.open(im) 
    photo = ImageTk.PhotoImage(image)
    canvas.itemconfig(cimage, image=photo)
 
 
root = tk.Tk()
canvas = tk.Canvas(root)
cimage = canvas.create_image(0, 0, anchor=tk.NW, image="")
canvas.pack()
ouvrir = tk.Button(root, text="Ouvrir", command=openfile)
ouvrir.pack()
root.mainloop()