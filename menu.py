from operaciones import sumar, restar, multiplicar,dividir

def pedir_valor():
    try:
        return float(input("Introduce un valor: "))

def mostrar_menu():
    while True:
        print("Elija una opción:")
        print("1- Sumar")
        print("2- Restar")
        print("3- Multiplicar")
        print("4- Dividir")
        print("5- Salir")
        
        opcion = input("Introduce un número: ")

        if opcion == '1':
            try:
                a = pedir_valor()
                b = pedir_valor()
                resultado = sumar(a, b)
                print(f"Resultado de la suma: {resultado}")
            except ValueError as e:
                print(e)

        elif opcion == '2':
            try:
                a = pedir_valor()
                b = pedir_valor()
                resultado = restar(a, b)
                print(f"Resultado de la resta: {resultado}")
            except ValueError as e:
                print(e)

        elif opcion == '3':
            try:
                a = pedir_valor()
                b = pedir_valor()
                resultado = multiplicar(a, b)
                print(f"Resultado de la multiplicación: {resultado}")
            except ValueError as e:
                print(e)

        elif opcion == '4':
            try:
                a = pedir_valor()
                b = pedir_valor()
                resultado = dividir(a, b)
                print(f"Resultado de la división: {resultado}")
            except ValueError as e:
                print(e)
            except ZeroDivisionError as e:
                print(e)

        elif opcion == '5':
            print("Saliendo del menú.")
            break

        else:
            print("Opción no válida, por favor elija de nuevo.")


