#Proyecto Final
#Nombre: David Estuardo Mejicano Ortiz
#Carne: 202200605

#Matriz de tipo texto


sala = [["X","X","X","X","X"],
        ["X","X","X","X","X"],
        ["X","X","X","X","X"],
        ["X","X","X","X","X"],
        ["X","X","X","X","X"] ]
            
#Variables de numeros enteros
fila = 0
columna = 0


#variables de tipo booleano
comp1 = True
comp2 = True
comp3 = True

def imprimir_sala():
        
    matriz = len(sala)

    for i in range(matriz):
        for j in range(matriz):
            print("\t",sala[i][j], end=" ")
        print()
        

def pedir_datos():
#En python es necesario indicar que se usaran las variables globales dentro de esta funcion
    global comp1
    global comp2
    global fila 
    global columna
#Como la funcion puede ser usada mas de una vez es necesario devolver los valores iniciales de las variables globales
    comp1 = True
    comp2 = True
#Variables locales de tipo entero
    f1 = 0
    c1 = 0
    
    while comp1 or comp2:
#Se intenta solicitar los valores de la fila y columna
        try:
            f1 = int(input("Ingrese el numero de fila: "))
            c1 = int(input("Ingrese el numero de columna: "))
            
        except:
            print("Ingrese un numero valido")
            
#Se comprueba si los valores ingresados estan dentro del rango establecido, de no ser asi se solicita ingresar nuevamente los datos
        if f1 <= 5 and f1 >= 1:
            fila = f1
            comp1 = False
        else:
            print("Fila incorrecta, por favor ingrese los datos nuevamente.")

        if c1 <= 5 and c1 >= 1:
            columna = c1
            comp2 = False
        else:
            print("Columna incorrecta, por favor ingrese los datos nuevamente.")
            
def ingresar_butaca(f,c):
#Primero comprobamos que la butaca este libre, luego le asignamos el valor de ocupado
    if sala[f-1][c-1] != "O":
        sala[f-1][c-1] = "O"
    else:
        print("Butaca ocupada, por favor ingrese otra.")
        

def comprobacion():
    global comp3
#Comprobamos si se desea cerrar el programa, de ser asi se imprime el estado de la sala y se cierra el programa
    while comp3:
        respuesta = input("¿Desea realizar otra reserva? (S/N):")
        if respuesta == "N":
            print("Las butacas ocupadas son:")
            imprimir_sala()
            comp3 = False
        elif respuesta == "S":
            break
        else:
            print("Ingrese una respuesta valida.")
        

while comp3:
    print("Estado de la sala:")
    imprimir_sala()
    pedir_datos()
    ingresar_butaca(fila,columna)
    comprobacion()