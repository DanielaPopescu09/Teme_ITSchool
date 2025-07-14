import sqlite3
import os
#from fpdf import FPDF
import csv

DB_FILE = 'angajati.db'

def conectare():
    return sqlite3.connect(DB_FILE)

def init_db():
    with conectare() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS angajati (
                cnp TEXT PRIMARY KEY,
                nume TEXT,
                prenume TEXT,
                varsta INTEGER,
                salariu INTEGER,
                departament TEXT,
                senioritate TEXT
            )
        ''')
        conn.commit()

def creare_angajat(cnp, nume, prenume, varsta, salariu, departament, senioritate):
    if len(cnp) != 13 or not cnp.isdigit():
        print("CNP invalid.")
        return None
    if not isinstance(varsta, int) or varsta <= 18:
        print("Varsta invalida (trebuie > 18).")
        return None
    if not isinstance(salariu, int) or salariu <= 4050:
        print("Salariul trebuie sa fie > 4050.")
        return None
    return (cnp, nume, prenume, varsta, salariu, departament, senioritate)

def populare_initiala():
    angajati = [
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
    # with conectare() as conn:
    #     for ang in angajati:
    #         if creare_angajat(*ang):
    #             try:
    #                 conn.execute("INSERT INTO angajati VALUES (?, ?, ?, ?, ?, ?, ?)", ang)
    #             except sqlite3.IntegrityError:
    #                 continue
    #     conn.commit()
    with conectare() as conn:
        for ang in angajati:
            cnp = ang[0]
            nume = ang[1]
            prenume = ang[2]
            varsta = ang[3]
            salariu = ang[4]
            departament = ang[5]
            senioritate = ang[6]

            if creare_angajat(cnp, nume, prenume, varsta, salariu, departament, senioritate):
                try:
                    conn.execute(
                        "INSERT INTO angajati VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (cnp, nume, prenume, varsta, salariu, departament, senioritate)
                    )
                except sqlite3.IntegrityError:
                    continue
        conn.commit()

def adauga_angajat():
    cnp = input("CNP: ")
    nume = input("Nume: ")
    prenume = input("Prenume: ")
    varsta = int(input("Varsta: "))
    salariu = int(input("Salariu: "))
    departament = input("Departament: ")
    senioritate = input("Senioritate (junior/mid/senior): ")
    ang = creare_angajat(cnp, nume, prenume, varsta, salariu, departament, senioritate)
    if ang:
        with conectare() as conn:
            conn.execute("INSERT INTO angajati VALUES (?, ?, ?, ?, ?, ?, ?)", ang)
            conn.commit()
            print("Angajat adaugat.")

def cauta_angajat():
    cnp = input("CNP de cautat: ")
    with conectare() as conn:
        c = conn.execute("SELECT * FROM angajati WHERE cnp = ?", (cnp,))
        row = c.fetchone()
        if row:
            print(row)
        else:
            print("Angajat inexistent.")

def modifica_angajat():
    cnp = input("CNP angajat de modificat: ")
    with conectare() as conn:
        c = conn.execute("SELECT * FROM angajati WHERE cnp = ?", (cnp,))
        row = c.fetchone()
        if not row:
            print("CNP inexistent.")
            return
        nume = input(f"Nume ({row[1]}): ") or row[1]
        prenume = input(f"Prenume ({row[2]}): ") or row[2]
        varsta = int(input(f"Varsta ({row[3]}): ") or row[3])
        salariu = int(input(f"Salariu ({row[4]}): ") or row[4])
        departament = input(f"Departament ({row[5]}): ") or row[5]
        senioritate = input(f"Senioritate ({row[6]}): ") or row[6]
        ang = creare_angajat(cnp, nume, prenume, varsta, salariu, departament, senioritate)
        if ang:
            conn.execute("UPDATE angajati SET nume=?, prenume=?, varsta=?, salariu=?, departament=?, senioritate=? WHERE cnp=?", (nume, prenume, varsta, salariu, departament, senioritate, cnp))
            conn.commit()
            print("Modificare finalizata.")

def sterge_angajat():
    cnp = input("CNP de sters: ")
    with conectare() as conn:
        conn.execute("DELETE FROM angajati WHERE cnp = ?", (cnp,))
        conn.commit()
        print("Angajat sters.")

def afisare_angajati():
    with conectare() as conn:
        c = conn.execute("SELECT * FROM angajati")
        for row in c.fetchall():
            print(row)

def cost_total():
    with conectare() as conn:
        c = conn.execute("SELECT SUM(salariu) FROM angajati")
        print(f"Cost total salarii: {c.fetchone()[0]} RON")

def cost_pe_departament():
    dep = input("Departament: ")
    with conectare() as conn:
        c = conn.execute("SELECT SUM(salariu) FROM angajati WHERE departament = ?", (dep,))
        print(f"Cost salarii {dep}: {c.fetchone()[0]} RON")

def fluturas():
    cnp = input("CNP: ")
    with conectare() as conn:
        c = conn.execute("SELECT nume, prenume, salariu FROM angajati WHERE cnp = ?", (cnp,))
        row = c.fetchone()
        if row:
            brut = row[2]
            cas = brut * 0.10
            cass = brut * 0.25
            impozit = (brut - cas - cass) * 0.10
            net = brut - cas - cass - impozit
            print(f"Fluturas: {row[0]} {row[1]} - Net: {net:.2f} RON")
        else:
            print("Angajat inexistent.")

# def sortare_senioritate():
#     ord_sen = {'junior': 1, 'mid': 2, 'senior': 3}
#     with conectare() as conn:
#         c = conn.execute("SELECT * FROM angajati")
#         angajati = c.fetchall()
#         sortati = sorted(angajati, key=lambda a: ord_sen.get(a[6], 0))
#         for a in sortati:
#             print(a)
def get_seniority(a):
    ord_sen = {'junior': 1, 'mid': 2, 'senior': 3}
    return ord_sen.get(a[6], 0)

def sortare_senioritate():
    with conectare() as conn:
        c = conn.execute("SELECT * FROM angajati")
        angajati = c.fetchall()
        sortati = sorted(angajati, key=get_seniority)
        for a in sortati:
            print(a)

def sortare_departament():
    with conectare() as conn:
        c = conn.execute("SELECT * FROM angajati ORDER BY departament")
        for a in c.fetchall():
            print(a)

def meniu():
    while True:
        print("\n--- MENIU ---")
        print("1) Adaugare angajat")
        print("2) Cautare angajat")
        print("3) Modificare angajat")
        print("4) Stergere angajat")
        print("5) Afisare angajati")
        print("6) Cost total salarii")
        print("7) Cost salarii departament")
        print("8) Fluturas salariu")
        print("9) Sortare senioritate")
        print("10) Sortare departament")
        print("11) Iesire")
        opt = input("Alege: ")
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
            break
        else:
            print("Optiune invalida.")

# Initializare si rulare
init_db()
populare_initiala()
meniu()