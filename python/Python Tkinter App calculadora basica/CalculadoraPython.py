from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

indice = 0

#Entrada
entrada_texto = Entry(ventana, font= ("Calibri 20") )
entrada_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#Funciones

def click_Boton(valor):
    global indice
    entrada_texto.insert(indice, valor)
    indice+= 1

def borrar():
    entrada_texto.delete(0, END)
    indice= 0

def hacer_operaciones():
    ecuacion = entrada_texto.get()
    resultado = eval(ecuacion)
    entrada_texto.delete(0, END)
    entrada_texto.insert(0, resultado)
    indice=0

# Botones

boton1 = Button(ventana, text = "1", width = 5,height = 2, command = lambda: click_Boton(1))
boton2 = Button(ventana, text = "2", width = 5,height = 2, command = lambda: click_Boton(2))
boton3 = Button(ventana, text = "3", width = 5,height = 2, command = lambda: click_Boton(3))
boton4 = Button(ventana, text = "4", width = 5,height = 2, command = lambda: click_Boton(4))
boton5 = Button(ventana, text = "5", width = 5,height = 2, command = lambda: click_Boton(5))
boton6 = Button(ventana, text = "6", width = 5,height = 2, command = lambda: click_Boton(6))
boton7 = Button(ventana, text = "7", width = 5,height = 2, command = lambda: click_Boton(7))
boton8 = Button(ventana, text = "8", width = 5,height = 2, command = lambda: click_Boton(8))
boton9 = Button(ventana, text = "9", width = 5,height = 2, command = lambda: click_Boton(9))
boton0 = Button(ventana, text = "0", width = 13,height = 2, command = lambda: click_Boton(0))

boton_Borrar = Button(ventana, text = "AC", width = 5,height = 2, command = lambda: borrar())
boton_Parentesis1 = Button(ventana, text = "(", width = 5,height = 2, command = lambda: click_Boton("("))
boton_Parentesis2 = Button(ventana, text = ")", width = 5,height = 2, command = lambda: click_Boton(")"))
boton_Punto = Button(ventana, text = ".", width = 5,height = 2, command = lambda: click_Boton("."))

boton_Div = Button(ventana, text = "/", width = 5,height = 2, command = lambda: click_Boton("/"))
boton_Mult = Button(ventana, text = "*", width = 5,height = 2, command = lambda: click_Boton("*"))
boton_Sum = Button(ventana, text = "+", width = 5,height = 2, command = lambda: click_Boton("+"))
boton_Rest = Button(ventana, text = "-", width = 5,height = 2, command = lambda: click_Boton("-"))
boton_Igual = Button(ventana, text = "=", width = 5,height = 2, command = lambda: hacer_operaciones())

#Agregar botones en pantalla
boton_Borrar.grid (row = 1, column = 0, padx = 5, pady = 5)
boton_Parentesis1.grid (row =1 , column = 1, padx = 5, pady = 5)
boton_Parentesis2.grid (row =1 , column = 2, padx = 5, pady = 5)
boton_Div.grid (row =1 , column = 3, padx = 5, pady = 5)

boton7.grid (row =2 , column = 0, padx = 5, pady = 5)
boton8.grid (row =2 , column = 1, padx = 5, pady = 5)
boton9.grid (row =2 , column = 2, padx = 5, pady = 5)
boton_Mult.grid (row =2 , column = 3, padx = 5, pady = 5)

boton4.grid (row =3 , column = 0, padx = 5, pady = 5)
boton5.grid (row =3 , column = 1, padx = 5, pady = 5)
boton6.grid (row = 3, column = 2, padx = 5, pady = 5)
boton_Rest.grid (row =3 , column = 3, padx = 5, pady = 5)

boton1.grid (row =4 , column =0 , padx = 5, pady = 5)
boton2.grid (row =4 , column = 1, padx = 5, pady = 5)
boton3.grid (row = 4, column = 2, padx = 5, pady = 5)
boton_Sum.grid (row = 4, column = 3, padx = 5, pady = 5)

boton0.grid (row =5 , column = 0, columnspan=  2, padx = 5, pady = 5)
boton_Punto.grid (row =5 , column = 2, padx = 5, pady = 5)
boton_Igual.grid (row =5 , column = 3, padx = 5, pady = 5)



ventana.mainloop()


