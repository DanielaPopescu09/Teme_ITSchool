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
Suma = Numar_A + Numar_B
Diferenta = Numar_A - Numar_B
Produsul = Numar_A * Numar_B
Impartirea = Numar_A / Numar_B
Impartirea_intreaga = Numar_A // Numar_B
Restul_impartirii = Numar_A % Numar_B
Puterea = Numar_A ** Numar_B
print(f"Suma celor doua numere este: {Suma:.2f},\n Diferenta celor douia numere este: {Diferenta:.2f}, \n Produsul lor este: {Produsul:.4f}, \n Impartirea lor este: {Impartirea:.2f}, \n Impartirea intreaga rezultata este: {Impartirea_intreaga}, \n Restul impartirii numerelor este: {Restul_impartirii}, \n Puterea dintre cele doua numere este: {Puterea:.4f}")'''
#Sfarsit problema 1


'''Problema 2. Tipuri de date
Declara cate o variabila pentru fiecare tip de date studiat si afiseaza tipul acesteia
'''
#Incepe de aici problema 2
'''Numar_intreg = int(input("Numarul intreg este: "))
Numar_real = float(input('Numarul real este: '))
Numar_complex = complex(input('Numarul complex este: '))
Variabila_text = input('Variabila text este: ')
Variabila_boolean = bool(input('Variabila true/false este: '))
print('Tipurile de variabile declarate sunt: ')
print(f' {Numar_intreg} este: ',type(Numar_intreg),f'\n {Numar_real} este: ',type(Numar_real),f'\n{Numar_complex} este: ',type(Numar_complex),f'\n{Variabila_text} este:',type(Variabila_text),f'\n{Variabila_boolean} este: ',type(Variabila_boolean))'''
#Sfarsit problema 2


''' Problema 3. Transforma din minute in ore si minute
    - Primeste de la tastatura un numar de minute(ex. 135)
    - Afiseaza cate ore si minute reprezinta acel numar
'''

#Incepe de aici problema 3
'''Numar_minute = int(input('Numarul de minute ales este: '))
Numar_ore = Numar_minute//60
Numar_minute_ramas = Numar_minute - Numar_ore*60
print(f'Numarul de ore incluse in {Numar_minute} este: {Numar_ore} ore, iar numarul de minute este de: {Numar_minute_ramas} minute')'''
#Sfarsit problema 3


''' Problema 4. Bonul de cumparaturi
O persoana cumpara 3 produse. Vrem sa afisam:
    - Totalul fara TVA
    - TVA(ex. 19%)
    - Totalul cu TVA
'''

#Incepe de aici problema 4
'''Produs_1 = float(input('Costul primului produs este:'))
Produs_2 = float(input('Costul celui de-al doilea produs este:'))
Produs_3 = float(input('Costul celui de-al treilea produs este:'))
Total_fara_TVA = (Produs_1 + Produs_2 + Produs_3)/1.19
TVA = (Produs_1 + Produs_2 + Produs_3)*0.19
Total_cu_TVA = Produs_1 + Produs_2 + Produs_3
print(f"Totalul fara TVA al celor trei produse este: {Total_fara_TVA:.2f}, \nTVA-ul celor trei produse este: {TVA:.2f}, iar \nTotalul cu TVA al acestora este: {Total_cu_TVA}")'''
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
'''Numar_prieteni = int(input('Numarul de prieteni este:'))
Suma_persoana = int(input('Suma cu care contribuie fiecare persoana este:'))
Cost_transport = float(input('Costul transportului este:'))
Cost_cazare_zi = float(input('Costul cazarii zilnic este:'))
Cost_mancare_zi = float(input('Costul pe mancare zilnic este:'))
Numar_zile = int(input('Numarul de zile de vacanta este:'))
print(f'Contributia totala este: {Numar_prieteni*Suma_persoana:.2f}, \nCostul total al cheltuielilor este: {Cost_transport+(Cost_cazare_zi+Cost_mancare_zi)*Numar_zile:.2f}, iar \nSuma pentru distractii ramasa este: {Numar_prieteni*Suma_persoana-(Cost_transport+(Cost_cazare_zi+Cost_mancare_zi)*Numar_zile):.2f}')'''
#Sfarsit problema 5