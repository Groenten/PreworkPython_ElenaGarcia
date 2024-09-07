'''Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.'''

edad_usuario=float(input("Edad: "))
if edad_usuario> 18:
  print('Eres mayor de edad porque tienes',edad_usuario, 'años')
elif edad_usuario<18:
  print('Eres menor de edad porque tienes', edad_usuario, 'años')
