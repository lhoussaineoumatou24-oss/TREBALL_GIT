def mostrar_menu():
    print ("Funcions 1")
    print("====================")
    print ("1. Multiplica")
    print ("2.Anys 2000")
    print ("3.Gira del revés")
    print ("4.Triangle de Pascal")
    print ("5.Sortir")
    
def multiplica(a, b):
    # Funció que multiplica dos números
    print (f" El resultat es {a*b}")

from datetime import date

def anys_2000():
    any_actual = date.today().year
    
    correcte = False

    while correcte == False:
        try:
            any_usuari = int(input("Introdueix un any: "))

            if any_usuari >= 2000 and any_usuari <= any_actual:
                        correcte = True
            else:
                print("Any incorrecte. Torna-ho a provar.")

        except ValueError:
            print("Introdueix un any vàlid.")

    anys_passats = any_usuari - 2000

    print(f"Des del 2000 han passat {anys_passats} anys")

def gira_reves():
        
    texto = input("Introdueix una paraula o frase: ")

    text_invertit = ""

    for lletra in texto:
        text_invertit = lletra + text_invertit
            
    print("Text del revés:", text_invertit)

    
def main():
    mostrar_menu()
    numero = False
    while numero == False:
        try:
            opcio = int(input("Escoge una opcion: "))
            numero = True
        except ValueError:
            print("Selecciona un numero del menu:")
            
    while opcio !=5:
        if opcio < 1 or opcio > 5:
            print("Opció incorrecta")

        if opcio == 1:
            print ("Has seleccionat Multiplicar ")
    
            correcte = False
            while correcte == False:
                try:
                    multiplicacio = int(input("Escriu el Primer valor: "))
                    correcte = True
                except ValueError:
                    print("Ha de ser un enter")

            correcte2 = False
            while correcte2 == False:
                try:
                    multiplicacio2 = int(input("Escriu el Segon valor: "))
                    correcte2 = True
                except ValueError:
                    print("Ha de ser un enter")
            multiplica(multiplicacio,multiplicacio2)
            
        elif opcio == 2:
            print("Has seleccionat Anys 2000")
            anys_2000()

        elif opcio == 3:
            print ("Has seleccionat Gira del revés ")
            gira_reves()
            
        elif opcio == 4:
            print ("Has seleccionat Triangle de Pascal")
        else:
            print ("Adeu")
        
        mostrar_menu()
        opcio = int(input("Escoge una opcion: "))
            
        
if __name__ == "__main__":
    main()
    
