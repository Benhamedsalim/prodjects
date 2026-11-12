theBord = {
    '7':' ', '8': ' ', '9': ' ',
    '4':' ', '5': ' ', '6': ' ',
    '1':' ', '2': ' ', '3': ' '
}
def printBord(theBord):
    print(theBord['7'], '|', theBord['8'], '|', theBord['9'])
    print('--+---+--')
    print(theBord['4'], '|', theBord['5'], '|', theBord['6'])
    print('--+---+--')
    print(theBord['1'], '|', theBord['2'], '|', theBord['3'])
#printBord(theBord)
def reset_board():
    for k in theBord:
        theBord[k] = ' '
def game():
    turn = 'x'
    count = 0
    for i in range(10):
        printBord(theBord)
        move = input(f"It's your turn,' {turn} 'Move to whitch place?: ")
        if move not in theBord:
            print('ERROR, Sorry try again .....!!')
            continue

        if theBord[move] == ' ':
            theBord[move] = turn
            count += 1
        else:
            print("The place is already filled.\nMove to another place?")
            continue

        if count >= 5:
            if theBord['7'] == theBord['8'] == theBord['9'] != ' ':
                printBord(theBord)
                print("\nGame Over\n")
                print(f"*********\n{turn} is the winner\n*********")
                break
            elif theBord['4'] == theBord['5'] == theBord['6'] != ' ':
                printBord(theBord)
                print("\nGame Over\n")
                print(f"*********\n{turn} is the winner\n*********")
                break
            elif theBord['1'] == theBord['2'] == theBord['3'] != ' ':
                printBord(theBord)
                print("\nGame Over\n")
                print(f"*********\n{turn} is the winner\n*********")
                break
            elif theBord['1'] == theBord['4'] == theBord['7'] != ' ':
                printBord(theBord)
                print("\nGame Over\n")
                print(f"*********\n{turn} is the winner\n*********")
                break
            elif theBord['5'] == theBord['8'] == theBord['2'] != ' ':
                printBord(theBord)
                print("\nGame Over\n")
                print(f"*********\n{turn} is the winner\n*********")
                break
            elif theBord['3'] == theBord['6'] == theBord['9'] != ' ':
                printBord(theBord)
                print("\nGame Over\n")
                print(f"*********\n{turn} is the winner\n*********")
                break
            elif theBord['7'] == theBord['5'] == theBord['3'] != ' ':
                printBord(theBord)
                print("\nGame Over\n")
                print(f"*********\n{turn} is the winner\n*********")
                break
            elif theBord['1'] == theBord['5'] == theBord['9'] != ' ':
                printBord(theBord)
                print("\nGame Over\n")
                print(f"*********\n{turn} is the winner\n*********")
                break
        if count == 9:
            print("\nGame Over\n")
            print('It\'s a tie!!')
            break
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    if input('Dp ypu want play again? (y/n): ').lower() == 'y':
        print('Welcom')

        reset_board()
        game()

    else:
        exit()



if __name__ == '__main__':
    game()

