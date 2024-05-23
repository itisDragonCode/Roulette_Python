redNumbers=[32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
blackNumbers= [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]

def isWin(bet, num):
    if bet == 'black':
        if num in blackNumbers:
            return True
        else:
            return False
    if bet == 'red':
        if num in redNumbers:
            return True
        else:
            return False
    if bet == 'big':
        if num > 18 and num <37:
            return True
        else:
            return False
    if bet == 'small':
        if num > 0 and num < 19:
            return True
        else:
            return False
    if bet == 'odd':
        if num % 2 == 1:
            return True
        else:
            return False
    if bet == 'even':
        if num % 2 == 0 and num != 0:
            return True
        else:
            return False
   
