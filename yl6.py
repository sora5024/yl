# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi
# (ära kasuta max funktsiooni). (loogikatehted - logic operators)
n1 = int(input('Sisesta arv: '))
n2 = int(input('Sisesta arv: '))
n3 = int(input('Sisesta arv: '))

if n1 > n2 and n1 > n3:
    print(n1, 'on maksimum')

elif n2 > n3:
    print(n2, 'on maksimum')

else:
    print(n3, 'on maksimum')