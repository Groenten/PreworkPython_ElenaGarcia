'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.'''

def suma_numeros_pares(numeros):
  contador=(0)
  for par in range(0,101):
        if numeros % 2 == 0:
           contador += 1
           return contador
print(suma_numeros_pares)