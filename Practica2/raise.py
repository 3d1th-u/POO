try:
    numero = int(input("Escribe um número entre el 1 y el 9: "))
    if numero < 1 or numero > 9:
        raise ValueError
    resultado = 100 / numero
    print("El resultado es:", resultado)
except ValueError:
    print("Error: Debes escribir un número válido entre 1 y 9")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
