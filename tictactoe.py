theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + ' ')
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + ' ')
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + ' ')


Turn = 'X'

for i in range(9):
    printboard(theBoard)
    print('Turn for ' + Turn + ' to move')
    move = input()
    theBoard[move] = Turn
    if Turn == 'X':
        Turn = 'O'

    else:
        Turn = 'X'

print(printboard(theBoard))
