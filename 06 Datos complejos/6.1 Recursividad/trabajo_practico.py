#1 Factorial recursivo hasta un número ingresado
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Mostrar todos los factoriales desde 1 hasta un número dado
def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")


#2 Serie de Fibonacci recursiva
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Mostrar la serie completa hasta una posición
def mostrar_fibonacci(hasta):
    for i in range(hasta):
        print(f"F({i}) = {fibonacci(i)}")


#3 Potencia recursiva (n^m)
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)
    

#4 Convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ''
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
# Para evitar cadena vacía al convertir 0
def convertir_a_binario(n):
    if n == 0:
        return '0'
    return decimal_a_binario(n)


#5 Verificar si una palabra es un palíndromo (sin usar [::-1])
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    

#6 Sumar los dígitos de un número (sin convertir a string)
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)


#7 Contar bloques en una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    

#8 Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

    

