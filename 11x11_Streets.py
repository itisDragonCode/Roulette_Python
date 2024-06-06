import rouletteFunctions as rf
import random
import pandas as pd

gamesNumber = 10000


money = 11 + pow(11,2) + pow(11,3) + pow(11,4)
bet = 11
gameOver = False
listMoney = []

for i in range(gamesNumber):
    result = random.randrange(0,37)
    avoid_street= 4

    if money - bet < 0:
        gameOver = True
        print('Game over')
        break

    money-=bet

    if rf.isStreetWin(avoid_street, result):
        money += bet
        money+= (bet/11)* 12 - (bet / 11)* 11
        if bet!=11:
            bet/=11
    else:
        bet *= 11
    listMoney.append(money)


if gameOver==True:
    print('Not enough money to continue 11*11 Streets strategy')
else:
    print('Your profit is ', money - (11 + pow(11,2) + pow(11,3) + pow(11,4)))

  
# dict = {'MoneyStreets':listMoney}
# df = pd.DataFrame(dict)

# df.to_csv('11x11Streets.csv')  