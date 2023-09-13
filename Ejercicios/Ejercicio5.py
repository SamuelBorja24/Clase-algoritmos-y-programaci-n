print("---------------------------------Inicio del programa----------------------------------")

Edad1 = int (input("¿Cual es su edad?:  "))

if Edad1 < 18:
    print("Eres menor de edad")
else: 
    print("Eres mayor de edad")

print("---------------------------------Modulo de Seguridad----------------------------------")

    #Aca si el usuario es mayor de edad, le vamos a solicitar una contraseña en comentarios 

print("Su contraseña fue enviada exitosamente al correo")

Clavemayoredad = "Contraseña"

password = input("Ingrese la contraseña enviada al correo:   ")

if Clavemayoredad == password.lower():
    print("Contraseña correcta")
else:
    print ("Contraseña incorrecta")

print ("-------------------------------Modulo 3 de la interacción---------------------------")

print("Escriba una frase o palabra para seguir adelante en la autenticación")

frase = input("Introduce una frase: ")

#Si desea reemplazar la contraseña, solicite al usuario escribir en diferentes letras o números la nueva contraseña o simplemnete solicite un parametro de validación

vocal = input("Introduzaca una vocal en minuscula:   ")
print(frase.replace(vocal, vocal.upper()))

print ("Usted a completado los tres modulos de autenticación / puede seguir adelante con el pago")

ChatGPT
Aquí tienes una versión mejorada del código con algunos cambios para hacerlo más eficiente y limpio:

python
Copy code
print("---------------------------------Inicio del programa----------------------------------")

edad = int(input("¿Cuál es su edad?: "))

if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

print("---------------------------------Modulo de Seguridad----------------------------------")

# Si el usuario es mayor de edad, solicitar una contraseña
if edad >= 18:
    print("Su contraseña fue enviada exitosamente al correo")
    clave_mayor_edad = "Contraseña"
    password = input("Ingrese la contraseña enviada al correo: ")

    if clave_mayor_edad == password.lower():
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

print("-------------------------------Modulo 3 de la interacción---------------------------")

print("Escriba una frase o palabra para seguir adelante en la autenticación")

frase = input("Introduce una frase: ")
vocal = input("Introduzca una vocal en minúscula: ")

# Reemplace todas las instancias de la vocal en minúscula con la vocal en mayúscula
frase_modificada = frase.replace(vocal, vocal.upper())
print(frase_modificada)

print("Ha completado los tres módulos de autenticación / puede seguir adelante con el pago")







