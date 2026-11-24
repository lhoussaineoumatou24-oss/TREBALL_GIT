def mostrar_menu():
    """Mostra les opcions del menú."""
    print ("Funcions 2")
    print ("=====================================================")
    print ("1. Comptar majúscules i minúscules")
    print ("2. Any de traspàs")
    print ("3. Dies del mes")
    print ("4. Número perfecte")
    print ("5. Números perfectes fins a 10000  (repte)")
    print ("0. Sortir")
    
#Exercici 1. Entrada segura d'enters
def introduir_int_segur(missatge, minim=None, maxim=None):
    """Demana un enter i el retorna quan és vàlid."""
    correcte = False

    while correcte == False:
        valor_text = input(missatge)
        if not valor_text.isdigit():
            print ("Has d'introduir un número enter")
        else:
            valor_text = int(valor_text)
            if minim is not None and valor_text < minim:
                print (f"El número ha de ser més gran o igual que {minim}.")
            elif maxim is not None and valor_text > maxim:
                print (f"El número ha de ser més petit o igual que {maxim}.")
            else:
                correcte = True
    return valor_text               
#Exercici 2. Comptador de majúscules i minúscules                
def comptar_majuscules_minuscules(cadena):
    """Compta les lletres majúscules i minúscules d'una cadena."""
    majuscules = 0
    minuscules = 0
    
    for lletra in cadena:
        if lletra.isupper():
            majuscules +=1
        elif lletra.islower():
            minuscules +=1
        
    return (majuscules,minuscules)
# Exercici 3. Any de traspàs
def es_any_traspas(a):
    """Determina si un any és de traspàs."""
    if a % 400 == 0:
        return True
    elif a % 100 == 0:
        return False
    elif a % 4 == 0:
        return True
    else:
        return False

def comptar_dies_mes(mes, a):
    """Retorna el nombre de dies d'un mes en un any determinat."""  
    dies_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    dies = dies_mes[mes - 1]
    if mes == 2 and es_any_traspas(a):
        dies = 29
    return dies

def es_num_perfecte(numero):
    """Comprova si un número és perfecte."""
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor
        
    return suma == numero
        
  
def main():
    """Executa el menú i gestiona les opcions."""
    opcio = -1

    while opcio != 0:
        mostrar_menu()
        opcio = introduir_int_segur("Escull una opció: ", 0, 5)

        if opcio == 1:
            cadena = input("Introdueix una cadena: ")
            majuscules, minuscules = comptar_majuscules_minuscules(cadena)
            print("Majúscules:", majuscules)
            print("Minúscules:", minuscules) 
                   
        elif opcio == 2:
            any = introduir_int_segur("Introdueix un any: ", 1)
            resultat = es_any_traspas(any)
            if resultat:
                print("L'any és de traspàs.")
            else:
                print("L'any no és de traspàs.")
                
        elif opcio == 3:
            mes = introduir_int_segur("Introdueix un mes (1-12): ", 1, 12)
            any_entrada = introduir_int_segur("Introdueix un any: ", 1)

            dies = comptar_dies_mes(mes, any_entrada)
            print("Aquest mes té", dies, "dies.")
            
        elif opcio == 4:
            numero = introduir_int_segur("Introdueix un número: ", 1)
            resultat = es_num_perfecte(numero)

            if resultat:
                print("El número és perfecte.")
            else:
                print("El número no és perfecte.")
            
        elif opcio == 5:
            print("Números perfectes fins a 10000:")

            for numero in range(1, 10001):
                if es_num_perfecte(numero):
                    print(numero)   

if __name__ == "__main__":
    main()