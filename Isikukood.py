from math import *
from random import *

# === Funktsioonid (endine Omamoodul1.py) ===
def Sugu(ik_list: list) -> str:
    # Määrame soo esimese numbri järgi
    if int(ik_list[0]) % 2 == 0:
        return "naine"
    else:
        return "mees"


def Sunnikoht(a: int) -> str:
    # Määrame sünnikoha numbri põhjal
    if 1 <= a <= 10:
        haigla = "Kuresaare Haigla"
    elif 11 <= a <= 19:
        haigla = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= a <= 220:
        haigla = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla, Loksa"
    elif 221 <= a <= 270:
        haigla = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= a <= 370:
        haigla = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371 <= a <= 420:
        haigla = "Narva Haigla"
    elif 471 <= a <= 490:
        haigla = "Pärnu Haigla"
    elif 491 <= a <= 520:
        haigla = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu Haigla"
    elif 521 <= a <= 570:
        haigla = "Järvamaa Haigla (Paide)"
    elif 571 <= a <= 600:
        haigla = "Valga Haigla"
    elif 601 <= a <= 650:
        haigla = "Viljandi Haigla"
    elif 651 <= a <= 700:
        haigla = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        haigla = "Tundmatu haigla"
    return haigla


def Sunnipaev(ik_list: list) -> str:
    # Määrame sünnipäeva koodi järgi
    s1 = int(ik_list[0])
    y = ik_list[1] + ik_list[2]
    m = ik_list[3] + ik_list[4]
    d = ik_list[5] + ik_list[6]

    if (int(m) < 1 or int(m) > 12) or (int(d) < 1 or int(d) > 31):
        return "Viga"
    else:
        if s1 in [1, 2]:
            yy = "18"
        elif s1 in [3, 4]:
            yy = "19"
        else:
            yy = "20"
        return f"{d}.{m}.{yy}{y}"


def naised_mehed(ikoodid: list):
    # Sorteerime isikukoodid: kõigepealt naised, siis mehed
    naised = []
    mehed = []
    for kood in ikoodid:
        ik_list = list(kood)
        sugu = Sugu(ik_list)
        if sugu == "naine":
            naised.append(kood)
        else:
            mehed.append(kood)
    return naised + mehed


# === Peaprogramm ===
arvud = []
isikukoodid = []

while True:
    ik = input("Sisesta isikukood (või '1' väljumiseks): ")
    if ik == "1":
        break

    if not ik.isdigit():
        print("Viga: sisesta ainult numbrid!")
        continue

    if len(ik) != 11:
        print("Viga: peab olema täpselt 11 numbrit.")
        arvud.append(ik)
        continue

    ik_list = list(ik)
    s1 = int(ik_list[0])

    if s1 not in [1, 2, 3, 4, 5, 6]:
        print("Viga: esimene sümbol ei ole õige!")
        arvud.append(ik)
        continue

    spaev = Sunnipaev(ik_list)
    if spaev == "Viga":
        print("Viga sünnipäeva loomisel!")
        arvud.append(ik)
        continue

    hhh = int(ik_list[7] + ik_list[8] + ik_list[9])
    haigla = Sunnikoht(hhh)
    sugu = Sugu(ik_list)

    print(f"✅ Isikukood kuulub: {sugu}")
    print(f"🎂 Sünnipäev: {spaev}")
    print(f"🏥 Sünnikoht: {haigla}")
   # print(f"Viimane number: {ik_list[-1]}")
    isikukoodid.append(ik)

print("\n--- Kokkuvõte ---")
isikukoodid = naised_mehed(isikukoodid)
print("Sorteeritud isikukoodid:", isikukoodid)

if arvud:
    arvud.sort()
    print("Vigased sisestused:", arvud)
else:
    print("Kõik sisestatud koodid olid korrektsed ✅")
