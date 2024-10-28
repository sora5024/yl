# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha,
# kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse,
# kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida,
# kui vanus on 18, siis õnnitleb täisealiseks saamise puhul,
# kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. 

name = input('Sisesta oma nimi: ')
print('Tere,',name)

location = input('Kus sa elad?:')

if location == 'Saaremaa' or 'saaremaa':
    try:
        age = int(input('Kui vana sa oled?: '))
        
        if age > 18:
            print('Kasutaja võib autot juhtida.')

        elif age < 18:
            print('Kasutaja on liiga noor, et autot juhtida.')

        else:
            print('Õnnitleme teid täisealiseks saamise puhul!')

    except ValueError:
        print('Palun sisestage kehtiv number.')
else:
    print('Kasutaja ei ela Saaremaal.')