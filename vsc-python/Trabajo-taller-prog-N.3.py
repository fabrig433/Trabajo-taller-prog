#punto1
def maximo_de_tres(a, b, c):
    return max(a, b, c)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado = maximo_de_tres(num1, num2, num3)
print("El número mayor es:", resultado)

#2
def maximo_de_tres(a, b, c):
    return max(a, b, c)

def maximo_de_diez(lista_numeros):
    max_actual = maximo_de_tres(lista_numeros[0], lista_numeros[1], lista_numeros[2])
    for i in range(3, len(lista_numeros)):
        max_actual = maximo_de_tres(max_actual, lista_numeros[i], lista_numeros[i])
    return max_actual

numeros = []
for i in range(10):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

resultado = maximo_de_diez(numeros)
print("El número mayor es:", resultado)

#3


def cargar_vector(n):
    vector = []
    for i in range(n):
        num = int(input(f"Ingrese el número {i+1} del vector de tamaño {n}: "))
        vector.append(num)
    return vector

def sumar_vector(vector):
    return sum(vector)

def sumar_vectores(a, b):
    return [a[i] + b[i] for i in range(len(a))]


N = int(input("Ingrese la cantidad de elementos para el vector A: "))
M = int(input("Ingrese la cantidad de elementos para el vector B: "))

print("\nCargando vector A:")
vector_A = cargar_vector(N)
print("\nCargando vector B:")
vector_B = cargar_vector(M)

suma_A = sumar_vector(vector_A)
suma_B = sumar_vector(vector_B)

print(f"\nSuma de los elementos del vector A: {suma_A}")
print(f"Suma de los elementos del vector B: {suma_B}")

if N == M:
    vector_resultante = sumar_vectores(vector_A, vector_B)
    print(f"\nSuma de vectores (elemento a elemento): {vector_resultante}")
else:
    print("\nLos vectores tienen diferentes tamaños. No se puede hacer la suma vectorial.")

#4

def contar_vocales(palabra):
    vocales = "aeiou"
    return sum(1 for letra in palabra if letra in vocales)

def contar_consonantes(palabra):
    vocales = "aeiou"
    return sum(1 for letra in palabra if letra.isalpha() and letra not in vocales)

texto = input("Ingrese una o más oraciones: ")
palabras = texto.split()

total_vocales = 0
total_consonantes = 0

for palabra in palabras:
    total_vocales += contar_vocales(palabra)
    total_consonantes += contar_consonantes(palabra)

print(f"\nCantidad total de vocales: {total_vocales}")
print(f"Cantidad total de consonantes: {total_consonantes}")

#5

def calcular_potencia(x, k):
    return x ** k

def contar_digitos(x):
    return len(str(abs(x)))

def es_capicua(x):
    x_str = str(abs(x))
    return x_str == x_str[::-1]

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Calcular la potencia K de un número X")
    print("2. Obtener la cantidad de dígitos de un número X")
    print("3. Determinar si un número es capicúa")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        x = int(input("Ingrese el número X: "))
        k = int(input("Ingrese la potencia K: "))
        resultado = calcular_potencia(x, k)
        print(f"{x} elevado a la {k} es: {resultado}")

    elif opcion == "2":
        x = int(input("Ingrese el número X: "))
        cantidad = contar_digitos(x)
        print(f"La cantidad de dígitos de {x} es: {cantidad}")

    elif opcion == "3":
        x = int(input("Ingrese el número X: "))
        if es_capicua(x):
            print(f"El número {x} es capicúa.")
        else:
            print(f"El número {x} NO es capicúa.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

#6

def cargar_matriz(filas, columnas):
    """Carga una matriz de tamaño filas x columnas"""
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el elemento en la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matrices(A, B, filas, columnas):
    """Realiza la suma de dos matrices A y B"""
    C = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)
    return C

def multiplicar_matrices(A, B, filas_A, columnas_A, filas_B, columnas_B):
    """Realiza el producto de dos matrices A y B"""
    if columnas_A != filas_B:
        print("Las matrices no se pueden multiplicar. Las dimensiones no coinciden.")
        return None
    
    C = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]
    
    for i in range(filas_A):
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma += A[i][k] * B[k][j]
            C[i][j] = suma
    
    return C

def mostrar_matriz(matriz):
    """Muestra la matriz en pantalla"""
    for fila in matriz:
        print(fila)

