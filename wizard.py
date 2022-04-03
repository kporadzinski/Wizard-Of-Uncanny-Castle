from random import randrange
import json


def record(num,counter):




    name = input('JAK SIĘ ZWIESZ ŚMIAŁKU?')
    wynik = [counter,name]

    with open('magazyn.json') as json_file:


      data = json.load(json_file)



    if str(num) in data.keys():


        data[str(num)].append(wynik)
        data[str(num)]=sorted(data[str(num)], key=lambda x: x[0])

        with open('magazyn.json', 'w') as f:
             f.write(json.dumps(data))

        print(f"\nTABLICA WYNIKÓW DLA KATEGORII LICZBY DO {num}\n")
        for i in data[str(num)] :
            print(str(i)+'\n')

    else:
        data[str(num)]=[]
        data[str(num)].append(wynik)

        with open('magazyn.json', 'w') as f:
             f.write(json.dumps(data))
             print(f'TABLICA WYNIKÓW DLA KATEGORII {num} ' )

        for i in data[str(num)] :
            print(str(i)+'\n')




def gra(number, zakres, counter=1):

    my_num = (input(' O JAKIEJ LICZBIE MYŚLI KOMPUTEROWY CZARODIEJ? \n'))

    try:
        my_num = int(my_num)
    except:
        print('MIAŁEŚ PODAĆ LICZBĘ, POSTARAJ SIĘ!')
        gra(number,zakres,counter+1)

    if my_num == number :
        print(f'NOT BAD, HUMAN! \n you did it in {counter} attempsów')


        will = input('CHCESZ SIĘ ZASEJFOWAĆ? T/N')

        if will.upper() == 'T':

           record(zakres,counter)

           another = input('CHCESZ ZAGRAĆ RAZ JESZCZE? (T/N)')
           if another.upper() == 'T':
               starter()
           else:
               print('\nWIĘC TYMCZASEM, ŚMIAŁKU!\n')
               return

        else:

           another = input('CHCESZ ZAGRAĆ RAZ JESZCZE? (T/N)')
           if another.upper() == 'T':
               starter()
           else:
               print('\nWIĘC TYMCZASEM, ŚMIAŁKU!\n')
               return

    else:
        if my_num > number :
            print('\nPRZESADZASZ NĘDZNIKU!, try again \n')
            return gra(number, zakres, counter+1)

        else:
            print('\nZA MAŁO GŁUPCZE,  try again \n')
            return gra(number, zakres, counter+1)

def starter() :

    print('\n----------NOWA GRA----------')

    choice = int(input('\nWYBIERZ SWE PRZEZNACZENIE: \n\n EASY -- (1)\n MEDIUM -(2)\n HARD ---(3)\n superhard ---(4)\n CUSTOM--(5)\n'))

    if choice == 1 :
        print('WYBRAŁEŚ LEVEL 1, LICZBY 0-10')
        return gra(randrange(10),10)
    if choice == 4 :
            print('WYBRAŁEŚ LEVEL 4, LICZBY 1-1000000')
            return gra(randrange(1000000),1000000)
    if choice == 2:
        print('WYBRAŁEŚ POZIOM LEVEL 2, LICZBY 0-100')
        return gra(randrange(100),100)
    if choice == 3:
        print('WYBRAŁEŚ LEVEL HARD LICZBY 0-1000')
        return gra(randrange(1000),1000)
    else :
        print('WYBRAŁEŚ POZIOM CUSTOMOWY')
        liczba = int(input('podaj więc liczbę'))

        return gra(randrange(liczba),liczba)

starter()
