#Din Tema1
'''Problema 1. Operatii aritmetice
Scrie un program care:
    - Cere doua numere si calculeaza:
        - Suma
        - Diferenta
        - Produsul
        - Impartirea
        - Imaprtirea intreaga
        - Restul impartirii (modulo)
        - Puterea
    - La final, afiseaza fiecare rezultat
'''

#Incepe de aici problema 1
'''Numar_A = float(input(f'Ptrimul numar este: '))
Numar_B = float(input(f'Al doilea numar este: '))
def adunare(a, b):
    return a + b
Suma = adunare(Numar_A, Numar_B)
#Suma = Numar_A + Numar_B
def scadere(a,b):
    return a-b
Diferenta = scadere(Numar_A,Numar_B)
#Diferenta = Numar_A - Numar_B
def inmultire(a,b):
    return a*b
Produsul = inmultire(Numar_A,Numar_B)
#Produsul = Numar_A * Numar_B
def cat(a,b):
    return a/b
Impartirea = cat(Numar_A,Numar_B)
#Impartirea = Numar_A / Numar_B
def imp_int(a,b):
    return a//b
Impartirea_intreaga = imp_int(Numar_A,Numar_B)
#Impartirea_intreaga = Numar_A // Numar_B
def rest(a,b):
    return a%b
Restul_impartirii = rest(Numar_A,Numar_B)
#Restul_impartirii = Numar_A % Numar_B
def putere(a,b):
    return a**b
Puterea = putere(Numar_A,Numar_B)
#Puterea = Numar_A ** Numar_B
print(f"Suma celor doua numere este: {Suma:.2f},\n Diferenta celor douia numere este: {Diferenta:.2f}, \n Produsul lor este: {Produsul:.4f}, \n Impartirea lor este: {Impartirea:.2f}, \n Impartirea intreaga rezultata este: {Impartirea_intreaga}, \n Restul impartirii numerelor este: {Restul_impartirii}, \n Puterea dintre cele doua numere este: {Puterea:.4f}")'''
#Sfarsit problema 1


''' Problema 3. Transforma din minute in ore si minute
    - Primeste de la tastatura un numar de minute(ex. 135)
    - Afiseaza cate ore si minute reprezinta acel numar
'''

#Incepe de aici problema 3
'''Numar_minute = int(input('Numarul de minute ales este: '))
def ore(a):
    return a//60
Numar_ore = ore(Numar_minute)
#Numar_ore = Numar_minute//60
def min(a):
    return a%60
Numar_minute_ramas = min(Numar_minute)
#Numar_minute_ramas = Numar_minute - Numar_ore*60
print(f'Numarul de ore incluse in {Numar_minute} este: {Numar_ore} ore, iar numarul de minute este de: {Numar_minute_ramas} minute')'''
#Sfarsit problema 3


''' Problema 4. Bonul de cumparaturi
O persoana cumpara 3 produse. Vrem sa afisam:
    - Totalul fara TVA
    - TVA(ex. 19%)
    - Totalul cu TVA
'''

#Incepe de aici problema 4
#varianta 1
'''Produs_1 = float(input('Costul primului produs este:'))
Produs_2 = float(input('Costul celui de-al doilea produs este:'))
Produs_3 = float(input('Costul celui de-al treilea produs este:'))
Produse = Produs_1 + Produs_2 + Produs_3
def net(a):
    return a/1.19
Total_fara_TVA = net(Produse)
#Total_fara_TVA = (Produs_1 + Produs_2 + Produs_3)/1.19
def tva(a):
    return a*0.19
TVA = tva(Produse)
#TVA = (Produs_1 + Produs_2 + Produs_3)*0.19
Total_cu_TVA = Produse
print(f"Totalul fara TVA al celor trei produse este: {Total_fara_TVA:.2f}, \nTVA-ul celor trei produse este: {TVA:.2f}, iar \nTotalul cu TVA al acestora este: {Total_cu_TVA}")'''
#varianta2
'''def calculeaza_TVA():
    Produs_1 = float(input('Costul primului produs este: '))
    Produs_2 = float(input('Costul celui de-al doilea produs este: '))
    Produs_3 = float(input('Costul celui de-al treilea produs este: '))
    Total_cu_TVA = Produs_1 + Produs_2 + Produs_3
    Total_fara_TVA = Total_cu_TVA / 1.19
    TVA = Total_cu_TVA * 0.19
    print(f"Totalul fara TVA al celor trei produse este: {Total_fara_TVA:.2f}, \nTVA-ul celor trei produse este: {TVA:.2f}, iar \nTotalul cu TVA al acestora este: {Total_cu_TVA}")
calculeaza_TVA()'''
#Sfarsit problema 4

