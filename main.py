import tkinter as t
from tkinter import *
from tkinter import ttk
import sv_ttk
from tkinter import font
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import font
import os
global acord
# long garabge string of code, doesnt even have formatting which would've been easier on pyqt
root = t.Tk()
root.option_add('*font', 'Arial 10')
sv_ttk.set_theme("dark")
wname = "Untitled"

def count():
    global word
    cos = txt.get("1.0", "end-1c")
    wor = cos.split()
    word = len(wor)
    acord.set(f"Words: {word}")
    root.after(300, count)
def save(event=None):
    global txt
    global tefxt
    global wname
    def tefxt():
        global wname

        fname = f"{wname}.txt"
        die = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.join(die, fname)
        cons = txt.get("1.0", "end-1c")
        try:
            with open(fpath, "w") as file:
                file.write(cons)
        except IOError as e:
            print(f"error writing to file: {e}")  
    tefxt()     
    

def saveas(event=None):
    t.Tk().withdraw() # dont know what this is, saw online
    fpath = filedialog.askdirectory(
        title="savesigma"
    )
    fname = f"foo.txt"
    cons = txt.get("1.0", "end-1c")

    try:
        with open(fname, "w") as file:
         file.write(cons)
    except IOError as e:
        print(f"error writing to file: {e}")

def ope(event=None):
    t.Tk().withdraw()
    fpath = filedialog.askopenfilename(
        title="opensigma",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*")]
    )
    try:
     with open(fpath, "r") as file:
        cons = file.read()
        txt.insert(t.END, cons)
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "File not found")
    except PermissionError:
        messagebox.showerror("Permission Denied", 
        "yeah no, come on diddy blud I can't access this file! Is it sussy, like a sigma?")

def undo(event=None):
    try:
        txt.edit_undo()
    except t.TclError:
        pass
        messagebox.showerror("None", "nothing to undo, blud")
        
        
def redo(event=None):
    try:
        txt.edit_redo()
    except t.TclError:
        messagebox.showerror("None", "nothing to redo, blud")        

def secall(event=None):
    txt.tag_add(SEL, "1.0", END)
    txt.mark_set(INSERT, "1.0")
    txt.see(INSERT)
    return 'break'

def close(event=None):
    global wname
    check = txt.get("1.0", "end-1c")
    if check:
        fname = f"{wname}.txt"
        die = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.join(die, fname)
        os.path.exists(fpath)
        with open(fpath, "r") as file:
           cons = file.read()
           if cons == check:
             root.destroy()
             nm.destroy() 
           else:
             messagebox.showerror("Unsaved", "blud, you haven't saved ts file yet. If ts is an error, pull up an issue on trollsigma's github page.")
    else:
      root.destroy()
      nm.destroy()  

    

def find(event=None):
    global spa
    global nuxt

    fn = t.Toplevel(root)
    fn.title("findsigma")
    fn.geometry("300x150")
    fn.maxsize(300, 150)
    def gettxt():
       txt.tag_remove("highlight", "1.0", END)
       spa = nuxt.get()
       count = 0
       sindex = "1.0"
       mlen = t.IntVar()
       while True:
        if spa:
         mlen.set(0)
         sidx = txt.search(
             spa,
             sindex,
             stopindex=t.END,
             nocase=True,
             count=mlen,
             regexp=False
         )
         if sidx:
            manlen = mlen.get()
            if manlen == 0:
             print("something went wrong")
             sindex = f"{sidx}+1c"

         edx = f"{sidx}+{manlen}c"
         txt.tag_add("highlight", sidx, edx)
         count += 1
         sindex = edx 
        else:
            print("no match, breaking.")
            break
     
        def cls():
            txt.tag_remove("highlight", "1.0", END)
            fn.destroy()

        fn.protocol("WM_DELETE_WINDOW", cls)

         

    txt.tag_configure("highlight", background="yellow")

    fin = ttk.Label(fn, text="type what you find")
    fin.pack(pady=10, padx=10)
    nuxt = ttk.Entry(fn)
    nuxt.pack(pady=10)
    jfin = ttk.Button(fn, text="Find", command=gettxt)
    jfin.pack()
    fn.bind('<Return>', gettxt)


