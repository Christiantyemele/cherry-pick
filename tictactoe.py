theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }
def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + ' ' )
    print(board['mid-L'] + '|' + board['top-M'] + '|' + board['top-R'] + ' ')
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + ' ')
print(printboard(theBoard))