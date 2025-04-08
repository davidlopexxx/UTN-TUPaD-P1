#Ejercicio 1
#edad=int (input ("Escriba su edad: "))
#if edad >= 18 : 
#    print ("Es mayor de edad") 


#Ejercicio 2
#calificacion= int(input("Escriva su calificacion: "))
#if calificacion>= 6 :
#    print("Aprovado")
#else:
#    print("Desaprobado")


#Ejercicio 3
#num= int (input("Ingrese un nemero: "))
#if num % 2 == 0:
#    print("Numero par")
#else :
#    print("Ingrese un numero par")


#Ejercicio 4
#edad= int (input("Escriba su edad: "))
#if edad < 12:
#    print("Es un niño/a")
#elif edad >= 12 and edad < 18:
#    print("Es un adolecente")
#elif edad >= 18 and edad < 30:
#    print("Es un adulto/a joven")
#else :
#    print ("Es un adolto/a mayor")


#Ejercicio 5
#contra= input("Ingrese una contraseña entre 8 y 14 caracteres: ")
#if len(contra) >=8 and len(contra) <=14:
#    print ("contraseña correcta")
#else:
#    print("ingrese una contraceña correcta")


#Ejercicio 6
#import random 
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
#from statistics import mode, median, mean
#promedio 
#media= mean(numeros_aleatorios)
#valor repetido(comentario)
#moda=mode(numeros_aleatorios)
#valor del centro(comentario)
#mediana=median(numeros_aleatorios)
#if media > mediana and mediana > moda:
#    print("Sesgo positivo")
#elif media < mediana and mediana < moda:
#    print("Sesgo negativo")
#else:
#    media == mediana == moda
#    print(" Sin sesgo")


#Ejercicio 7
#frase= input("ingrese un frase: ")
#if frase [-1] in "a,e,i,o,u": 
#    print (f"frase {frase} !" )
#else: 
#    print (frase)


#Ejercicio 8
# frase= input("Escriba su nombre: ")
# opcion=int(input("Ingrese la opcion 1( nombre mayuscula), 2(nombre minuscula), 3(primera letra matuscula): "))
# if opcion == 1:
#     print (frase.upper())
# elif opcion == 2:
#     print(frase.lower())
# else:
#     opcion == 3
#     print (frase.title())


#Ejercicio 9
# magnitud= int(input("Ingrese la magnitud del terremoto: "))
# if magnitud < 3:
#     print ("Muy leve")
# elif  4 > magnitud >= 3:
#     print("Leve")
# elif 5 > magnitud >=4:
#     print("Moderado") 
# elif  6 > magnitud >= 5:
#     print("Fuerte")
# elif 7 > magnitud >=6:
#     print("Muy Fuerte")
# else:
#     magnitud >= 7
#     print("Extremo")


#Ejercicio 10
# hemisferio=input("Ingrese el hemisferio donde se encuenta N/S: ")
# mes=input("Ingrese el mes del año que es: ")
# dia=int(input("Ingrese el dia: "))
# mesInvN=("ENERO,FEBRERO")
# mesVerS=("ENERO,FEBRERO")
# mesInvS=("JULIO,AGOSTO")
# mesVerN=("JULIO,AGOSTO")
# mesPriN=("ABRIL,MAYO")
# mesOtoS=("ABRIL,MAYO")
# mesPriS=("OCTUBRE,NOVIEMBRE")
# mesOtoN=("OCTUBRE,NOVIEMBRE")
 
# if hemisferio.upper() == "N" and  ((mes.upper() == "DICIEMBRE" and 21 < dia <= 31) or (mes.upper() in mesInvN) or (mes.upper()== "MARZO" and 1 < dia <= 20)):
#     print("Invierno")
# elif  hemisferio.upper() == "S" and  ((mes.upper() == "DICIEMBRE" and 21 < dia <= 31) or (mes.upper() in mesVerS) or (mes.upper()== "MARZO" and 1 < dia <= 20)):  
#     print("Verano")
# elif  hemisferio.upper() == "S" and  ((mes.upper() == "JUNIO" and 21 < dia <= 30) or (mes.upper() in mesInvS) or (mes.upper()== "SEPTIEMBRE" and 1 < dia <= 20)):
#     print("Invierno")
# elif  hemisferio.upper() == "N" and  ((mes.upper() == "JUNIO" and 21 < dia <= 30) or (mes.upper() in mesVerN) or (mes.upper()== "SEPTIEMBRE" and 1 < dia <= 20)):
#     print("Verano")
# elif  hemisferio.upper() == "N" and  ((mes.upper() == "MARZO" and 21 < dia <= 31) or (mes.upper() in mesPriN) or (mes.upper()== "JUNIO" and 1 < dia <= 20)):
#     print("Primavera")
# elif  hemisferio.upper() == "S" and  ((mes.upper() == "MARZO" and 21 < dia <= 31) or (mes.upper() in mesOtoS) or (mes.upper()== "JUNIO" and 1 < dia <= 20)):
#     print("Otoño")
# elif  hemisferio.upper() == "S" and  ((mes.upper() == "SEPTIEMBRE" and 21 < dia <= 30) or (mes.upper() in mesPriS) or (mes.upper()== "DICIEMBRE" and 1 < dia <= 20)):
#     print("Primavera")
# elif  hemisferio.upper() == "N" and  ((mes.upper() == "SEPTIEMBRE" and 21 < dia <= 30) or (mes.upper() in mesOtoN) or (mes.upper()== "DICIEMBRE" and 1 < dia <= 20)):
#     print("Otoño")