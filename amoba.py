import random


def kiir(lst=[' '] * 9):
    for i in range(1, 10, 3):
        print('\t\t\t\t', lst[-(i + 2)], '  |  ', lst[-(i + 1)], '  |  ', lst[-i])
        if i != 7:
            print('\t\t\t\t-------------------')


def kezd():
    players = []
    players.append(str(input('Kérem az első játékos nevét:\t')))
    players.append(str(input('Kérem a második játékos nevét:\t')))
    random.shuffle(players)

    print("\nA véletlenszerűen kiválasztott kezdő játékos \033[94m" + players[0] + "\033[0;0m lesz,",
          "szimbóluma: az \033[94m'X'\033[0;0m")  # Színezés ANSI escape sequence-szel
    print("\033[94m" + players[1] + "\033[0;0m lesz a második, szimbóluma: az \033[94m'O'\033[0;0m")

    playerssimb = list(zip(players, ['X', 'O']))

    print("\nA numerikus billenytűzet fogja reprezentálni a 3x3-as játékasztalt.")


    input('\033[95mNyomj egy gombot a kezdéshez!\033[0;0m')
    kiir()
    return playerssimb


def gyozelem(lista):
    if [lista[0], lista[4], lista[8]] in (['X', 'X', 'X'], ['O', 'O', 'O']):
        return True

    elif [lista[2], lista[4], lista[6]] in (['X', 'X', 'X'], ['O', 'O', 'O']):
        return True

    else:
        for i in range(3):
            j = i * 3

            if [lista[i], lista[i + 3], lista[i + 6]] in (['X', 'X', 'X'], ['O', 'O', 'O']):
                return True

            elif lista[j:j + 3] in (['X', 'X', 'X'], ['O', 'O', 'O']):
                return True

    return False


def game():
    tabla = [' '] * 9
    gamepref = kezd()
    j = 0

    while gyozelem(tabla) is not True and j < 9:

        if j % 2 == 0:
            aktplayer = gamepref[0][0]

            while True:
                t = int(input(aktplayer + '(' + gamepref[0][1] + ') lépése:     '))
                if t not in range(1,10):
                    print('\t\t1-9 között légy szíves!')

                elif tabla[t - 1] == ' ':
                    tabla[t - 1] = 'X'
                    break
                else:
                    kiir(tabla)
                    print('A {} hely már foglalt', {t})


        else:
            aktplayer = gamepref[1][0]

            while True:
                t = int(input(aktplayer + '(' + gamepref[1][1] + ') lépése:     '))
                if t not in range(1,10):
                    print('\t\t1-9 között légy szíves!')

                elif tabla[t - 1] == ' ':
                    tabla[t - 1] = 'O'
                    break
                else:
                    kiir(tabla)
                    print('A {} hely már foglalt', {t})

        j += 1
        kiir(tabla)

    if j == 9 and gyozelem(tabla) is False:
        print('\n\t\t\t\033[95mDöntetlen\033[0;0m')

    else:
        print('\n\t\t\t\033[92m', aktplayer, 'nyert!\033[0;0m')

    uj = str(input('Új játék (Y/N):\t'))

    if uj in ('y', 'Y', 'i', 'I', 'z', 'Z'):
        game()

    else:
        print('Köszönöm a játékot!')


if __name__ == '__main__':
    game()
