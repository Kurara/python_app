#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass

# Gestore geometrico (grid). Finestra no dimensionabile

class Aplicacion():
    def __init__(self):
        self.root = Tk()
        self.root.title("Acceso")
        
        # In questa funzione si imposibilita la ridimensione
        # della finestra, già che 0 = False
        
        self.root.resizable(0,0)
        fuente = font.Font(weight='bold')
        
        # Definisce un widget di tipo 'Frame' (cornice) cha farà
        # di contenitore del resto di widgets. Sarà situato
        # dentro di 'self.root'.
        # Ha un bordo di 2 pixel e il valore relief="raised" le
        # da un effeto 3D al bordo.
        # Posibili valori:
        # FLAT (piato), RAISED (rialzato), SUNKEN (),
        # GROOVE () y RIDGE ().
        # 'padding' è lo spazio interiore fra i widget e il cornice.
          
        self.cornice = ttk.Frame(self.root, borderwidth=2,
                               relief="raised", padding=(10,10))
                               
        # Definisce il resto di widget dentro a 'cornice'
                               
        self.etiq1 = ttk.Label(self.cornice, text="User:", 
                               font=fuente, padding=(5,5))
        self.etiq2 = ttk.Label(self.cornice, text="Password:",
                               font=fuente, padding=(5,5))
                               
        # Definisce variabili per 'textvariable'
        
        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set(getpass.getuser())        
        self.ctext1 = ttk.Entry(self.cornice, textvariable=self.usuario, 
                                width=30)
        self.ctext2 = ttk.Entry(self.cornice, textvariable=self.clave, 
                                show="*", 
                                width=30)
        self.separ1 = ttk.Separator(self.cornice, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.cornice, text="Aceptar", 
                                 padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(self.cornice, text="Cancelar", 
                                 padding=(5,5), command=quit)
        
        # Definisce l'ubicazione di ogni widget nella grid.
        # In questo esempio, ci sono 2 grid:
        # Uno di 1fx1c dentro della finestra dove verrà messo
        # il Frame; e altra nel Frame di 5fx3c per il resto 
        # di widgets.
        # La prima riga  e la prima colonna stanno nel numero 0.
        # La opzione 'column' indica il numero di colonna e la
        # opzione 'row' indica il numero di riga dove
        # colochiamo i widget.
        # La opzione 'columnspan' indica che il
        # widget ocuperà il numero scelto di colonne.
        
        self.cornice.grid(column=0, row=0)
        self.etiq1.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.etiq2.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.separ1.grid(column=0, row=3, columnspan=3)
        self.boton1.grid(column=1, row=4)
        self.boton2.grid(column=2, row=4)

        # Stabilisce il foco sulla password

        self.ctext2.focus_set()
        self.root.mainloop()
    
    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Access granted!")
            print("User:   ", self.ctext1.get())
            print("Password:", self.ctext2.get())
        else:
            print("Forbidden Access")
            self.clave.set("")
            self.ctext2.focus_set()

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()