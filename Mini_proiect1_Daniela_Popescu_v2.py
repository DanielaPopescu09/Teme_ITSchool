'''
Mini proiect
Sa se scrie un program care tine evidenta angajatilor dintr-o companie.
Informatiile pe care trebuie sa le retinem despre un angajat sunt urmatoarele:
	1) CNP
	2) Nume
	3) Prenume
	4) Varsta
	5) Salar
	6) Departament
	7) Senioritate (junior, mid, senior)

Programul trebuie sa dispuna de un meniu care ne permite sa efectuam urmatoarele actiuni:
	1) Adaugare angajat
	2) Cautare angajat (dupa CNP)
	3) Modificare date angajat (dupa CNP)
	4) Stergere angajat
	5) Afisare angajati
	6) Calculator cost total salarii
	7) Calculator cost total salarii departament
	8) Calculator fluturas salar angajat (CAS - 10% din brut, CASS - 25% din brut, Impozit - 10% din ce a ramas)
	9) Afisarea angajatilor (dupa senioritate)
	10) Afisarea angajatilor (dupa departament)
	11) Iesire

Criterii notare:
	- Lizibilitate cod
	- Documentatie cod
	- Denumire variabile
	- Functionalitate
	- Verificare integriatate date (parametrii introdusi sa fie corespunzatori)
		○ Exemplu:
			§ CNP sa fie de lungime corespunzatoare si sa contina doar cifre
			§ Varsta sa fie mai mare de 18 ani
			§ Salarul sa fie mai mare decat minimul (4050)
			etc
'''
def validare_cnp(cnp):
    return len(cnp) == 13 and cnp.isdigit()

def validare_varsta(varsta):
    return isinstance(varsta, int) and varsta > 18

def validare_salariu(salariu):
    return isinstance(salariu, int) and salariu > 4050

def creare_angajat(cnp, nume, prenume, varsta, salariu, departament, senioritate):
    if not validare_cnp(cnp):
        print("CNP invalid.")
        return None
    if not validare_varsta(varsta):
        print("Varsta invalida (trebuie > 18).")
        return None
    if not validare_salariu(salariu):
        print("Salariul trebuie sa fie > 4050.")
        return None

    return {
        'CNP': cnp,
        'Nume': nume,
        'Prenume': prenume,
        'Varsta': varsta,
        'Salariu': salariu,
        'Departament': departament,
        'Senioritate': senioritate
    }

# Dicționar angajați
angajati = {}

# Lista inițială
lista_angajati = [
    ("2234567890121", "Popescu", "Ana", 30, 5001, "HR", "mid"),
    ("1234567890122", "Ionescu", "Dan", 45, 7000, "IT", "senior"),
    ("2234567890123", "Georgescu", "Elena", 28, 4501, "Marketing", "junior"),
    ("1234567890124", "Vasilescu", "Andrei", 22, 4200, "IT", "junior"),
    ("2234567890125", "Petrescu", "Ioana", 38, 6000, "Finance", "mid"),
    ("2234567890126", "Stan", "Cristina", 41, 8000, "HR", "senior"),
    ("1234567890127", "Dumitru", "Mihai", 26, 4700, "Marketing", "mid"),
    ("2234567890128", "Pop", "Larisa", 24, 4300, "Finance", "junior"),
    ("1234567890129", "Nistor", "Robert", 35, 7500, "IT", "senior"),
    ("1234567890120", "Tudor", "Gabriel", 29, 5100, "HR", "mid")
]

for entry in lista_angajati:
    cnp, nume, prenume, varsta, salariu, departament, senioritate = entry
    angajat = creare_angajat(cnp, nume, prenume, varsta, salariu, departament, senioritate)
    if angajat:
        angajati[angajat['CNP']] = angajat

def adauga_angajat():
    try:
        cnp = input("CNP: ")
        nume = input("Nume: ")
        prenume = input("Prenume: ")
        varsta = int(input("Varsta: "))
        salariu = int(input("Salariu: "))
        departament = input("Departament: ")
        senioritate = input("Senioritate (junior/mid/senior): ").lower()
        angajat = creare_angajat(cnp, nume, prenume, varsta, salariu, departament, senioritate)
        if angajat:
            angajati[cnp] = angajat
            print("Angajat adaugat cu succes.")
        else:
            print("Angajatul NU a fost adaugat din cauza unor erori.")
    except Exception as e:
        print("Eroare:", e)

def cauta_angajat():
    cnp = input("Introdu CNP: ")
    angajat = angajati.get(cnp)
    if angajat:
        print(angajat)
    else:
        print("Angajatul nu a fost gasit.")

