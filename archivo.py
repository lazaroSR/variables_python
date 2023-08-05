# variable string 
saludo = "hola a todos" 

# variable int 
numero_entero = 27

# variable float
numero_real = 0.1314

# variable boolean 
numero_logico = False

resultado_0 = (f"variable string: {saludo}\nvariable int: {int(numero_entero)}\nvariable float: {numero_real}\nvariable boolean: {numero_logico}") 

# Limite de los enteros y flotantes en python
""""
los números de Python están fuertemente relacionados con los números matemáticos, 
pero están sujetos a las limitaciones de la representación numérica en las computadoras.

Enteros en Python 
Los tipos enteros o int en Python permiten almacenar un valor numérico no decimal, 
ya sea positivo o negativo incluyendo el 0 de cualquier valor.
Dependiendo de la longitud de palabra o de la arquitectura del ordenador, existen unos números mínimos y máximos que era posible representar. 
Si por ejemplo se usan enteros de 32 bits el rango a representar es de -2^31 a 2^31–1, es decir, -2.147.483.648 a 2.147.483.647. 
Con 64 bits, el rango es de -9.223.372.036.854.775.808 hasta 9.223.372.036.854.775.807. 
Una gran ventaja de Python es que ya no nos tenemos que preocupar de esto, ya que por debajo se encarga de asignar más o menos memoria al número, 
y podemos representar prácticamente cualquier número.
"""
""""
Boleanos en Python
en Python existe el tipo bool o booleano. Es un tipo de dato que permite almacenar dos valores True o False.
Un valor booleano también puede ser el resultado de evaluar una expresión. Ciertos operadores como el mayor que, 
menor que o igual que devuelven un valor bool.
También es posible convertir un determinado valor a bool usando la función bool().
"""
#Formula de la suma de los primeros n numeros pares 
numero = input("Ingrese un numero: ")
numero = int() 
suma = numero*numero+1
resultado = bool(suma)

#Imprimir los resultados de las tareas anteriores
print("punto numero 3")
print(resultado)
print("Punto numero 1")
print(resultado_0)




