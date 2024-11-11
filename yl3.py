# Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. Arvuta n + nn + nnn väärtus ja väljasta see.
# (Näiteks kui kasutaja sisestab 2, siis on vaja väljastada tulemus 2 + 22 + 222 = 246).
# Ära kasuta korrutamistehet. Ülesanne on lahendatav ainult liitmise operaatorit kasuades.


n = int(input("Sisesta täisarv vahemikus 1-9: "))

nn = int(str(n) * 2)
nnn = int(str(n) * 3)

summa = n + nn + nnn

print(f"Tulemus: {n} + {nn} + {nnn} = {summa}")