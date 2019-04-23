from tkinter import *
from tkinter import Menu
window = Tk()
window.title("Welcome to LikeGeeks app")

main_menu = Menu(window)
window.config(menu = main_menu)

file_menu = Menu(main_menu)
main_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'New File')
file_menu.add_separator()
file_menu.add_command(label = 'Edit')


help_menu = Menu(main_menu)
main_menu.add_cascade(label = 'Help', menu = help_menu)
help_menu.add_command(label = 'About Idle')
help_menu.add_command(label = 'IDLE')
help_menu.add_separator()
help_menu.add_command(label = 'Python Docs')

option_menu = Menu(main_menu)
main_menu.add_cascade(label = 'Option', menu = option_menu)



window.mainloop()


##from tkinter import*
##from tkinter.ttk import Progressbar
##from tkinter import ttk
##
##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('350x200')

##style = ttk.Style()
##style.theme_use('default')
##style.configure("black.Horizontal.TProgressbar", background='black')
##bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
##bar['value'] = 70
##bar.grid(column=0, row=0)


##window.mainloop()






##from tkinter import *
##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('350x200')
##
##var = IntVar()
##var.set(40)
##spin = Spinbox(window, from_=10, to =50, width=5, textvariable = var)
##spin.grid(column=0,row=0)
##window.mainloop()





##from tkinter import *
##from tkinter import scrolledtext
##
##window = Tk()
##window.title('Welcome to the Geek app')
##window.geometry('350x240')
##
##txt = scrolledtext.ScrolledText(window, width = 40, height = 10)
##txt.grid(row = 0, column =0)
##txt.insert(INSERT, 'Your text goes here')
##txt.delete(1.0, END)
##window.mainloop()







##from tkinter import *
##from tkinter.ttk import *
##
##window = Tk()
##window.title('Just some more fun')
##window.geometry('350x240')
##
##
##var1 = BooleanVar()
##chk1 = Checkbutton(window, text = 'Humble', var = var1)
##var2 = BooleanVar()
##chk2 = Checkbutton(window, text = 'Disciplined', var = var2)
##var3 = BooleanVar()
##chk3 = Checkbutton(window, text = 'Stern', var = var3)
##chk1.grid(row = 0, column = 0)
##chk2.grid(row = 0, column = 1)
##chk3.grid(row = 0, column = 2)
##
##selected = IntVar()
##rad1 = Radiobutton(window, text = 'First', value = 1, variable = selected)
##rad2 = Radiobutton(window, text = 'Second', value = 2, variable = selected)
##rad3 = Radiobutton(window, text = 'Third', value = 3, variable = selected)
##def clicked():
##    print(selected.get())
##
##btn = Button(window, text = 'Click Me', command = clicked)
##rad1.grid(row = 1, column = 0)
##rad2.grid(row = 1, column = 1)
##rad3.grid(row = 1, column = 2)
##btn.grid(row = 1, column = 3)

###########Button and Entry#########

##a_label = Label(window, text = 'Hi there!')
##a_label.grid(row = 0, column = 0)
##
##a_text = Entry(window, width = 30, state = 'disabled')
##a_text.grid(row = 0, column = 1)
##a_text.focus()
##
##def clicked():
##    ##a_btn.config(text = 'Button was clicked!')
##    res = 'Welcome to ' + a_text.get()
##    a_btn.config(text = res)
##    
##a_btn = Button(window, text = 'Click me', fg = 'blue', command= clicked)
##a_btn.grid(row = 0, column = 2)


##################Combobox##################
##combo = Combobox(window)
##combo['values']= (1,2,3,4,5,'Text')
##combo.current(0)
##combo.get()
##combo.grid(row = 0, column = 0)


##window.mainloop()
































































