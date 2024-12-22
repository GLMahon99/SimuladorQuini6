import random

# Genera los 6 numeros secretos con la biblioteca random
numeros_secretos = random.sample(range(46), 6)
# Mostrar los números generados 
print("estos son los numeros secretos:",numeros_secretos)

# inicializa variable para ingreso del usuario
numeros_ingresados = []

# recorre 6 veces, cada vez el usuario ingresa un numero se guarda en la lista si cumple con las condiciones, sino pide que se vuelva a ingresar otro numero
for i in range(6): 
    while True: 
        numero = int(input(f"Introduce el número {i + 1} (entre 0 y 48): ")) 
        if 0 <= numero <= 45 and numero not in numeros_ingresados:
            # GUARDA EL NUMERO AL FINAL DE LA LISTA
            numeros_ingresados.append(numero) 
            break
        else: 
            print("Número fuera de rango. Por favor, introduce un número entre 0 y 48, y que sea disitinto a los ya ingresados.")

print("numeros ingresados: ", numeros_ingresados)

lista_de_coincidencia = []


# recorre la lista de numeros secretos
for i in range(len(numeros_secretos)):
    coincidencia = False
    # recorre la lista de numeros ingresados y compara cada numero con el numero secreto segun el ciclo que este recorriendo, si coincide se agrega un 1 a la lista de coindicendia, cambia a true la variable coincidencia y realiza un breacr para romper el recorrido
    for num in range(len(numeros_ingresados)):
        if numeros_ingresados[num] == numeros_secretos[i]:
            lista_de_coincidencia.append(1)
            coincidencia = True
            break
    if not coincidencia:
        lista_de_coincidencia.append(0)
            
print("lista de coincidencia", lista_de_coincidencia)

# condicion si la lista coincidencia es toda de 1, ganaste
if all(elemento == 1 for elemento in lista_de_coincidencia): 
    print("GANASTE") 
else: 
    print("PERDISTE")
