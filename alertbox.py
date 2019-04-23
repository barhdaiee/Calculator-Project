import tkinter

window = tkinter.Tk()
window.title('Hello World')

icon = tkinter.PhotoImage(file = 'Users/user/pictures/screen.png')

label = tkinter.Label(window, image = icon)
label.pack()


window.mainloop()












##import tkinter
##
##window = tkinter.Tk()
##window.title('DEMO')
##
##canvas = tkinter.Canvas(window, width = 500, height = 500)
##canvas.pack()
##
####to create line
##line1 = canvas.create_line(25,25,250,150)
##line2 = canvas.create_line(25,250,250,150, fill = 'red')
##rect = canvas.create_rectangle(500,25,175,75, fill = 'green')
##canvas.delete(line1)
##
##
##window.mainloop()






##import tkinter
##import tkinter.messagebox
##
##window = tkinter.Tk()
##window.title('Hello World')
##
####to create a simple alert box
####tkinter.messagebox.showinfo('Alert Message', 'This is just an alert message!')
##
##
####to create a question to get response from user{Yes or no}
##response = tkinter.messagebox.askquestion('Simple Question', 'Do you love Python?')
##
##if response == 0:
##    tkinter.Label(window, text = 'Python lover!').pack()
##else:
##    tkinter.Label(window, text = "You don't love Python!").pack()
##
