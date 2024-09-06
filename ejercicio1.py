'''Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.'''
temperatura_celsius=float(input("Temperatura en grados Celsius: "))
temperatura_fahrenheit= (temperatura_celsius*9/5) +32
print('Temperatura en grados Fahrenheit:', temperatura_fahrenheit)

'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

def cuenta(price_restaurante):
  total=0
  for price in price_restaurante:
    total += price
  return total
cuenta_sin_propina=price_restaurante([23,45,10,3.5,5])
print(cuenta_sin_propina)
propina=cuenta_sin_propina * 0,15
cuenta_con_propina=cuenta_sin_propina+propina
print(cuenta_con_propina)

