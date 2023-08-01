#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

a = 3
print (a)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print (type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print (type(a))




# 4) Crear una variable que contenga tu nombre

# In[2]:


mi_nombre = "Jonathan"

# 5) Crear una variable que contenga un número complejo

# In[3]:

num = 5j



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(num))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

var1 = True
var2 = False

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print (type(var1))
print (type(var2))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

var3 = 5 + 10.5


# 11) Realizar una operación de suma de números complejos

# In[2]:

5j + 10j


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

5j + 10



# 13) Realizar una operación de multiplicación

# In[5]:

5*3

# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print (2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

print (27/4)

# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

print(27//4)

# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

print(27%4)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

6*4+3



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:


var1 = "Juan"
var2 = "Perez"
print (var1 + " " + var2)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

"2" == 2 # uno es una String el otro es un Int



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

int ("2") == 2



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

a = float('3.8') #Porque el valor tiene una coma no un punto. para poderlo convertir el dato debe ser 3.8 no 3,8
print (type(a))



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

var = 3
var -= 1



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1 << 2 

# **Explicación:**  La operación 1 << 2 en Python realiza un desplazamiento a la izquierda de bits (bitwise left shift) en el número entero 1.
# En este caso, el número binario 1 se desplaza dos posiciones hacia la izquierda, y se rellena con ceros a la derecha. El resultado de esta operación es 4.
# Explicación paso a paso:
# 1. El número 1 en binario es representado como 0001.
# 2. Realizamos un desplazamiento de dos posiciones hacia la izquierda: 0001 << 2.
# 3. El resultado es 0100, que en decimal representa el número 4.*
# Es importante tener en cuenta que el desplazamiento a la izquierda de bits (<<) multiplica el número original
# por 2 elevado a la potencia del número de posiciones desplazadas. 
# En este caso, 1 se multiplica por 2 elevado a la potencia de 2, lo que resulta en 4.



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

2 + int('2')
#no se puede hacer operaciones aritmeticas entre ints y strings




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

var = "hoy es 1 de Agosto"
var2 = 2023
print (var + " de " + str(var2))