'''Problema 5. Bugetul pentru un concediu
Cerinta: Un grup de prieteni planuieste o vacanta. Trebuie sa calculezi: 
    - Contributia totala
    - Costul cheltuielilor (transport, cazare, mancare pe zile)
    - Ce suma ramane pentru distractii

Date de intrare: 
    - Numarul de prieteni
    - Suma de bani per persoana
    - Costul transportului
    - Costul pe zi pentru cazare
    - Costul pe zi pentru mancare
    - Numarul de zile
'''
#Incepe de aici problema 5
'''def calcul_buget():
    Numar_prieteni = int(input('Numarul de prieteni este:'))
    Suma_persoana = int(input('Suma cu care contribuie fiecare persoana este:'))
    Cost_transport = float(input('Costul transportului este:'))
    Cost_cazare_zi = float(input('Costul cazarii zilnic este:'))
    Cost_mancare_zi = float(input('Costul pe mancare zilnic este:'))
    Numar_zile = int(input('Numarul de zile de vacanta este:'))
    print(f'Contributia totala este: {Numar_prieteni*Suma_persoana:.2f}, \nCostul total al cheltuielilor este: {Cost_transport+(Cost_cazare_zi+Cost_mancare_zi)*Numar_zile:.2f}, iar \nSuma pentru distractii ramasa este: {Numar_prieteni*Suma_persoana-(Cost_transport+(Cost_cazare_zi+Cost_mancare_zi)*Numar_zile):.2f}')
calcul_buget()'''
#Sfarsit problema 5


#Din Tema2
'''Problema 1. Se citeste de la tastatura o parola. Sa se verifice daca parola introdusa are
    cel putin 10 caractere si nu contine spatiu.
Sa se afiseze un mesaj corespunzator pentru fiecare neregula gasita
    sau mesajul "OK" in cazul in care parola respecta regulile.
    hints: boolean, conditionals'''
'''def verifica_parola():
    parola = input('Parola aleasa este: ')
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
    print ('Felicitari! Parola implineste ambele conditii de lungime si spatii goale.')
verifica_parola()'''

'''Problema 2. Sa se numere de cate ori apare o litera intr-un cuvant.'''
'''def verif_aparitii_litera():
    suma = 0
    cuvant = input('Cuvantul ales este: ')
    litera = input(f'Alege o litera pe care sa o verifici daca apare in {cuvant}: ')
    for x in cuvant:
        if x == litera:
            suma +=1
    print (f"Litera {litera} apare de {suma} ori in cuvantul {cuvant}.")
verif_aparitii_litera()'''

'''Problema 3. Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.'''
'''def afiseaza_puteri_3_intre_200_300():
    for i in range (1,10):
        power = 3 ** i
        if power >= 200 and power <= 300:
            print (f'3 la puterea {i} este {power}')
afiseaza_puteri_3_intre_200_300()'''

'''Problema 4. Se citeste un numar de la tastatura. 
    Sa se calculeze suma numerelor de la 1 pana la numarul citit. (folositi for si while)'''
#varianta for
'''def calcul_gauss():
    suma = 0
    numar = int(input('Gandeste-te la un numar: '))
    for i in range(1,numar +1):
        suma += i
    print(f'Suma lui Gauss pentru {numar} este {suma}.')
calcul_gauss()'''
#varianta while
'''def calcul_gauss2():
    sum = 0
    j = 0
    numarul = int(input('Gandeste-te la un numar: '))
    while j <= numarul:
        sum +=j
        j +=1
    print(f'Suma lui Gauss pentru {numarul} este {sum}.')
calcul_gauss2()'''

'''Problema 5. Rezolvati folosind doua variante: Varianta 1 -> FOR
                                                Varianta 2 -> WHILE
   Se citeste un numar n de la tastatura. Sa se scrie un program care
    face o numaratoare inversa de la numarul respectiv pana la 0.'''
# varianta for
'''def numar_invers():
    numar = int(input('Gandeste-te la un numar: '))
    for i in range(numar, -1,-1):
        print(i)
numar_invers()'''
#varianta while
'''def numar_invers2():
    numar = int(input('Gandeste-te la un numar: '))
    i = numar
    while numar>=i and i >= 0:
        print(i)
        i -=1
numar_invers2()'''


