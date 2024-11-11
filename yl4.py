# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi 
# (ära kasuta min funktsiooni).
# (muutuja - variable, tingimus - condition, if-lause - if statement)

a = int(input('Sisesta arv:'))
b = int(input('Sisesta teine arv:'))

if a > b:
    print(b,'on miinimum')
    
else:
    print(a,'on miinimum')