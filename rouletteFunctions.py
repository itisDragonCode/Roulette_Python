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

def isStreetWin(avoid, num):
    if avoid == 1:
        if num == 1 or num == 2 or num == 3 or num == 0:
            return False
        else:
            return True
    elif avoid == 2:
        if num == 4 or num == 5 or num == 6 or num == 0:
            return False
        else:
            return True
    elif avoid == 3:
        if num == 7 or num == 8 or num == 9 or num == 0:
            return False
        else:
            return True
    elif avoid == 4:
        if num == 10 or num == 11 or num == 12 or num == 0:
            return False
        else:
            return True
    elif avoid == 5:
        if num == 13 or num == 14 or num == 15 or num == 0:
            return False
        else:
            return True
    elif avoid == 6:
        if num == 16 or num == 17 or num == 18 or num == 0:
            return False
        else:
            return True
    elif avoid == 7:
        if num == 19 or num == 20 or num == 21 or num == 0:
            return False
        else:
            return True
    elif avoid == 8:
        if num == 22 or num == 23 or num == 24 or num == 0:
            return False
        else:
            return True
    elif avoid == 9:
        if num == 25 or num == 26 or num == 27 or num == 0:
            return False
        else:
            return True
    elif avoid == 10:
        if num == 28 or num == 29 or num == 30 or num == 0:
            return False
        else:
            return True
    elif avoid == 11:
        if num == 31 or num == 32 or num == 33 or num == 0:
            return False
        else:
            return True
    elif avoid == 12:
        if num == 34 or num == 35 or num == 36 or num == 0:
            return False
        else:
            return True
   
