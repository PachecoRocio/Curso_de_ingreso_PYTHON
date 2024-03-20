import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
nombre: Rocio Ayelen
apellido: Pacheco
---

De los 11 Jugadores de fútbol se debe ingresar los siguientes datos:
Nombre
Categoría (amateur - profesional - retirado )
Edad (entre 18 y 99 inclusive)
goles puede ser cero
Número de camiseta del 0 al 100

Pedir datos por prompt y mostrar por print, se debe informar:

Informe A- Cuál hay más , mayores a 25 años o menores
Informe B- El Porcentaje de jugadores con más de dos goles
Informe C- El nombre y número del jugador de la categoría retirado más joven
Informe D- los goles y nombre del profesional con más goles
Informe E- Promedio de goles de los jugadores mayores a 25
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        cont_jugadores = 0
        #categoria
        cont_amateur = 0
        cont_prof = 0
        cont_reti = 0

        cont_mayor_edad = 0
        cont_menor_edad = 0
        mayor_cant_edad = ""

        cont_dos_goles = 0
        porc_goles = 0

        bandera_joven = False
        cat_ret_joven = 0
        nombre_joven = ""
        camiseta_joven = 0

        bandera_goles = False
        prof_mas_gol = 0
        nombre_mas_goles = ""
      
        prom_goles = 0
        acu_goles = 0

        for cont_jugadores in range(11):
            nombre = prompt("","Ingrese nombre")
            
            while nombre == "":
                nombre = prompt("","Ingrese nombre")

            categoria= prompt("","Ingrese categoría")
            while categoria != "amateur" and categoria != "profesional" and categoria != "retirado":
                categoria= prompt("","Ingrese categoría")
            
            edad = int(prompt("","ingrese un edad"))
            while edad > 99 or edad < 18:
                edad = int(prompt("","Ingrese edad"))

            goles = int(prompt("","ingrese cantidad de goles"))
            while goles < 0:
                goles = int(prompt("","Ingrese cantidad de goles"))

            camiseta = int(prompt("","ingrese número de camiseta"))
            while camiseta > 100 or edad < 0:
                camiseta = int(prompt("","Ingrese número de camiseta"))
            
            match categoria:
                case "amateur":
                    cont_amateur += 1
                case "profesional":
                    cont_prof += 1 b

                    if prof_mas_gol < goles or bandera_goles == False:
                        prof_mas_gol = goles
                        nombre_mas_goles = nombre
                        bandera_goles = True

                case  "retirado":
                    cont_reti += 1

                    if cat_ret_joven < edad or bandera_joven == False:
                        cat_ret_joven = edad
                        nombre_joven = nombre
                        camiseta_joven = camiseta
                        bandera_joven = True
            if goles > 2:
                cont_dos_goles += 1

            cont_jugadores += 1

            if edad < 25:
                cont_menor_edad += 1
            else:
                cont_mayor_edad += 1
                acu_goles += goles

            if cont_menor_edad < cont_mayor_edad:
                mayor_cant_edad = "Hay mas jugadores mayores a 25"
            else:            
                mayor_cant_edad = "Hay mas jugadores menores a 25"


        porc_goles = ( cont_dos_goles / 100) * cont_jugadores

        if cont_mayor_edad > 0:
            prom_goles =  acu_goles / cont_mayor_edad
        else:
            prom_goles = 0

        print(mayor_cant_edad)
        print(f"El Porcentaje de jugadores con más de dos goles es: {porc_goles}%")
        print(f"El nombre y número del jugador de la categoría retirado más joven: {nombre_joven} ,{camiseta_joven}")
        print(f"Los goles y nombre del profesional con más goles: {prof_mas_gol}, {nombre_mas_goles}")
        print(f"Promedio de goles de los jugadores mayores a 25: {prom_goles}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

    

