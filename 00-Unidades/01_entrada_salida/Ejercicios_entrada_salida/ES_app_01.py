import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lara 
apellido: Godoy
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_01
---

Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

Nombre

Edad (debe ser mayor a 12)

Altura (no debe ser negativa)

Días que asiste a la semana (1, 3, 5)

Kilos que levanta en peso muerto (no debe ser cero, ni negativo)



No sabemos cuántos clientes serán consultados.

Se debe informar al usuario:

El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

El porcentaje de clientes que asiste solo 1 día a la semana.

Nombre y edad del cliente con más altura.

Determinar si los clientes eligen más ir 1, 3 o 5 días

Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
        seguir = True

        kilos_total = 0
        cantidad_clientes_tres = 0
        cantidad_clientes = 0
        cantidad_clientes_uno = 0

        cantidad_clientes_cinco = 0
        dia_concurrido = None
        
        bandera_primer_ing = False
        altura_max = 0
        nombre_mas_alto=""

        edad_mas_joven= 0
        nombre_mas_joven=""
        peso_mas_joven=0

        
        while seguir==True:

            nombre = prompt("","ingrese nombre")


            edad = int(prompt("","ingrese un edad"))

            while edad < 13 :
            
                edad = int(prompt("","ingrese un edad"))
                
            
            altura = float(prompt("","ingrese un altura"))

            while altura <= 0 :
                altura = float(prompt("","ingrese un altura"))

            dias = int(prompt("","ingrese un dia"))

            while dias != 1 and dias != 3 and dias != 5 :
            
                dias =  int(prompt("","ingrese un dia"))

            peso_muerto = float(prompt("","ingrese un peso_muerto"))

            while peso_muerto < 1 :
                peso_muerto = float(prompt("","ingrese un peso_muerto"))

            #El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
            if dias == 3:
                kilos_total += peso_muerto
                cantidad_clientes_tres += 1

            elif dias == 1:
            #El porcentaje de clientes que asiste solo 1 día a la semana.
                cantidad_clientes_uno += 1
            #El porcentaje de clientes que asiste solo 1 día a la semana.
            else:
                cantidad_clientes_cinco += 1

            cantidad_clientes += 1

            # if bandera_primer_ing == False:
            #     altura_max = altura
            #     nombre_mas_alto =nombre
            #     edad_persona_alta = edad
            #     bandera_primer_ing = True

            # elif altura >= altura_max:
            #     altura_max = altura
            #     nombre_mas_alto =nombre
            #     edad_persona_alta = edad
            if altura > altura_max or bandera_primer_ing == False: 
                altura_max = altura
                nombre_mas_alto =nombre
                edad_persona_alta = edad
                bandera_primer_ing = True

                
            seguir = question("","desea seguir?")

        if cantidad_clientes_cinco > cantidad_clientes_tres and cantidad_clientes_cinco > cantidad_clientes_uno:
            dia_concurrido = "Dia 5"
        elif cantidad_clientes_tres > cantidad_clientes_uno:
            dia_concurrido = "Dia 3"
        else:
            dia_concurrido = "Dia 1"

        if (edad > edad_mas_joven or bandera_primer_ing == False) and dias == 5: 
                edad_mas_joven = edad
                nombre_mas_joven = nombre
                peso_mas_joven = peso_muerto
                bandera_primer_ing = True
                
        if cantidad_clientes_tres > 0:
            promedio_kilos_tres = kilos_total / cantidad_clientes_tres
        else:
             promedio_kilos_tres = 0

        porcentaje_clientes_1 = ( cantidad_clientes_uno / 100)*cantidad_clientes
        print(f"El promedio de kilos que levantan las personas que asisten solo 3 días a la semana: {promedio_kilos_tres}")
        print(f"El porcentaje de clientes que asiste solo 1 día a la semana es {porcentaje_clientes_1}")
        print(f"El día mas concurrido fue el: {dia_concurrido}")
        print(f"El mas joven: {nombre_mas_joven}, {peso_mas_joven}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

    

