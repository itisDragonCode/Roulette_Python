import rouletteFunctions as rf
import random
import pandas as pd


first = 1
second = 2

fibonacci= [1,2]

for i in range(100):
    third = first + second
    fibonacci.append(third)
    first=second
    second= third


gamesNumber = 100000


money = 10000
fibIndex = 0
gameOver = False
listMoney = []

bettings = ['black','red','big','small','even','odd']

for i in range(gamesNumber):
    result = random.randrange(0,37)
    betting_index= 0
    userBet = bettings[betting_index]

    if money - fibonacci[fibIndex] < 0:
        gameOver = True
        print('Game over')
        break

    money-=fibonacci[fibIndex]

    if rf.isWin(userBet, result):
        money+= fibonacci[fibIndex]*2
        if fibIndex > 1:
            fibIndex -=2
        else:
            fibIndex = 0
    else:
        fibIndex+=1

    listMoney.append(money)

if gameOver==True:
    print('Not enough money to continue Fibonacci strategy')
else:
    print('Your profit is ', money - 10000)

# dict = {'MoneyFibonacci':listMoney}
# df = pd.DataFrame(dict)

# df.to_csv('Fibonacci.csv')  