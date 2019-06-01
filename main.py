from tkinter import *
from tkinter import filedialog
from fileio import *

#mini TODO
#ubuntu monospace font

conf_file=fread("settings")
conf_file=conf_file.split(",")


f_size=int(conf_file[0])
wfont=conf_file[1]
background_color=conf_file[2]
font_color=conf_file[3]
cursor_color=conf_file[4]
def_size=conf_file[5]
win_title=conf_file[6]

window=Tk()
window.title(win_title)
window.configure(background="gray")
window.geometry(def_size)

is_new=1



#text window and scroll bar
text_area=Text(window)
text_area.pack(expand=True, fill=BOTH)
#scrollbar=Scrollbar(text_area)
#scrollbar.pack(side=RIGHT, fill=Y)
#custom colors
text_area.configure(background=background_color, fg=font_color, insertbackground=cursor_color, font=(wfont,f_size))
text_area.focus_set() #focus to the text area


path_to_save=""

def cleararea():
    text_area.delete('1.0', END)


def new():
    window.title("New File")
    global is_new
    is_new = 1
    #print(is_new)
    cleararea()

def open():
    #print("Opening")
    cleararea()
    window.filename = filedialog.askopenfilename(initialdir = "~",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    window.title(window.filename)
    f_content=fread(str(window.filename))
    global is_new
    is_new = 0
    global path_to_save
    path_to_save=str(window.filename)
    #print(window.filename)
    #print(f_content)
    text_area.insert("1.0",f_content)


def save_as():
    #print("Saving as")
    save_as_dir=filedialog.asksaveasfilename(initialdir="~",defaultextension=".txt",title = "Select save location",filetypes=(("text files","*txt"),("all files", "*.*")))

    #print(save_as_dir)
    global path_to_save
    path_to_save=save_as_dir
    acontent=text_area.get("1.0", "end-1c")
    #print(acontent)
    fwrite(save_as_dir,acontent)
    global is_new
    is_new=0

def save():
    #print("Saving")
    global path_to_save
    if (is_new is 1) or (path_to_save is '') :
        save_as()
    else:
        #global path_to_save
        acontent=text_area.get("1.0", "end-1c")
        fwrite(path_to_save,acontent)

#menu bar
menu_bar=Menu(window)
menu_bar.add_command(label="New", command=new)
menu_bar.add_command(label="Open", command=open)
menu_bar.add_command(label="Save", command=save)
menu_bar.add_command(label="Save as", command=save_as)
window.config(menu=menu_bar)





window.mainloop()
