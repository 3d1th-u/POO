try:
    numero = int(input("Escribe un número entre el 1 y el 9: "))
    if numero < 1 or numero > 9:
        print("Error: El número debe estar entre 1 y 9")
    else:
        resultado = 100 / numero
        print("El resultado es:", resultado)
except ValueError:
    print("Error: Debes escribir un número entero válido")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
finally:
    print("Fin de la ejecución del programa.")
