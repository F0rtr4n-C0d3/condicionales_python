# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición


#inicio de la actividad

if numero_1 > numero_2:
    print('El primer numero={} es mayor que el segundo numero={}'.format(numero_1 , numero_2))

else:
    print('El segundo numero={} es mayor que el primer numero={}'.format(numero_2, numero_1))

print ('Termino la primera condicion')

if numero_1 > 0:
    print('El primer numero es positivo={}'.format(numero_1))
elif numero_1 < 0:
    print('el primer numero es negativo'.format(numero_1))

else:
    print('El primer numero es 0')

print('Terminada segunda condicion')

if (numero_1 < 10) and (numero_2 > -2):
    print('El primer numero={} es menor a 10 y el segundo mayor={} a -2'.format(numero_1 , numero_2))

elif (numero_1 > 10) and (numero_2 < -2):
    print('el primer numero={} es mayor a 10 y el segundo numero={} menor a -2'.format(numero_1 , numero_2))

else:
    print('Ningun numero es mayor ni menor')

print('terminada tercera condicion')

#Actividad 1 terminada


   