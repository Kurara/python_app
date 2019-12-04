#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometría (grid). Finestra dimensionabile

class Aplicacion():
    def __init__(self):
        self.root = Tk()
        self.root.title("Acceso")
        fuente = font.Font(weight='bold')  
        self.cornice = ttk.Frame(self.root, borderwidth=2,
                               relief="raised", padding=(10,10))
        self.label1 = ttk.Label(self.cornice, text="Usuario:", 
                               font=fuente, padding=(5,5))
        self.label2 = ttk.Label(self.cornice, text="Contraseña:", 
                               font=fuente, padding=(5,5))
        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set(getpass.getuser())        
        self.ctext1 = ttk.Entry(self.cornice, textvariable=self.usuario,
                                width=30)
        self.ctext2 = ttk.Entry(self.cornice, textvariable=self.clave,
                                show="*", width=30)
        self.separ1 = ttk.Separator(self.cornice, orient=HORIZONTAL)
        self.btn1 = ttk.Button(self.cornice, text="Aceptar", 
                                 padding=(5,5), command=self.aceptar)
        self.btn2 = ttk.Button(self.cornice, text="Cancelar", 
                                 padding=(5,5), command=quit)
        
        # Per riuscire che la grid e i widget si adattino al
        # contenitore nel momento che la finestra si fa grande
        # o si rimpiciolisce, bisogna definire la opzione 'sticky'.
        # Quando un widget si ubica nel grid, si mette nel centro 
        # della sua cella o quadro. Con 'sticky' si
        # stabilisce il suo comportamento 'appiccicoso' che avrà il
        # widget dentro della sua cella, quando si modifichi la 
        # dimensione della finestra. Per questo, si utilizerà
        # i punti cardinali: N (Nord), S (Sud), (E) Est e (W) Ovest,
        # si possono anche combinare. Il widget rimarrà 
        # 'incollato' ai suoi lati della cella nelle direzioni
        # che si indichino quando la finestra cambila sua dimensione. 
        # Pero serve attivare anche quello che vedremmo sotto.
        
        self.cornice.grid(column=0, row=0, padx=5, pady=5, 
                        sticky=(N, S, E, W))
        self.label1.grid(column=0, row=0, 
                        sticky=(N, S, E, W))
        self.ctext1.grid(column=1, row=0, columnspan=2, 
                         sticky=(E, W))
        self.label2.grid(column=0, row=1,
                        sticky=(N, S, E, W))
        self.ctext2.grid(column=1, row=1, columnspan=2, 
                         sticky=(E, W))
        self.separ1.grid(column=0, row=3, columnspan=3, pady=5, 
                         sticky=(N, S, E, W))
        self.btn1.grid(column=1, row=4, padx=5, 
                         sticky=(E))
        self.btn2.grid(column=2, row=4, padx=5, 
                         sticky=(W))

        # A continuación, se activa la propiedad de expandirse
        # o contraerse definida antes con la opción
        # 'sticky' del método grid().
        # La activación se hace por contenedores y por filas
        # y columnas asignando un peso a la opción 'weight'.
        # Esta opción asigna un peso (relativo) que se utiliza
        # para distribuir el espacio adicional entre columnas
        # y/o filas. Cuando se expanda la ventana, una columna
        # o fila con un peso 2 crecerá dos veces más rápido
        # que una columna (o fila) con peso 1. El valor
        # predeterminado es 0 que significa que la columna o
        # o fila no crecerá nada en absoluto. 
        # Lo habitual es asignar pesos a filas o columnas donde 
        # hay celdas con widgets.

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.cornice.columnconfigure(0, weight=1)
        self.cornice.columnconfigure(1, weight=1)
        self.cornice.columnconfigure(2, weight=1)
        self.cornice.rowconfigure(0, weight=1)
        self.cornice.rowconfigure(1, weight=1)
        self.cornice.rowconfigure(4, weight=1)
        
        # Establece el foco en la caja de entrada de la
        # contraseña.
        
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