def main():
    filas_A = int(input("Ingrese el número de filas para la matriz A: "))
    columnas_A = int(input("Ingrese el número de columnas para la matriz A: "))
    filas_B = int(input("Ingrese el número de filas para la matriz B: "))
    columnas_B = int(input("Ingrese el número de columnas para la matriz B: "))

    if filas_A != filas_B or columnas_A != columnas_B:
        print("Las matrices no pueden sumarse porque las dimensiones no coinciden.")
    
    print("\nCargando la matriz A:")
    A = cargar_matriz(filas_A, columnas_A)
    
    print("\nCargando la matriz B:")
    B = cargar_matriz(filas_B, columnas_B)

    print("\n¿Qué operación desea realizar?")
    print("1. Sumar matrices")
    print("2. Multiplicar matrices")
    operacion = int(input("Ingrese la opción (1 o 2): "))
    
    if operacion == 1:
        if filas_A == filas_B and columnas_A == columnas_B:
            C = sumar_matrices(A, B, filas_A, columnas_A)
            print("\nResultado de la suma de las matrices:")
            mostrar_matriz(C)
        else:
            print("Las matrices no pueden sumarse porque las dimensiones no coinciden.")
    
    elif operacion == 2:
        if columnas_A == filas_B:
            C = multiplicar_matrices(A, B, filas_A, columnas_A, filas_B, columnas_B)
            if C is not None:
                print("\nResultado del producto de las matrices:")
                mostrar_matriz(C)
        else:
            print("Las matrices no pueden multiplicarse debido a dimensiones incompatibles.")
    
    else:
        print("Opción inválida.")


if __name__ == "__main__":
    main()

#7

import math

