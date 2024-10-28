# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha,
# kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse,
# kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida,
# kui vanus on 18, siis õnnitleb täisealiseks saamise puhul,
# kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. 

name = input('Enter your name: ')
print('Hello,', name)

location = input('Where do you live?:')

if location == 'Saaremaa' or location == 'saaremaa':
    try:
        age = int(input('How old are you?: '))
        
        if age > 18:
            print('User can drive a car.')

        elif age < 18:
            print('User is too young to drive a car.')

        else:
            print('Congratulations on turning 18!')

    except ValueError:
        print('Please enter a valid number.')
else:
    print('User does not live in Saaremaa.')