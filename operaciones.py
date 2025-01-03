def es_numero(valor):
    return isinstance(valor, (int, float))

def sumar(a, b):
    if es_numero(a) and es_numero(b):
        return a + b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def restar(a, b):
    if es_numero(a) and es_numero(b):
        return a - b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def multiplicar(a, b):
    if es_numero(a) and es_numero(b):
        resultado = 0
        positivo = abs(b)
        for _ in range(int(positivo)):
            resultado += a
        return resultado if b >= 0 else -resultado
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def dividir(dividendo, divisor):
    if not es_numero(dividendo) or not es_numero(divisor):
        raise ValueError("Ambos parámetros deben ser int o float")
    if divisor == 0:
        raise ZeroDivisionError("El divisor no puede ser cero")
    
    cociente = 0
    acumulador = abs(dividendo)
    resta_del_divisor = abs(divisor)

    while acumulador >= resta_del_divisor:
        acumulador -= resta_del_divisor
        cociente += 1

    return cociente if dividendo * divisor >= 0 else -cociente

def factorial_iterativo(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El valor debe ser un número entero no negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El valor debe ser un número entero no negativo")
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El valor debe ser un número entero no negativo")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
