import random

letras_Minusculas= ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z']

letras_Mayusculas= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

Simbolos = ['!', '#', '$', '%', '(', ')', '*', '+', '/']

Numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("bienvenido a tu generesador de Contraseña \n")

entrada_letras_Minusculas = int(input("ingrese el numero de letras Minusculas que desea para su contaseña: "))

entrada_letras_Mayusculas = int(input("ingrese el numero de letras  Mayusculas que desea para su contaseña: "))

entrada_Simbolos =int(input("ingrese el numero de simbolo que desea para su contaseña: "))

entrada_Numeros = int(input("ingrese el numero de numeros que desea para su contaseña: "))

password_lista = []

for carater_aleatorio in range(1, entrada_letras_Minusculas + 1):
    password_lista.append(random.choice(letras_Minusculas))


for carater_aleatorio in range(1, entrada_letras_Mayusculas + 1):
    password_lista.append(random.choice(letras_Mayusculas))
  

for caracter_aleatorio in range(1, entrada_Simbolos + 1):
   password_lista.append(random.choice(Simbolos))
   

for caracter_aleatorio in range(1, entrada_Numeros + 1):
   password_lista.append(random.choice(Numeros))

password_string = ""

for final in password_lista:
    password_string += final

print("su contraseña aleatoria es: " + password_string)