def rname(event=None):
    nf = t.Toplevel(root)
    nf.title("namesigma")
    nf.geometry("400x150")
    nf.maxsize(400, 200)
    def name(event=None):
        global wname
        grep = bo.get()
        wname = grep
        if " " in wname:
           messagebox.showerror("Can't accept that", "boi ts not tuff, you need to not include spaces. Alright, sigma?")
            
        root.title(f"{wname} | trollsigma")
        nf.destroy()

    la = t.Label(nf, text="give me name, mustard mango")
    la.pack(pady=10, padx=10)
    bo = t.Entry(nf)
    bo.pack()
    bn = t.Button(nf, text="Continue", command=name)
    bn.pack()
    nf.bind('<Return>', name)

def settings(event=None):
    sl = t.Toplevel(root)
    sl.title("setsigma")
    sl.geometry("300x300")
    sl.maxsize(300, 300)
    
    theme = ["Light", "Dark"]
    def edge():
       const = td.get()
       match const:
         case "Light":
            sv_ttk.set_theme("light")
         case "Dark":
            sv_ttk.set_theme("dark")   
          


    px = ttk.Label(sl, text="Settings", font="Arial 30")
    px.pack(side=t.TOP, pady=20)

    ask = ttk.Label(sl, text="Set theme")
    ask.pack(pady=10)

    td = ttk.Combobox(sl, values=theme)
    td.set("Dark")
    td.pack(pady=10)

    brb = ttk.Button(sl, text="Apply", command=edge)
    brb.pack(pady=(2, 40))
    later = ttk.Label(sl, text="I'll add other stuff later")
    later.pack()
    
root.minsize(400, 300)
root.title(f"{wname} | Trollsigma")
mbar = Menu(root)
root.config(menu=mbar)

trym = Menu(mbar, tearoff=False)
edit = Menu(mbar, tearoff=False)
trym.add_command(
    label='Save',
    command=save
)
trym.add_command(
    label='Save As',
    command=saveas
)
trym.add_command(
    label='Open',
    command=ope
)
trym.add_command(
    label="Close",
    command=close
)
trym.add_command(
    label="Settings",
    command=settings
)
mbar.add_cascade(
    label="Menu",
    menu=trym
)
mbar.add_cascade(
    label="Edit",
    menu=edit
)
edit.add_command(
    label="Undo",
    command=undo
)
edit.add_command(
    label="Redo",
    command=redo
)
edit.add_command(
    label="Select All",
    command=secall
)
edit.add_command(
    label="Find",
    command=find
)
edit.add_command(
    label="Rename",
    command=rname
)
acord = t.StringVar()
acord.set("Words: 0")
txt = scrolledtext.ScrolledText(root, wrap=t.WORD, width=50, height=20, undo=True, autoseparators=True)
txt.pack(pady=1, 
         padx=10,
         fill=t.BOTH,
         expand=True)

led = ttk.Label(root, textvariable=acord, font="Arial 10")
led.pack()
count()
root.bind('<Control-s>', save)
root.bind('<Control-o>', ope)
root.bind('<Control-a>', saveas)
root.bind('<Command-s>', save)
root.bind('<Command-o>', ope)
root.bind('<Command-a>', saveas)
root.bind('<Control-z>', undo)
root.bind('<Command-z>', undo)
root.bind('<Control-b>', redo)
root.bind('<Command-b>', redo)
root.bind('<Control-d>', secall)
root.bind('<Command-d>', secall)
root.bind('<Control-q>', close)
root.bind('<Command-q>', close)
root.bind('<Control-f>', find)
root.bind('<Command-f>', find)
root.bind('<Control-h>', settings)
root.bind('<Command-h>', settings)
root.bind('<Control-r>', rname)
root.bind('<Command-r>', rname)

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
