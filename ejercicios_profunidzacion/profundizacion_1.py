# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia
- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
n1 = float(input('Ingrese Numero 1: '))
n2 = float(input('Ingrese Numero 2: '))
sum = n1 + n2
res = n1 - n2
mul = n1 * n2
div = n1 / n2
exp = n1 ** n2
print(f'La suma entre {n1} y {n2} es {sum}')
print(f'La resta entre {n1} y {n2} es {res}')
print(f'La multiplicacion entre {n1} y {n2} es {mul}')
print(f'La division entre {n1} y {n2} es {div}')
print(f'La exponencial entre {n1} y {n2} es {exp}')
