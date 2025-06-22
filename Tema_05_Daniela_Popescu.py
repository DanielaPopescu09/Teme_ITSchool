'''Problema 1:
    Catalog de elevi cu fișiere TXT și JSON
    Scrie un program care:
        -Primește de la utilizator o listă de elevi (nume, prenume, nota la informatică), fiecare pe o linie, sub forma: Popescu Ana 9
        -Salvează această listă într-un fișier text elevi.txt (fiecare elev pe o linie).
        -Citește fișierul elevi.txt și salvează toți elevii sub formă de listă de dicționare în fișierul elevi.json, unde fiecare elev va avea cheile: nume, prenume, nota.
        -Afișează pe ecran toți elevii din elevi.json care au nota mai mare sau egală cu 8.
'''
import json
'''
# === Pas 1: Citire de la utilizator și salvare în elevi.txt ===
print("Introduceți elevii în formatul: Nume Prenume Nota (ex: Popescu Ana 9)")
print("Când ați terminat, apăsați Enter pe o linie goală.")

with open("elevi.txt", "w", encoding="utf-8") as f:
    while True:
        linie = input("Elev: ")
        if linie.strip() == "":
            break
        f.write(linie.strip() + "\n")

# === Pas 2: Citire din elevi.txt și salvare în elevi.json ===
lista_elevi = []

with open("elevi.txt", "r", encoding="utf-8") as f:
    for linie in f:
        parti = linie.strip().split()
        if len(parti) == 3:
            nume, prenume, nota = parti
            elev = {
                "nume": nume,
                "prenume": prenume,
                "nota": int(nota)
            }
            lista_elevi.append(elev)

with open("elevi.json", "w", encoding="utf-8") as f:
    json.dump(lista_elevi, f, indent=4, ensure_ascii=False)

# === Pas 3: Afișare elevi cu nota >= 8 din elevi.json ===
print("\nElevii cu nota mai mare sau egală cu 8:")
with open("elevi.json", "r", encoding="utf-8") as f:
    elevi_din_json = json.load(f)
    for elev in elevi_din_json:
        nota = int(elev["nota"])  # Ensure numeric comparison
        if elev["nota"] >= 8:
            print(f"{elev['nume']} {elev['prenume']} - Nota: {elev['nota']}")'''
'''Problema 2: 
    Verificarea inventarului (TXT și JSON)
        -Fie un fișier text produse.txt cu produse dintr-un depozit, fiecare produs pe o linie, sub forma:
            EX:
            -Laptop,5
            -Tableta,30
            -Telefon,8

        -Scrie un program care:
            -Citește fișierul produse.txt și salvează datele într-un fișier JSON inventar.json ca listă de dicționare (chei: produs, stoc).
            -Afișează pe ecran toate produsele care au stocul mai mic decât 10.
            -Permite utilizatorului să adauge un produs nou (nume și stoc), să actualizeze fișierele și să repete afișarea produselor cu stoc sub 10.
'''
# Creare fișier produse.txt cu exemple
with open("produse.txt", "w", encoding="utf-8") as f:
    f.write("Laptop,5\n")
    f.write("Tableta,30\n")
    f.write("Telefon,8\n")

print("Fișierul 'produse.txt' a fost creat cu succes.")
# === Pas 1: Citire produse.txt și salvare în inventar.json ===
lista_produse = []

with open("produse.txt", "r", encoding="utf-8") as f:
    for linie in f:
        linie = linie.strip()
        if linie:  # ignoră liniile goale
            try:
                nume, stoc = linie.split(",")
                produs = {
                    "produs": nume.strip(),
                    "stoc": int(stoc.strip())
                }
                lista_produse.append(produs)
            except ValueError:
                print(f"Linie invalidă ignorată: {linie}")

with open("inventar.json", "w", encoding="utf-8") as f:
    json.dump(lista_produse, f, indent=4, ensure_ascii=False)

# === Funcție de afișare a produselor cu stoc < 10 ===
def afiseaza_produse_stoc_redus():
    print("\nProduse cu stoc mai mic decât 10:")
    with open("inventar.json", "r", encoding="utf-8") as f:
        produse = json.load(f)
        exista = False
        for produs in produse:
            if int(produs["stoc"]) < 10:
                print(f"- {produs['produs']} (stoc: {produs['stoc']})")
                exista = True
        if not exista:
            print("Nu există produse cu stoc sub 10.")

# === Afișare inițială ===
afiseaza_produse_stoc_redus()

# === Pas 3: Adăugare produs nou ===
adauga = input("\nDoriți să adăugați un produs nou? (da/nu): ").strip().lower()
if adauga == "da":
    nume_nou = input("Introduceți numele produsului: ").strip()
    stoc_nou = input("Introduceți stocul: ").strip()

    try:
        stoc_nou = int(stoc_nou)
        # Adăugare în lista deja existentă
        lista_produse.append({
            "produs": nume_nou,
            "stoc": stoc_nou
        })
        # Rescriere fișier JSON
        with open("inventar.json", "w", encoding="utf-8") as f:
            json.dump(lista_produse, f, indent=4, ensure_ascii=False)

        # Rescriere fișier produse.txt (opțional)
        with open("produse.txt", "w", encoding="utf-8") as f:
            for item in lista_produse:
                f.write(f"{item['produs']},{item['stoc']}\n")

        print("\nProdus adăugat cu succes.")
        afiseaza_produse_stoc_redus()

    except ValueError:
        print("Stocul introdus nu este un număr valid.")
