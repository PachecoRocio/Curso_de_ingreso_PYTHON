import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Rocio AYelen
apellido: Pacheco
---
De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:
Nombre
Categoría (Principiante - Intermedio - Avanzado)
Edad (entre 18 y 99 inclusive)
Score (mayor que 0)
Nivel alcanzado (1 , 2 o 3)

Pedir datos por prompt y mostrar por print, se debe informar:

Informe A- Cuál es el nivel más alcanzado de los jugadores
Informe B- El Porcentaje de jugadores de la categoría principiante sobre el total
Informe C- La categoría del participante de mayor edad
Informe D- El score y nombre del principiante con mayor score
Informe E- Promedio de score de los participantes intermedios.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        

    def btn_mostrar_on_click(self):
        cont_part = 0
        #ej 1
        cont_nivel_1 = 0
        cont_nivel_2 = 0
        cont_nivel_3 = 0
        mayor_nivel = 0
        #ej 2
        porc_principiante = 0
        cont_princ = 0
        cont_avan = 0
        #ej 3
        bandera_edad = 0
        mayor_edad = 0
        cat_mayor_edad = 0
        #ej 4
        bandera_score= False
        mayor_score = 0
        mayor_score_nombre =""
        #ej 5
        prom_inter : 0
        cont_inter = 0
        score_inter = 0


        while cont_part < 5:

            nombre = prompt("","Ingrese nombre")
            
            while nombre == "":
                nombre = prompt("","Ingrese nombre")

            categoria= prompt("","Ingrese categoría")
            while categoria != "Principiante" and categoria != "Intermedio" and categoria != "Avanzado":
                categoria= prompt("","Ingrese categoría")
            
            edad = int(prompt("","ingrese un edad"))
            while edad > 99 or edad < 18:
                edad = int(prompt("","Ingrese edad"))
            
            score = int(prompt("","Ingrese score"))
            while score < 0:
                score = int(prompt("","Ingrese score"))

            nivel = int(prompt("","Ingrese nivel"))
            while nivel != 1 and nivel != 2 and nivel != 3:
                nivel = int(prompt("","Ingrese nivel"))

            #contador categorias
            match categoria:
                case "Principiante":
                    cont_princ += 1
                    
                    #Mayor score
                    if score > mayor_score or bandera_score == False:
                        mayor_score = score
                        mayor_score_nombre = nombre
                        bandera_score = True

                case "Intermedio":
                    cont_inter += 1
                    score_inter += score
                case  "Avanzado":
                    cont_avan += 1

            #contador niveles
            match nivel:
                case 1:
                    cont_nivel_1 += 1
                case 2:
                    cont_nivel_2 += 1
                case 3:
                    cont_nivel_3 +=1

            cont_part += 1
        
            #Mayor nivel
            if cont_nivel_2 < cont_nivel_1:
                mayor_nivel = 1
            elif cont_nivel_3 < cont_nivel_2:
                mayor_nivel = 2
            else:
                mayor_nivel = 3

            #Mayor edad
            if edad >mayor_edad or bandera_edad == False:
                mayor_edad = edad
                cat_mayor_edad = categoria
                bandera_edad = True 
            
          
        porc_principiante = (cont_princ / 100) * cont_part

        if cont_inter > 0:
            prom_inter= score_inter / cont_inter
        else:
            prom_inter = 0
        
       
        print(f"el nivel más alcanzado de los jugadores: {mayor_nivel}")
        print(f"Porcentaje de jugadores de la categoría principiante sobre el total: {porc_principiante}")
        print(f"La categoría del participante de mayor edad: {cat_mayor_edad}")
        print(f"El score y nombre del principiante con mayor score: {mayor_score}, {mayor_score_nombre}")
        print(f"Promedio de score de los participantes intermedios {prom_inter}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()