def modifica_angajat():
    cnp = input("CNP angajat de modificat: ")
    if cnp not in angajati:
        print("Angajatul nu exista.")
        return
    angajat = angajati[cnp]
    nume = input(f"Nume ({angajat['Nume']}): ") or angajat['Nume']
    prenume = input(f"Prenume ({angajat['Prenume']}): ") or angajat['Prenume']
    try:
        varsta = int(input(f"Varsta ({angajat['Varsta']}): ") or angajat['Varsta'])
        salariu = int(input(f"Salariu ({angajat['Salariu']}): ") or angajat['Salariu'])
        departament = input(f"Departament ({angajat['Departament']}): ") or angajat['Departament']
        senioritate = input(f"Senioritate ({angajat['Senioritate']}): ") or angajat['Senioritate']
        angajati[cnp] = creare_angajat(cnp, nume, prenume, varsta, salariu, departament, senioritate)
        print("Angajat modificat.")
    except Exception as e:
        print("Eroare:", e)

def sterge_angajat():
    cnp = input("CNP de sters: ")
    if cnp in angajati:
        del angajati[cnp]
        print("Angajat sters.")
    else:
        print("CNP inexistent.")

def afisare_angajati():
    for ang in angajati.values():
        print(f"{ang['CNP']}: {ang['Nume']} {ang['Prenume']}, {ang['Varsta']} ani, {ang['Salariu']} RON, {ang['Departament']}, {ang['Senioritate']}")

def cost_total():
    total = sum(ang['Salariu'] for ang in angajati.values())
    print(f"Cost total salarii: {total} RON")

def cost_pe_departament():
    dep = input("Departament: ")
    total = sum(ang['Salariu'] for ang in angajati.values() if ang['Departament'] == dep)
    print(f"Cost salarii pentru departamentul {dep}: {total} RON")

def fluturas():
    cnp = input("CNP angajat: ")
    ang = angajati.get(cnp)
    if not ang:
        print("Angajatul nu a fost gasit.")
        return
    brut = ang['Salariu']
    cas = brut * 0.10
    cass = brut * 0.25
    impozit = (brut - cas - cass) * 0.10
    net = brut - cas - cass - impozit
    print(f"Fluturas salariu {ang['Nume']} {ang['Prenume']} - Brut: {brut}, CAS: {cas:.2f}, CASS: {cass:.2f}, Impozit: {impozit:.2f}, Net: {net:.2f}")

def get_ordine_senioritate(angajat):
    ord_sen = {'junior': 1, 'mid': 2, 'senior': 3}
    return ord_sen.get(angajat['Senioritate'], 0)
def sortare_senioritate():
    lista = sorted(angajati.values(), key=get_ordine_senioritate)
    for ang in lista:
        print(
            f"{ang['CNP']}: {ang['Nume']} {ang['Prenume']}, {ang['Varsta']} ani, "
            f"{ang['Salariu']} RON, {ang['Departament']}, {ang['Senioritate']}")

def get_departament(angajat):
    return angajat['Departament']
def sortare_departament():
    lista = sorted(angajati.values(), key=get_departament)
    for ang in lista:
        print(
            f"{ang['CNP']}: {ang['Nume']} {ang['Prenume']}, {ang['Varsta']} ani, "
            f"{ang['Salariu']} RON, {ang['Departament']}, {ang['Senioritate']}")

def meniu():
    while True:
        print("\n--- MENIU ---")
        print("1) Adaugare angajat")
        print("2) Cautare angajat (dupa CNP)")
        print("3) Modificare date angajat")
        print("4) Stergere angajat")
        print("5) Afisare angajati")
        print("6) Cost total salarii")
        print("7) Cost salarii departament")
        print("8) Fluturas salariu")
        print("9) Afisare angajati dupa senioritate")
        print("10) Afisare angajati dupa departament")
        print("11) Iesire")
        opt = input("Alege optiunea: ")
        if opt == '1':
            adauga_angajat()
        elif opt == '2':
            cauta_angajat()
        elif opt == '3':
            modifica_angajat()
        elif opt == '4':
            sterge_angajat()
        elif opt == '5':
            afisare_angajati()
        elif opt == '6':
            cost_total()
        elif opt == '7':
            cost_pe_departament()
        elif opt == '8':
            fluturas()
        elif opt == '9':
            sortare_senioritate()
        elif opt == '10':
            sortare_departament()
        elif opt == '11':
            print("Multumesc. La revedere!")
            break
        else:
            print("Optiune invalida.")
meniu()

