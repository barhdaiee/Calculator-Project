from tkinter import *

display = Tk()
frame = Frame(display)
frame.pack()

bottom_frame = Frame(display)
bottom_frame.pack(side = 'bottom')

button1 = Button(frame, text = 'Red', fg = 'red')
button1.pack(side = 'left')

button2 = Button(frame, text = 'Brown', fg = 'brown')
button2.pack(side = 'left')

button3 = Button(frame, text = 'Blue', fg = 'blue')
button3.pack(side = 'left')

button4 = Button(bottom_frame, text = 'Black', fg = 'black')
button4.pack(side = 'bottom')

display.mainloop()
