#este programa va a tener como finalidad mezclar varios elementos que pueda solicitar el usuario
#vamos a colocar diferentes metodos para poder realizaar actividades simples o secuenciales del mismo modo permitirá realizar salidas de información 
#sujetas a condiciones logicas.
#print("---------------------------------Inicio del programa----------------------------------")
#Edad1 = int (input("¿Cual es su edad?:  "))
#if Edad1 < 18:
    #print("Eres menor de edad")
#else: 
    #print("Eres mayor de edad")
#print("---------------------------------Modulo de Seguridad----------------------------------")
    #Aca si el usuario es mayor de edad, le vamos a solicitar una contraseña en comentarios 
#print("Su contraseña fue enviada exitosamente al correo")
#Clavemayoredad = "Contraseña"
#password = input("Ingrese la contraseña enviada al correo:   ")
#if Clavemayoredad == password.lower():
    #print("Contraseña correcta")
#else:
    #print ("Contraseña incorrecta")
#print ("-------------------------------Modulo 3 de la interacción---------------------------")
#print("Escriba una frase o palabra para seguir adelante en la autenticación")
#frase = input("Introduce una frase: ")
#Si desea reemplazar la contraseña, solicite al usuario escribir en diferentes letras o números la nueva contraseña o simplemnete solicite un parametro de validación
#vocal = input("Introduzaca una vocal en minuscula:   ")
#print(frase.replace(vocal, vocal.upper()))
#print ("Usted a completado los tres modulos de autenticación / puede seguir adelante con el pago")

print("---------------------------------Inicio del programa----------------------------------")

edad = int(input("¿Cuál es su edad?: "))

if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

print("---------------------------------Modulo de Seguridad----------------------------------")

# Si el usuario es mayor de edad, solicitar una contraseña
if edad >= 18:
    print("Su contraseña es su primer nombre y los 6 primeros numeros de su cedula")
    clavemayoredad = "samuel124361"
    password = input("Ingrese su contraseña: ")

    if clavemayoredad == password.lower():
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

print("-------------------------------Modulo 3 de la interacción---------------------------")

print("Escriba la respuesta a la siguiente pregunta de autenticación:")

print("¿Cual es su deporte favorito?")
respuesta = "volleyball"

respuesta2 = input("Escriba la respuesta a la pregunta:  ")

if respuesta == respuesta2.lower():
    print ("contraseña correcta")
else: 
    print("contraseña incorrecta")

frase = input("Introduce la respuesta de la pregunta de seguridad: ")
letra = input("Introduzca una letra en minúscula: ")

# Reemplace todas las instancias de la vocal en minúscula con la vocal en mayúscula
frasemodificada = frase.replace(letra, letra.upper())
print(frasemodificada)

print("Ha completado los tres módulos de autenticación / puede seguir adelante con la autenticación")
