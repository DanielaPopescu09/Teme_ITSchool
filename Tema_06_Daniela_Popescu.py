'''
Creeaza un script care executa urmatoarele operatii:

1. Creeaza tabelul studenti cu coloanele:
    -id
    -nume
    -varsta
2. Adauga cel putin 5 studenti cu valori diferite pentru nume si varsta
    - Foloseste parametrizare si inserari multiple
3. Afiseaza toti studentii
4. Afiseaza studentii cu varsta > 20
5. Afiseaza studentii al caror nume incepe cu litera A
6. Creste varsta cu 1 pentru un student
    -Afiseaza dupa aceea randul modificat pentru a verifica schimbarea
7. Sterge toti studentii cu varsta < 19
    -Afiseaza toti studentii pentru a verifica rezultatul
8. Daca exista deja tabela studenti, sterge-o pentru a nu face append cu datele precedente
9. Adauga o coloana email
    - Pentru studentul cu id = 1 seteaza un mail si verifica comanda
Spor
'''
import sqlite3
#0. Conectare la baza de date (sau creare dacă nu există)
conn = sqlite3.connect("studenti.db")
cursor = conn.cursor()

#8.Șterge tabela dacă există
cursor.execute('DROP TABLE IF EXISTS studenti')

#1.Creare tabel
cursor.execute('''
    CREATE TABLE IF NOT EXISTS studenti(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nume TEXT NOT NULL,
        varsta INTEGER
    )
''')

# 2.Adauga cel putin 5 studenti cu valori diferite pentru nume si varsta
studenti = [
    ("Tudor_Popescu", 19),
    ("Iulia_Ionescu", 18),
    ("Petru_Petrescu", 20),
    ("Marius_Marinescu", 22),
    ("Aura_Enescu", 20)
]
cursor.executemany("INSERT INTO studenti (nume, varsta) VALUES (?, ?)", studenti)
conn.commit()

# 3. Afișează toți studenții
#v1
print("\n3.v1. Toți studenții:")
for row in cursor.execute("SELECT * FROM studenti"):
    print(row)
#v2
cursor.execute('SELECT * FROM studenti')
print("3.v2. ")
for row in cursor.fetchall():
    print(f"{row[1]},{row[2]}")

# 4. Afișează studenții cu vârsta > 20
#v1
print("\n4.v1.Studenți cu vârsta > 20:")
for row in cursor.execute("SELECT * FROM studenti WHERE varsta > 20"):
    print(row)
#v2
cursor.execute('SELECT nume, varsta FROM studenti WHERE varsta > ?', (20, ))
print("4.v2. ")
for nume, varsta in cursor.fetchall():
    print(f"{nume}: {varsta} ani")

# 5. Afișează studenții al căror nume începe cu 'A'
#v1
print("\n5.v1. Studenți al căror nume începe cu 'A':")
for row in cursor.execute("SELECT * FROM studenti WHERE nume LIKE 'A%'"):
    print(row)
#v2
cursor.execute('SELECT nume FROM studenti WHERE nume LIKE "A%"')
print("5.v2. ")
for nume in cursor.fetchall():
    print(f"nume care incepe cu A: {nume}")

# 6. Crește vârsta cu 1 pentru un student (ex: studentul cu id = 1)
cursor.execute("UPDATE studenti SET varsta = varsta + 1 WHERE id = 1")
conn.commit()

print("\nStudentul cu id = 1 după actualizare:")
cursor.execute("SELECT * FROM studenti WHERE id = 1")
print(cursor.fetchone())

# 7. Șterge studenții cu vârsta < 19
cursor.execute("DELETE FROM studenti WHERE varsta < 19")
conn.commit()

print("\nStudenți după ștergerea celor cu vârsta < 19:")
for row in cursor.execute("SELECT * FROM studenti"):
    print(row)

# 9. Adaugă o coloană email
cursor.execute("ALTER TABLE studenti ADD COLUMN email TEXT")
conn.commit()

# Setează email pentru studentul cu id = 1
cursor.execute("UPDATE studenti SET email = 'tudor_popescu@school.com' WHERE id = 1")
conn.commit()

print("\nStudentul cu id = 1 după adăugarea emailului:")
cursor.execute("SELECT * FROM studenti WHERE id = 1")
print(cursor.fetchone())

# Închide conexiunea
conn.close()