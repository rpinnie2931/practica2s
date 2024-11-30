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
