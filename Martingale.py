import rouletteFunctions as rf
import random
import pandas as pd

gamesNumber = 100000


money = 10000
bet = 1
gameOver = False
listMoney = []

bettings = ['black','red','big','small','even','odd']

for i in range(gamesNumber):
    result = random.randrange(0,37)
    betting_index= 2
    userBet = bettings[betting_index]

    if money - bet < 0:
        gameOver = True
        print('Game over')
        break

    money-=bet

    if rf.isWin(userBet, result):
        money+= bet*2
        bet=1
    else:
        bet= bet*2

    listMoney.append(money)


if gameOver==True:
    print('Not enough money to continue Martingale strategy')
else:
    print('Your profit is ', money - 10000)

  
# dict = {'MoneyMartingale':listMoney}
# df = pd.DataFrame(dict)

# df.to_csv('Martingale.csv')  





    