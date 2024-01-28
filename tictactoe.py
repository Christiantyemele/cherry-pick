theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }
def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + ' ' )
    print('-+-+-')
    print(board['mid-L'] + '|' + board['top-M'] + '|' + board['top-R'] + ' ')
    print('-+-+-')
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + ' ')

Turn = 'X'
for i in range(9):
    print()
    (printboard(theBoard))
    move = input('type in your move ' + Turn)
    theBoard[move] = Turn
    if Turn == 'X':
        Turn = 'O'
    else:
        Turn = 'X'
(printboard(theBoard))
