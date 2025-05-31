'''Problema 1.
Creeaza un catalog scolar care:
-Primeste de la utilizator numele elevilor si notele acestora
-Salveaza aceste informatii intr-o lista de forma catalog = [['Ana', [9, 10, 8], ['Mihai', [6, 7, 9]] etc
-Afiseaza: - media fiecarui elev
            - elevii care au media >= 5 -> promovat
            - elevii cu media < 5 -> corigenti ***(am facut la curs partea asta)***
-Functie adaugare elev
-Functie afisare rezultate
-Modificare note elev
-Stergere elev din catalog
-Exit
'''
'''catalog = [
    ['Iulia', [10, 8, 9]],
    ['Alex', [6, 10, 9]],
    ['Ioana', [5, 4, 4]]
]
def afiseaza_promovati(catalog):
    for elev in catalog:
        nume = elev[0]
        note = elev[1]
        media = sum(note) / len(note)
        if media >= 5:
            print(f"{nume} a promovat cu media {media:.1f}")
        else:
            print(f"{nume} este corigent, avand media {media:.1f}")
#afiseaza_promovati(catalog)
def adauga_elev(catalog):
    nume = input("Introdu numele elevului: ")
    note = []
    i=0
    for i in range (3):
        n= int(input(f'Introdu nota {i+1}: '))
        note.append(n)
    catalog.append([nume, note])
    print(f'Elevul {nume} a fost adaugat cu notele {note}.')
def afisare_rezultat(catalog):
    for elev in catalog:
        nume = elev[0]
        note = elev[1]
        media = sum(note) / len(note)
        print(f"Media generala a elevului {nume} este: {media:.2f}")
def modifica_note(catalog):
    nume = input("Introdu numele elevului caruia vrei sa-i modifici notele: ")
    note = []
    for i in range (3):
        n = int(input(f"Introdu nota {i+1}: "))
        note.append(n)
    print(f"Elevul {nume} are notele actualizate astfel: {note}.")
def sterge_elev(catalog):
    nume = input("Introdu numele elevului pe care vrei sa-l stergi: ")
    for elev in catalog:
        if elev[0] == nume:
            catalog.remove(elev)
            print(f'Elevul {nume} a fost sters, iar noul catalog este: {catalog}')
        else:
            print("Elevul nu a fost gasit.")
def meniu():
    while True:
        print("\n--- MENIU ---")
        print("1. Afiseaza promovati / corigenti")
        print("2. Adauga elev")
        print("3. Afiseaza medii")
        print("4. Modifica note elev")
        print("5. Sterge elev")
        print("6. Iesire")
        optiune = input("Alege o optiune: ")
        if optiune == '1':
            afiseaza_promovati(catalog)
        elif optiune == '2':
            adauga_elev(catalog)
        elif optiune == '3':
            afisare_rezultat(catalog)
        elif optiune == '4':
            modifica_note(catalog)
        elif optiune == '5':
            sterge_elev(catalog)
        elif optiune == '6':
            print("Iesire...")
            break
        else:
            print("Optiune invalida. Incearca din nou.")
meniu()'''

'''Problema 2. Detecteaza operatorul de telefonie mobila din Romania folosind liste si prefixe.
Accepta formate : -0xxxxxxxxx
                  -+40xxxxxxxxx
                  -0040xxxxxxxxx
vodafone: 72, 73
orange: 74, 75
telekom: 76, 78
digi: 77

Hints: -curatare spatii si liniute(folositi replace() )
        -Standardizare in format local 0xxxxxxxxx
        -Validare basic: 10 cifre, toate digits, incepe cu 0
        -Extrage prefixul
        -Defineste liste pentru prefixe operator
        -Lista generala operatori ( fiecare element este [nume, lista prefixe]
        -Cauta in liste
        -Afiseaza rezultatul'''
'''def detecteaza_operator(numar):
    numar = numar.replace(" ", "").replace("-", "")
    if numar[0:3]=="+40":
        numar = "0" + numar[3:]
    elif numar[0:4]=="0040":
        numar = "0" + numar[4:]
    if len(numar) != 10 or not numar.isdigit() or not numar[0]=="0":
        print("Numar invalid!")
        return
    prefix = numar[1:3]
    vodafone = ['72', '73']
    orange = ['74', '75']
    telekom = ['76', '78']
    digi = ['77']
    operatori = [
        ['Vodafone', vodafone],
        ['Orange', orange],
        ['Telekom', telekom],
        ['Digi', digi]
    ]
    for operator in operatori:
        nume, prefixe = operator
        if prefix in prefixe:
            print(f"Numarul {numar} apartine operatorului {nume}.")
            return
    print("Operator necunoscut.")
numar_utilizator = input("Introdu numarul de telefon: ")
detecteaza_operator(numar_utilizator)'''