def cargar_matriz(M):
    matriz = []
    for i in range(M):
        fila = []
        for j in range(M):
            valor = int(input(f"Ingrese el elemento en la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def suma_diagonal_principal(matriz, M):
    suma = 0
    for i in range(M):
        suma += matriz[i][i]
    return suma

def calcular_factorial(numero):
    return math.factorial(numero)

def almacenar_mayores_que_factorial(matriz, suma_diagonal, M):
    resultados = []
    for i in range(M):
        for j in range(M):
            num = matriz[i][j]
            if calcular_factorial(num) >= suma_diagonal:
                resultados.append(num)
    return resultados

def eliminar_duplicados(vector):
    return list(set(vector))

def ordenar_vector(vector):
    return sorted(vector)

def main():
    M = int(input("Ingrese el tamaño de la matriz (MxM): "))
    
    matriz = cargar_matriz(M)

    suma_diag = suma_diagonal_principal(matriz, M)
    print(f"La suma de la diagonal principal es: {suma_diag}")
    
    resultados = almacenar_mayores_que_factorial(matriz, suma_diag, M)
    print(f"Números cuyo factorial es mayor o igual a la suma de la diagonal: {resultados}")
    
    resultados_sin_duplicados = eliminar_duplicados(resultados)
    print(f"Después de eliminar duplicados: {resultados_sin_duplicados}")
    
    resultados_ordenados = ordenar_vector(resultados_sin_duplicados)
    print(f"Vector ordenado de menor a mayor: {resultados_ordenados}")

if __name__ == "__main__":
    main()

#8

def cargar_matriz():
    productos = []
    n = int(input("Ingrese el número de electrodomésticos a cargar: "))
    
    for i in range(n):
        print(f"\nCargando electrodoméstico {i+1}:")
        nombre = input("Ingrese el nombre del electrodoméstico: ")
        proveedor = input("Ingrese el proveedor: ")

        while True:
            try:
                precio = float(input("Ingrese el precio: "))
                if precio < 0:
                    print("El precio no puede ser negativo. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Precio inválido. Ingrese un número válido.")

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad en stock: "))
                if cantidad < 0:
                    print("La cantidad en stock no puede ser negativa. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Cantidad inválida. Ingrese un número entero válido.")
        
        productos.append([nombre, proveedor, str(precio), str(cantidad)])

    return productos

def mostrar_productos_por_proveedor(productos, proveedor):
    encontrados = [prod for prod in productos if prod[1].lower() == proveedor.lower()]
    
    if encontrados:
        print(f"\nElectrodomésticos del proveedor '{proveedor}':")
        for prod in encontrados:
            print(f"Nombre: {prod[0]}, Precio: {prod[2]}, Stock: {prod[3]}")
    else:
        print(f"No se encontraron productos del proveedor '{proveedor}'.")

def mostrar_producto_con_menor_precio(productos):
    if not productos:
        print("No hay productos en la lista.")
        return
    
    menor_precio_prod = min(productos, key=lambda prod: float(prod[2]))
    print(f"\nProducto con el menor precio:")
    print(f"Nombre: {menor_precio_prod[0]}, Proveedor: {menor_precio_prod[1]}, Precio: {menor_precio_prod[2]}, Stock: {menor_precio_prod[3]}")

def mostrar_productos_con_stock_positivo(productos):
    productos_en_stock = [prod for prod in productos if int(prod[3]) > 0]
    
    if productos_en_stock:
        print("\nElectrodomésticos con stock positivo:")
        for prod in productos_en_stock:
            print(f"Nombre: {prod[0]}, Proveedor: {prod[1]}, Precio: {prod[2]}, Stock: {prod[3]}")
    else:
        print("No hay productos con stock positivo.")

def mostrar_menu():
    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Cargar la matriz de electrodomésticos")
    print("2. Mostrar electrodomésticos de un proveedor")
    print("3. Mostrar el electrodoméstico con el menor precio")
    print("4. Mostrar los electrodomésticos con stock positivo")
    print("5. Salir")

productos = []
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        productos = cargar_matriz()
    elif opcion == "2":
        proveedor = input("Ingrese el nombre del proveedor: ")
        mostrar_productos_por_proveedor(productos, proveedor)
    elif opcion == "3":
        mostrar_producto_con_menor_precio(productos)
    elif opcion == "4":
        mostrar_productos_con_stock_positivo(productos)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

#9

class Paciente:
    def __init__(self, nombre, urgencia=False):
        self.nombre = nombre
        self.urgencia = urgencia

    def __str__(self):
        return f"{self.nombre} - {'Urgente' if self.urgencia else 'Normal'}"

def ingresar_paciente(lista_pacientes):
    nombre = input("Ingrese el nombre del paciente: ")
    urgencia = input("¿Es una urgencia? (s/n): ").strip().lower() == 's'
    paciente = Paciente(nombre, urgencia)
    lista_pacientes.append(paciente)
    print(f"Paciente {nombre} agregado a la lista.")

def atender_paciente(lista_pacientes):
    if lista_pacientes:
        paciente = lista_pacientes.pop(0)
        print(f"Atendiendo a {paciente.nombre}.")
    else:
        print("No hay pacientes en la lista de espera.")

def atender_urgencia(lista_pacientes):
    for i, paciente in enumerate(lista_pacientes):
        if paciente.urgencia:
            print(f"Atendiendo con urgencia a {paciente.nombre}.")
            del lista_pacientes[i]
            return
    print("No hay pacientes con urgencia en la lista.")

def contar_pacientes_para_atender(lista_pacientes, nombre_paciente):
    for i, paciente in enumerate(lista_pacientes):
        if paciente.nombre == nombre_paciente:
            print(f"Faltan {i} pacientes para atender a {nombre_paciente}.")
            return
    print(f"Paciente {nombre_paciente} no encontrado en la lista.")

def mostrar_lista(lista_pacientes):
    if lista_pacientes:
        print("\nLista de espera:")
        for paciente in lista_pacientes:
            print(paciente)
    else:
        print("La lista de espera está vacía.")

def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Ingresar nuevo paciente")
    print("2. Atender al siguiente paciente")
    print("3. Atender a un paciente con urgencia")
    print("4. Contar pacientes que faltan para atender a un paciente específico")
    print("5. Mostrar la lista de espera")
    print("6. Salir")

lista_pacientes = []

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        ingresar_paciente(lista_pacientes)
    elif opcion == "2":
        atender_paciente(lista_pacientes)
    elif opcion == "3":
        atender_urgencia(lista_pacientes)
    elif opcion == "4":
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        contar_pacientes_para_atender(lista_pacientes, nombre_paciente)
    elif opcion == "5":
        mostrar_lista(lista_pacientes)
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

#10

import random

def rotar_rodillo(rodillo, posiciones):
    return rodillo[-posiciones:] + rodillo[:-posiciones]

def mostrar_resultado(rodillos):
    print("Rodillos:")
    for i in range(3):
        print(f"Rodillo {i+1}: {rodillos[i]}")
    if rodillos[0][0] == rodillos[1][0] == rodillos[2][0]:
        if rodillos[0][0] == "X":
            print("¡Ganó 10 fichas!")
        elif rodillos[0][0] == "O":
            print("¡Ganó 100 fichas!")
        elif rodillos[0][0] == "7":
            print("¡Ganó 1000 fichas!")
    else:
        print("No ganó nada.")

def jugar():
    rodillo1 = ["O", "X", "7", "O", "X", "7", "O", "X", "7"]
    rodillo2 = ["7", "X", "O", "7", "X", "O", "7", "X", "O"]
    rodillo3 = ["X", "O", "7", "X", "O", "7", "X", "O", "7"]

    rodillos = [rodillo1, rodillo2, rodillo3]

    for i in range(3):
        rotaciones = random.randint(0, 9)  
        print(f"Rodillo {i+1} se rota {rotaciones} posiciones.")
        rodillos[i] = rotar_rodillo(rodillos[i], rotaciones)

    mostrar_resultado(rodillos)

def main():
    while True:
        print("\n=== Bienvenido a la máquina tragamonedas ===")
        jugar()
        continuar = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if continuar != "s":
            print("¡Gracias por jugar! ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()