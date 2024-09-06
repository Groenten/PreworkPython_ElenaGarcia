'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

def cuenta(price_restaurante):
  total=0
  for price in price_restaurante:
    total += price
  return total

cuenta_sin_propina=cuenta([23,45,10,3,5])
print('Cuenta sin propina:',cuenta_sin_propina)
propina=cuenta_sin_propina * 0.15
print('Propina:',propina)
cuenta_con_propina= cuenta_sin_propina+propina
print('Cuenta total con propina del 15% :', cuenta_con_propina)
