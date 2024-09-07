'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''
# Mi primer intento y tras preguntaar a ChatGPT
'''palabra=(input('Escribe una palabra:'))
contador_vocales=("a","e","i","o","u")
def palabra(vocales_palabra):
  for vocales in vocales_palabra:
    if vocales in contador_vocales:
      contador_vocales[palabra]=+1
      print(contador_vocales)
    else:
      print(palabra, 'no es una palabra tolili')'''

      # Función para contar las vocales en una palabra
def contar_vocales(palabra):
    contador_vocales = 0
    for letra in palabra:
        if letra.lower() in "aeiou":
            contador_vocales += 1
    return contador_vocales

# Solicitar la palabra al usuario
palabra = input('Escribe una palabra: ')

# Llamar a la función y mostrar el resultado
numero_de_vocales = contar_vocales(palabra)
print(f"La palabra '{palabra}' contiene {numero_de_vocales} vocales.")

    
