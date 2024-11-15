num_int_positivo = int(input("Escribe un numero entero positivo: "))
if num_int_positivo % 2 == 0:
    print(f" {num_int_positivo} es par")
else:
    print(f" {num_int_positivo} es impar")

num_entero = int(input("Escriba un numero entero: "))
for i in range(0, num_entero + 1, 3):
    print(i, end= num_entero % 3 != 0)
