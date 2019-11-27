#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *    # Carica il modulo tk (widgets standard)
from tkinter import ttk  # Carica ttk (per i nuovi widgets 8.5+)

# Istancia la finestra principale dell'app

root = Tk()

# Definisce le dimensioni della finestra.
# Se non si specifica, la finestra verrà adattata ai
# widgets che saranno contenuti su di essa

root.geometry('300x200') # altezza x ampiezza

# Assegna un colore allo sfondo della finestra.
# Se non specifichiamo niente, lo sfondo sarà grigio

root.configure(bg = 'beige')

# Titolo della finestra

root.title('Aplicación')

# Bottone per uscire del programma
# Il primo parametro indica dove si
# ubicherà il bottone, in questo caso la finestra 'root'

ttk.Button(root, text='Salir', command=quit).pack(side=BOTTOM)

# Questa funzione construisce e mostra la finestra

root.mainloop()