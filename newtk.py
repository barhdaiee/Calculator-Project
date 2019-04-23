import tkinter
window = tkinter.Tk()
window.title('Demo')

def function():
    pass

##create a root menu to insert all the sub menus
root_menu = tkinter.Menu(window)
window.config(menu = root_menu)

##create sub menus in the root menu
file_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'New File', command = function)
file_menu.add_command(label = 'Open file', command = function)
file_menu.add_separator()
file_menu.add_command(label = 'Exit', command = window.quit)

##creating another sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = 'Edit', menu = edit_menu)
edit_menu.add_command(label = 'Undo', command = function)
edit_menu.add_command(label = 'Redo', command = function)
edit_menu.add_separator()

##creating another sub menu
format_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = 'Format', menu = format_menu)
format_menu.add_command(label = 'Indent Region', command = function)
format_menu.add_command(label = 'Dedent Region', command = function)


window.mainloop()
