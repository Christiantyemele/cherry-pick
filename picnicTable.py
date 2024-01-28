def printpinic(itemsDict, leftWith, rightWith):
    print('PINIC ITEMS'.center(leftWith + rightWith, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWith, '.') + str(v).rjust((rightWith)))

pinicItems = {'sandwitches': 4, 'apples': 12, 'cups': 4, 'cookies':8000}
printpinic(pinicItems, 12, 5)
printpinic(pinicItems, 20, 6 )