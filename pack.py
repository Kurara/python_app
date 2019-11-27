#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometría (pack)

class Aplicacion():
    def __init__(self):
        self.root = Tk()
        self.root.title("Acceso")
        
        # Cambia el formato de la fonte_grossa actual a negrita para
        # resaltar las dos etiquetas que acompañan a las cajas
        # de entrada. (Para este cambio se ha importado el  
        # módulo 'font' al comienzo del programa):
        
        fonte_grossa = font.Font(weight='bold')
        fonte_light = font.Font(weight='bold', size=10)
        
        # Define las etiquetas que acompañan a las cajas de
        # entrada y asigna el formato de fonte_grossa anterior: 
                               
        self.lbl_user = ttk.Label(self.root, text="User:", 
                               font=fonte_grossa)
        self.lbl_password = ttk.Label(self.root, text="Password:", 
                               font=fonte_grossa)
        
        # Declara dos variables de tipo cadena para contener
        # el usuario y la contraseña: 
        
        self.usuario = StringVar()
        self.clave = StringVar()
        
        # Realiza una lectura del nombre de usuario que 
        # inició sesión en el sistema y lo asigna a la
        # variable 'self.usuario' (Para capturar esta
        # información se ha importando el módulo getpass
        # al comienzo del programa):
        
        self.usuario.set(getpass.getuser())
        
        # Define dos cajas de entrada que aceptarán cadenas
        # de una longitud máxima de 30 caracteres.
        # A la primera de ellas 'self.txt_user' que contendrá
        # el nombre del usuario, se le asigna la variable
        # 'self.usuario' a la opción 'textvariable'. Cualquier
        # valor que tome la variable durante la ejecución del
        # programa quedará reflejada en la caja de entrada.
        # En la segunda caja de entrada, la de la contraseña,
        # se hace lo mismo. Además, se establece la opción
        # 'show' con un "*" (asterisco) para ocultar la 
        # escritura de las contraseñas:
        
        self.txt_user = ttk.Entry(self.root, 
                                textvariable=self.usuario, 
                                width=30, font=fonte_light)
        self.txt_password = ttk.Entry(self.root, 
                                textvariable=self.clave, 
                                width=30, show="*", font=fonte_light)
        self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL)
        
        # Se definen dos botones con dos métodos: El botón
        # 'Aceptar' llamará al método 'self.aceptar' cuando
        # sea presionado para validar la contraseña; y el botón
        # 'Cancelar' finalizará la aplicación si se llega a
        # presionar:
        
        self.btn_ok = ttk.Button(self.root, text="Aceptar", 
                                 command=self.aceptar)
        self.btn_ko = ttk.Button(self.root, text="Cancelar", 
                                 command=quit)
                                 
        # Se definen las posiciones de los widgets dentro de
        # la ventana. Todos los controles se van colocando 
        # hacia el lado de arriba, excepto, los dos últimos, 
        # los botones, que se situarán debajo del último 'TOP':
        # el primer botón hacia el lado de la izquierda y el
        # segundo a su derecha.
        # Los valores posibles para la opción 'side' son: 
        # TOP (arriba), BOTTOM (abajo), LEFT (izquierda)
        # y RIGHT (derecha). Si se omite, el valor será TOP
        # La opción 'fill' se utiliza para indicar al gestor
        # cómo expandir/reducir el widget si la ventana cambia
        # de tamaño. Tiene tres posibles valores: BOTH
        # (Horizontal y Verticalmente), X (Horizontalmente) e 
        # Y (Verticalmente). Funcionará si el valor de la opción
        # 'expand' es True.
        # Por último, las opciones 'padx' y 'pady' se utilizan
        # para añadir espacio extra externo horizontal y/o 
        # vertical a los widgets para separarlos entre sí y de 
        # los bordes de la ventana. Hay otras equivalentes que
        # añaden espacio extra interno: 'ipàdx' y 'ipady':
                                         
        self.lbl_user.pack(side=TOP, fill=X, expand=True, 
                        padx=5, pady=5)
        self.txt_user.pack(side=TOP, fill=X, expand=True, 
                         padx=5, pady=5)
        self.lbl_password.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=5, pady=5)
        self.txt_password.pack(side=TOP, fill=X, expand=True, 
                         padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.btn_ok.pack(side=LEFT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.btn_ko.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        
        # Cuando se inicia el programa se asigna el foco
        # a la caja de entrada de la contraseña para que se
        # pueda empezar a escribir directamente:
                
        self.txt_password.focus_set()
        
        self.root.mainloop()
    
    # El método 'aceptar' se emplea para validar la 
    # contraseña introducida. Será llamado cuando se 
    # presione el botón 'Aceptar'. Si la contraseña
    # coincide con la cadena 'tkinter' se imprimirá
    # el mensaje 'Acceso permitido' y los valores 
    # aceptados. En caso contrario, se mostrará el
    # mensaje 'Acceso denegado' y el foco volverá al
    # mismo lugar.
    
    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.txt_user.get())
            print("Contraseña:", self.txt_password.get())
        else:
            print("Acceso denegado")
            
            # Se inicializa la variable 'self.clave' para
            # que el widget 'self.txt_password' quede limpio.
            # Por último, se vuelve a asignar el foco
            # a este widget para poder escribir una nueva
            # contraseña.
            
            self.clave.set("")
            self.txt_password.focus_set()

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()