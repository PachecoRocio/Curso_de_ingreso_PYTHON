import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4) = 7

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9. 9-7 = 2

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=6, pady=10, columnspan=2, sticky="nsew")
    
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        self.lista_nombre = ["Pepe", "Paola", "Dardo", "Fatiga", "Maria"]
        self.lista_monto = [20000,30000,40000,50000,60000]
        self.lista_tipo_instrumento = ["CEDEAR","BONOS","MEP","CEDEAR","CEDEAR"]
        self.lista_cantidad_instrumento = [20, 35, 199, 100, 80]
    
    def btn_cargar_datos_on_click(self):
        seguir = True
        cont_mep = 0
        cont_bonos = 0
        cont_cedear = 0
        cont_cliente = 0
        menos_operado = ""
        mas_operado = ""
        cont_no_cedear = 0

        while seguir == True:
            nombre = prompt("","Ingrese su nombre")

            monto = int(prompt("","Ingrese monto en pesos"))
            while monto < 10000:
                monto = int(prompt("","Ingrese monto en pesos"))
            
            tipo= prompt("","Ingrese tipo de instrumento")
            while tipo != "cedear" and tipo != "bonos" and tipo != "mep":
                tipo= prompt("","Ingrese tipo de instrumento")
            
            cant = int(prompt("","Cantidad de instrumentos "))
            while cant < 0:
                cant = int(prompt("","Cantidad de instrumentos "))

            match tipo:
                case "cedear":
                    cont_cedear += 1
                case "bonos":
                    cont_bonos +=1
                case "mep":
                    cont_mep += 1
            
            cont_cliente += 1

            seguir = question("","desea seguir?")

        if cont_bonos < cont_cedear:
            menos_operado = "bonos"
        elif cont_cedear < cont_mep:
            menos_operado = "cedear"
        else:
            menos_operado = "mep"
        
        if cont_bonos > cont_cedear:
            mas_operado = "bonos"
        elif cont_cedear > cont_mep:
            mas_operado = "cedear"
        else:
            mas_operado = "mep"
        
        cont_no_cedear = cont_cliente - cont_cedear

        print(cont_cliente)
        print(f"Tipo de instrumento que menos se operó {menos_operado}")
        print(f"Tipo de instrumento que mas se operó {mas_operado}")
        print(f"Cantidad de usuarios que no compraron CEDEAR {cont_no_cedear}")
        

    def btn_mostrar_informe_1(self):
        pass
        


    def btn_mostrar_informe_2(self):
        pass
        


    def btn_mostrar_informe_3(self):
        pass      


    def btn_mostrar_todos_on_click(self):
        pass

        

if __name__ == "__main__":
    app = App()
    app.mainloop()
