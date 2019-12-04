from tkinter import *
from tkinter import ttk, font
from tkinter import messagebox
import os

base_path = os.path.dirname(os.path.abspath(__file__))
app_name = 'personalapp' # NOTE: Modify also spec file!!!


class AppWithBinds:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x290")
        self.root.resizable(1,1)
        self.root.configure(bg = '#D91818')

        self.num2 = IntVar()
        self.num1 = IntVar()
        self.textResult = StringVar()
        self.icon = PhotoImage(data="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")

        self.firstValue = Spinbox(
            self.root, from_=1, to=100, wrap=True,
            textvariable=self.num1, 
            command=self.calcolare
        ) 
        self.secondValue = Spinbox(
            self.root, from_=1, to=100, wrap=True,
            textvariable=self.num2, 
            command=self.calcolare
        )
        self.img_apple = Label(self.root, image=self.icon, 
                      relief='raised')

        self.lvlResult = ttk.Label(
            self.root, text="", padding=(5,5), textvariable=self.textResult
        )
        self.lista_1 = Listbox(self.root)

        self.filemenu = Menu(self.root, tearoff=0)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")

        self.main_menu = Menu(self.root)
        self.main_menu.add_cascade(label="File", menu=self.filemenu)

        self.img_apple.place(relx=0, rely=0)
        self.lista_1.place(y=0, relx=0.5)
        
        self.firstValue.place(x=0, y=230, relx=0, rely=0)
        self.secondValue.place(x=0, y=230, relx=0.5, rely=0)
        self.lvlResult.place(y=200, relx=0.5)
        
        self.textResult.trace('w', self.prova)

        self.lista_1.bind('<Double-Button-1>', self.color)
        self.lista_1.bind('<B1-Motion>', self.color)
        self.lista_1.bind('<Button-3>', self.color)

        self.root.config(menu=self.main_menu)
        self.root.mainloop()

    def calcolare(self, *args):
        result = self.num1.get() + self.num2.get()
        self.textResult.set(str(result))

    def prova(self, *args):
        if int(self.textResult.get()) % 2 == 0:
            messagebox.showinfo("Numero Pari!", self.textResult.get())

    def color(self, *args):
        action = "Non catturata :("
        if 'ButtonPress' in str(args[0]):
            if 'num=3' in str(args[0]):
                action = "Singolo click"
            elif 'num=1' in str(args[0]):
                action = "Doppio click"
        if 'Motion' in str(args[0]):
            action = "Motion"
        self.lista_1.insert(END, action)
    

if __name__ == '__main__':
    app = AppWithBinds()
    # return 0