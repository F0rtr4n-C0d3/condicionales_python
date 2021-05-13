# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda


#Inicio de actividad : 

#Variables de cantidad de letras :

palabra_1=len(texto_1)
palabra_2=len(texto_2)



if texto_1 > texto_2:
    print('La primera palabra {} es mayor a la segunda {}'.format(texto_1 , texto_2))
elif texto_1 < texto_2:
    print('La segunda palabra {} es mayor a la primera {}'.format(texto_2, texto_1))
else:
    print('Las palabras son iguales')

print('primera condicion terminada')

#inicio segunda condicion

if palabra_1 > palabra_2:
    print('{} tiene mas cantidad de letras que {}'.format(texto_1, texto_2))
elif palabra_1 < palabra_2:
    print('{} tiene mas cantidad de letras que {}'.format(texto_2, texto_1))
else:
    print('tienen la misma cantidad de letras')   

#inicio tercera y cuarta condicion

if texto_1 == copia_texto_1:
    print('Es la misma palabra')

if copia_texto_1 != texto_2:
    print('No son la misma palabra')


print('Gracias por el aguante! ahha')
