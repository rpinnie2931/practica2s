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
