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
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el elemento en la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matrices(A, B, filas, columnas):
    C = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)
    return C

def multiplicar_matrices(A, B, filas_A, columnas_A, filas_B, columnas_B):
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

