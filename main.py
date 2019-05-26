from tkinter import *

#ubuntu font
#config file
#dark/dark blue color scheme


f_size=11
wfont="Arial"
background_color="black"
font_color="white"
cursor_color="pink"
def_size="500x300"
win_title="Macias's Project"




def testing():
    print("Opening")

def save():
    print("Saving")

def save_as():
    print("Saving as")


window=Tk()
window.title(win_title)
window.configure(background="gray")
window.geometry(def_size)

#menu bar
menu_bar=Menu(window)
menu_bar.add_command(label="Open", command=testing)
menu_bar.add_command(label="Save", command=save)
menu_bar.add_command(label="Save as", command=save_as)
window.config(menu=menu_bar)

#text window and scroll bar
text_area=Text(window)
text_area.pack(expand=True, fill=BOTH)
#scrollbar=Scrollbar(text_area)
#scrollbar.pack(side=RIGHT, fill=Y)
    #custom colors
text_area.configure(background=background_color, fg=font_color, insertbackground=cursor_color, font=(wfont,f_size))
text_area.focus_set() #focus to the text area




window.mainloop()
