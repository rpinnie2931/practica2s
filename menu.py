from operaciones import sumar, restar, multiplicar,dividir,factorial_iterativo,factorial_recursivo,fibonacci

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
        print("6- Calcular el factorial de un número (iterativo)")
        print("7- Calcular el factorial de un número (recursivo)")
        print("8- Calcular el Fibonacci de un número (iterativo)")
        
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

      elif opcion == '6':
            try:
                n = int(input("Introduce un número entero no negativo: "))
                resultado = factorial_iterativo(n)
                print(f"El factorial de {n} es: {resultado}")
            except ValueError as e:
                print(e)


      elif opcion == '7':
            try:
                n = int(input("Introduce un número entero no negativo: "))
                resultado = factorial_recursivo(n)
                print(f"El factorial de {n} es: {resultado}")
            except ValueError as e:
                print(e)

       elif opcion == '8':
            try:
                n = int(input("Introduce un número entero no negativo: "))
                resultado = fibonacci(n)
                print(f"El Fibonacci de {n} es: {resultado}")
            except ValueError as e:
                print(e)
     



        elif opcion == '5':
            print("Saliendo del menú.")
            break

        else:
            print("Opción no válida, por favor elija de nuevo.")


