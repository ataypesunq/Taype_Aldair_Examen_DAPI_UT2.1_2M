def area_cuadrado (lado1, lado2):
    """
    Esta función calcula el area de un cuadrado
    Parametros:
        lado: longitud, valor introducido por el usurio
    Salida:
        area del cuadrado
    """
    x = lado1 * lado2
    return x
area = area_cuadrado
y = int(input("Escriba un numero(longitud): "))
print(y * y)
