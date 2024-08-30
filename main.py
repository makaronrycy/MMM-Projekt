import controlsystem as cs
from config import Config as cfg
from config import InputSignal
import os
clear = lambda: os.system('cls')

def main():
    program_config = cfg()
    print("Witaj w projekcie na MMM Maurycego Szmuca i Mateusza Dublinowskiego\n"
          "Projekt polega na analizie modelu układu ze sterownikiem\n"
          "Użytkownik może zmieniać parmetry układu, sterownika, oraz wybierać funkcje wejściową i jej parametry\n")
    while True:
        print("Wybierz opcje z menu:")
        print("1. Ustaw parametry układu")
        print("2. Ustaw parametry sterownika")
        print("3. Wybierz funkcje wejściową")
        print("4. Ustaw parametry funkcji wejściowej i programu")
        print("5. Uruchom symulacje")
        choice = int(input("Podaj wartość liczbową referującą do listy z menu:"))
        if(choice == 1):
            clear()
            print("Wybierz parametr który chciałbyś zmienić:")
            print("1. a1:" + str(program_config.a1))
            print("2. a0:" + str(program_config.a0))
            print("3. b2:" + str(program_config.b2))
            print("4. b1:" + str(program_config.b1))
            print("5. b0:" + str(program_config.b0))
            choice = int(input())
            if (choice == 1):
                program_config.a1 = int(input("Nowa wartość dla a1 (aktualna =" + str(program_config.a1) + "): "))
            elif (choice == 2):
                program_config.a0 = int(input("Nowa wartość dla a0 (aktualna =" + str(program_config.a0) + "): "))
            elif (choice == 3):
                program_config.b2 = int(input("Nowa wartość dla b2 (aktualna =" + str(program_config.b2) + "): "))
            elif (choice == 4):
                program_config.b1 = int(input("Nowa wartość dla b1 (aktualna =" + str(program_config.b1) + "): "))
            elif (choice == 5):
                program_config.b0 = int(input("Nowa wartość dla b0 (aktualna =" + str(program_config.b0) + "): "))
            else: print("Niepoprawna składnia wyboru!")
            clear()
        elif(choice == 2):
            clear()
            print("Wybierz parametr który chciałbyś zmienić:")
            print("1. c2:" + str(program_config.c2))
            print("2. c1:" + str(program_config.c1))
            print("3. c0:" + str(program_config.c0))
            print("4. d2:" + str(program_config.d2))
            print("5. d1:" + str(program_config.d1))
            print("6. d0:" + str(program_config.d0))
            choice = int(input())
            if (choice == 1):
                program_config.c2 = int(input("Nowa wartość dla a1 (aktualna =" + str(program_config.c2) + "): "))
            elif (choice == 2):
                program_config.c1 = int(input("Nowa wartość dla a0 (aktualna =" + str(program_config.c1) + "): "))
            elif (choice == 3):
                program_config.c0 = int(input("Nowa wartość dla b2 (aktualna =" + str(program_config.c0) + "): "))
            elif (choice == 4):
                program_config.d2 = int(input("Nowa wartość dla b1 (aktualna =" + str(program_config.d2) + "): "))
            elif (choice == 5):
                program_config.d1 = int(input("Nowa wartość dla b0 (aktualna =" + str(program_config.d1) + "): "))
            elif (choice == 6):
                program_config.d0 = int(input("Nowa wartość dla b0 (aktualna =" + str(program_config.d0) + "): "))
            else:
                print("Niepoprawna składnia wyboru!")
            clear()
        elif (choice == 3):
            clear()
            print("Wybierz funkcje wejściową jaką chciałbyś wybrać (aktualna =" + str(program_config.input) +")")
            print("1. impuls jednostkowy")
            print("2. sinus")
            choice = int(input())
            if (choice == 1):
                program_config.input = InputSignal.SQUARE
            elif (choice == 2):
                program_config.input = InputSignal.SINUS
            else:
                print("Niepoprawna składnia wyboru!")
            clear()
        elif (choice == 4):
            clear()
            print("Wybierz parametr który chciałbyś zmienić:")
            print("1. Krok obliczeń:" + str(program_config.h))
            print("2. Liczba okresów sygnału sinus w przedziale T:" + str(program_config.L))
            print("3. Czas symulacji:" + str(program_config.T))
            print("4. Amplituda:" + str(program_config.M))
            choice = int(input())
            if (choice == 1):
                program_config.h = float(input("Nowy krok obliczeń (aktualna =" + str(program_config.h )+ "): "))
            elif (choice == 2):
                program_config.L = float(input("Nowa liczba okresów (aktualna =" + str(program_config.L )+ "): "))
            elif (choice == 3):
                program_config.T = float(input("Nowy czas symulacji (aktualna =" + str(program_config.T )+ "): "))
            elif (choice == 4):
                program_config.M = int(input("Nowa amplituda (aktualna =" + str(program_config.M )+ "): "))
            else:
                print("Niepoprawna składnia wyboru!")
            clear()
        elif(choice == 5):
            print("Uruchamianie...")
            p = cs.controlSystem(program_config)
            if p.checkStability():
                p.eulerMethod()
                print("Wykres narysowany!")
            else:
                print("Układ niestabilny!")
            input("Naciśnij ENTER aby kontynuować...")
        clear()



if __name__ == "__main__":
    main()
