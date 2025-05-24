'''Problema 1. Se citeste de la tastatura o parola. Sa se verifice daca parola introdusa are
    cel putin 10 caractere si nu contine spatiu.
Sa se afiseze un mesaj corespunzator pentru fiecare neregula gasita
    sau mesajul "OK" in cazul in care parola respecta regulile.
    hints: boolean, conditionals'''
'''parola = input('Parola aleasa este: ')
while (len(parola) < 10) or (" " in parola):
    if (len(parola) < 10) and (" " in parola):
        print(f'Parola {parola} nu implineste conditia de a avea cel putin 10 caractere si are spatii goale. Mai incearca!')
        parola = input('Noua parola aleasa este: ')
    else:
        if len(parola) <10:
            print(f'Parola {parola} nu implineste conditia de a avea cel putin 10 caractere. Mai incearca!')
            parola = input('Noua parola aleasa este: ')
        else:
            if " " in parola:
                print(f'Parola {parola} nu implineste conditia de a nu avea spatii goale. Mai incearca!')
                parola = input('Noua parola aleasa este: ')
print ('Felicitari! Parola implineste ambele conditii de lungime si spatii goale.')'''

'''Problema 2. Sa se numere de cate ori apare o litera intr-un cuvant.'''
'''suma = 0
cuvant = input('Cuvantul ales este: ')
litera = input(f'Alege o litera pe care sa o verifici daca apare in {cuvant}: ')
for x in cuvant:
    if x == litera:
        suma +=1
print (f"Litera {litera} apare de {suma} ori in cuvantul {cuvant}.")'''


'''Problema 3. Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.'''
'''for i in range (1,10):
    power = 3 ** i
    if power >= 200 and power <= 300:
        print (f'3 la puterea {i} este {power}')'''

'''Problema 4. Se citeste un numar de la tastatura. 
    Sa se calculeze suma numerelor de la 1 pana la numarul citit. (folositi for si while)'''
#varianta for
'''suma = 0
numar = int(input('Gandeste-te la un numar: '))
for i in range(1,numar +1):
    suma += i
print(f'Suma lui Gauss pentru {numar} este {suma}.')'''
#varianta while
'''sum = 0
j = 0
numarul = int(input('Gandeste-te la un numar: '))
while j <= numarul:
    sum +=j
    j +=1
print(f'Suma lui Gauss pentru {numarul} este {sum}.')'''

'''Problema 5. Rezolvati folosind doua variante: Varianta 1 -> FOR
                                                Varianta 2 -> WHILE
   Se citeste un numar n de la tastatura. Sa se scrie un program care
    face o numaratoare inversa de la numarul respectiv pana la 0.'''
# varianta for
'''numar = int(input('Gandeste-te la un numar: '))
for i in range(numar, -1,-1):
    print(i)'''
#varianta while
'''numar = int(input('Gandeste-te la un numar: '))
i = numar
while numar>=i and i >= 0:
    print(i)
    i -=1'''

'''Problema 6. Rezolvati folosind doua variante: Varianta 1 -> FOR
                                                Varianta 2 -> WHILE
    Se citeste un numar de la tastatura. Sa se calculeze 
        suma numerelor de la 1 pana la numarul citit. (folositi for si while)'''
#aceeasi cu problema 4
