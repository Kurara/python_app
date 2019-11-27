from tkinter import *
from tkinter import ttk, font
from tkinter import messagebox


class AppWithBinds:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("430x200")
        self.root.resizable(1,1)

        self.num2 = IntVar()
        self.num1 = IntVar()
        self.textResult = StringVar()
        self.icon = PhotoImage(file="resources/apple.png")

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
        self.image = Label(self.root, image=self.icon, 
                      relief='raised')

        self.lvlResult = ttk.Label(
            self.root, text="", padding=(5,5), textvariable=self.textResult
        )
        self.lista_1 = Listbox(self.root, height=50, width=50)

        self.filemenu = Menu(self.root, tearoff=0)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")

        self.main_menu = Menu(self.root)
        self.main_menu.add_cascade(label="File", menu=self.filemenu)

        self.firstValue.place(relx=0, rely=0)
        self.secondValue.place(relx=0.5, rely=0)
        self.lvlResult.place(y=20)
        self.lista_1.place(y=50, x= 20)
        self.image.place(y=20)
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