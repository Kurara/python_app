#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometría (grid). Ventana dimensionable

class Aplicacion():
    def __init__(self):
        self.root = Tk()
        self.root.title("Acceso")
        fuente = font.Font(weight='bold')  
        self.cornice = ttk.Frame(self.root, borderwidth=2,
                               relief="raised", padding=(10,10))
        self.etiq1 = ttk.Label(self.cornice, text="Usuario:", 
                               font=fuente, padding=(5,5))
        self.etiq2 = ttk.Label(self.cornice, text="Contraseña:", 
                               font=fuente, padding=(5,5))
        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set(getpass.getuser())        
        self.ctext1 = ttk.Entry(self.cornice, textvariable=self.usuario,
                                width=30)
        self.ctext2 = ttk.Entry(self.cornice, textvariable=self.clave,
                                show="*", width=30)
        self.separ1 = ttk.Separator(self.cornice, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.cornice, text="Aceptar", 
                                 padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(self.cornice, text="Cancelar", 
                                 padding=(5,5), command=quit)
        
        # Para conseguir que la cuadricula y los widgets se 
        # adapten al contenedor, si se amplia o reduce el tamaño
        # de la ventana, es necesario definir la opción 'sticky'.
        # Cuando un widget se ubica en el grid se coloca en el
        # centro de su celda o cuadro. Con 'sticky' se
        # establece el comportamiendo 'pegajoso' que tendrá el 
        # widget dentro de su celda, cuando se modifique la 
        # dimensión de la ventana. Para ello, se utilizan para
        # expresar sus valores los puntos cardinales: N (Norte),
        # S (Sur), (E) Este y (W) Oeste, que incluso se pueden
        # utilizar de forma combinada. El widget se quedará 
        # 'pegado' a los lados de su celda en las direcciones
        # que se indiquen. cuando la ventana cambie de tamaño. 
        # Pero con definir la opción 'sticky' no es suficiente: 
        # hay activar esta propiedad más adelante.
        
        self.cornice.grid(column=0, row=0, padx=5, pady=5, 
                        sticky=(N, S, E, W))
        self.etiq1.grid(column=0, row=0, 
                        sticky=(N, S, E, W))
        self.ctext1.grid(column=1, row=0, columnspan=2, 
                         sticky=(E, W))
        self.etiq2.grid(column=0, row=1,
                        sticky=(N, S, E, W))
        self.ctext2.grid(column=1, row=1, columnspan=2, 
                         sticky=(E, W))
        self.separ1.grid(column=0, row=3, columnspan=3, pady=5, 
                         sticky=(N, S, E, W))
        self.boton1.grid(column=1, row=4, padx=5, 
                         sticky=(E))
        self.boton2.grid(column=2, row=4, padx=5, 
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