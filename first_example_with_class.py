#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk


class Aplicacion():
    def __init__(self):
        root = Tk()
        root.geometry('300x200')
        root.configure(bg = 'beige')
        root.title('Aplicación')
        ttk.Button(root, text='Salir', 
                   command=root.destroy).pack(side=BOTTOM)
        root.mainloop()


def main():
    mia_app = Aplicacion()
    return 0

# Se il modulo ('__name__ ' è una variabile che ritorna il modulo di python)
# è chiamato direttamente e non importato, esegue la funzione main()

if __name__ == '__main__':
    main()