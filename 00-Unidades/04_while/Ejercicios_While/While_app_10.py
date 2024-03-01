import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Rocio Ayelen
apellido:Pacheco
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        cont_negativo = 0
        cont_positivo = 0
        acu_positivo = 0
        acu_negativo = 0
        cont_cero = 0

        while True:
            numero = prompt("","Ingrese un número")
            if numero == None:
                break
            numero = int(numero)

            if numero > 0:
                acu_positivo += numero
                cont_positivo += 1
            elif numero < 0:
                acu_negativo += numero
                cont_negativo += 1
            elif numero == 0:
                cont_cero += 1

            diferencia = cont_negativo - cont_positivo

        alert("",f"suma acumulada de los negativos {acu_negativo},La suma acumulada de los positivos {acu_positivo},Cantidad de números positivos ingresados{cont_positivo}, Cantidad de números negativos ingresados{cont_negativo}, Cantidad de ceros {cont_cero}, diferencia {diferencia}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
