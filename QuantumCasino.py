#!/usr/bin/env python
# coding: utf-8

# In[1]:



import numpy as np
from qiskit import QuantumCircuit, execute, BasicAer, IBMQ, QuantumRegister, ClassicalRegister
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()

cash = 1000


# In[ ]:


qr = QuantumRegister(5)
cr1 = ClassicalRegister(1)
cr2 = ClassicalRegister(1)
cr3 = ClassicalRegister(1)
cr4 = ClassicalRegister(1)
cr5 = ClassicalRegister(1)
Roulette = QuantumCircuit(qr,cr1,cr2,cr3,cr4,cr5)


Roulette.h(0)
Roulette.h(1)
Roulette.h(2)
Roulette.h(3)
Roulette.h(4)
Roulette.measure(0,cr1)
Roulette.measure(1,cr2)
Roulette.measure(2,cr3)
Roulette.measure(3,cr4)
Roulette.measure(4,cr5)

Roulette.draw()


# In[ ]:



def quantumRoll():
    print("Rolling the quantum wheel... this might take a while.")
    provider = IBMQ.get_provider(hub='ibm-q')
    provider.backends()
    # get the least-busy backend at IBM and run the quantum circuit there
    from qiskit.providers.ibmq import least_busy
    backend = least_busy(provider.backends(filters=lambda b: b.configuration().n_qubits >= 3 and
                                  not  b.configuration().simulator and b.status().operational==True))
    counts = execute(Roulette, backend, shots=1).result().get_counts()
    newcounts = {v: k for k, v in counts.items()}
    Result = (int(newcounts.get(1).replace(" ",""),2))
    return Result


# In[ ]:


def Game():
    return input()
def newGame():
    print("Starting new game...")
    print("Current cash: ", cash)
    print("Which game would you like to play?")
    print("Choose: luckynumber, odd, even, 1/3, 2/3, 3/3.")
    global game
    game = Game()
    startGame()


# In[ ]:


print("Welcome to the Quantum Casino! Our game is Roulette, and we will let a Quantum Computer give us a True Random number from 0 - 31")
print("Your starting cash is $1,000. You can bet a lucky number, bet odd,even, first third, second third, or last third.")
print("Choose: luckynumber, odd, even, 1/3, 2/3, 3/3.")
print("***Note*** there are only 32 possible numbers, last third is disadvantage so payout is 3.1x instead of 3x")
game = Game()

def startGame():
    global cash
    if(game == "luckynumber"):
        print("Enter your lucky roulette number from 0 to 31. Payout is 32x")
        luckynum = int(input())
        print("How much will you bet?")
        bet = int(input())
        if(bet > cash):
            print("Sorry, you cannot bet more than you own! Restart and try again")
            sys.exit()
        if(bet < 0):
            print("You can not do negative bets! BEGONE")
            sys.exit()
        qnum = quantumRoll()
        if(luckynum == qnum):
            cash = cash + (bet * 31) - bet
            print("Congratulations! You won Quantum Roulette Lucky Number! ", qnum)
            print("You won: ", (bet*31), " Total cash: ", cash)
        else:
            print("Sorry, you lost! The Roulette picked: ", qnum)
            cash = cash - bet
            if(cash <= 0):
                print("Balance is 0/Negative, EXIT THE CASINO IMMEDIATELY.")
                sys.exit()
        print("Play another game? y/n")
        yn = input()
        if(yn == "y"):
            newGame()
        else:
            sys.exit()
    
    if(game == "odd" ):
        print("Betting Odd! Payout is 2x")
        print("How much will you bet?")
        bet = int(input())
        if(bet > cash):
            print("Sorry, you cannot bet more than you own! Restart and try again")
            sys.exit()
        if(bet < 0):
            print("You can not do negative bets! BEGONE")
            sys.exit()
        qnum = quantumRoll()
        if(qnum % 2 == 1):
            print("Congratulations! You won odd! Number: ", qnum)
            cash = cash + (bet * 2) - bet
            print("You won: ", (bet*2 - bet), " Total cash: ", cash)
        else:
            print("Sorry, you lost! The Roulette picked: ", qnum)
            cash = cash - bet
            if(cash <= 0):
                print("Balance is 0/Negative, EXIT THE CASINO IMMEDIATELY.")
                sys.exit()
        print("Play another game? y/n")
        yn = input()
        if(yn == "y"):
            newGame()
        else:
            sys.exit()
    if(game == "even" ):
        print("Betting Even! Payout is 2x")
        print("How much will you bet?")
        bet = int(input())
        if(bet > cash):
            print("Sorry, you cannot bet more than you own! Restart and try again")
            sys.exit()
        if(bet < 0):
            print("You can not do negative bets! BEGONE")
            sys.exit()
        qnum = quantumRoll()
        if(qnum % 2 == 0):
            print("Congratulations! You won even! Number: ", qnum)
            cash = cash + (bet * 2) - bet
            print("You won: ", (bet*2 - bet), " Total cash: ", cash)
        else:
            print("Sorry, you lost! The Roulette picked: ", qnum)
            cash = cash - bet
            if(cash <= 0):
                print("Balance is 0/Negative, EXIT THE CASINO IMMEDIATELY.")
                sys.exit()
        print("Play another game? y/n")
        yn = input()
        if(yn == "y"):
            newGame()
        else:
            sys.exit()
    if(game == "1/3"):
        print("Betting first third! Payout is 3x")
        print("How much will you bet?")
        bet = int(input())
        if(bet > cash):
            print("Sorry, you cannot bet more than you own! Restart and try again")
            sys.exit()
        if(bet < 0):
            print("You can not do negative bets! BEGONE")
            sys.exit()
        qnum = quantumRoll()
        if(qnum <= 10):
            print("Congratulations! You won first third! Number: ", qnum)
            cash = cash + (bet * 3) - bet
            print("You won: ", (bet*3 - bet), " Total cash: ", cash)
        else:
            print("Sorry, you lost! The Roulette picked: ", qnum)
            cash = cash - bet
            if(cash <= 0):
                print("Balance is 0/Negative, EXIT THE CASINO IMMEDIATELY.")
                sys.exit()
        print("Play another game? y/n")
        yn = input()
        if(yn == "y"):
            newGame()
        else:
            sys.exit()
    if(game == "2/3"):
        print("Betting second third! Payout is 3x")
        print("How much will you bet?")
        bet = int(input())
        if(bet > cash):
            print("Sorry, you cannot bet more than you own! Restart and try again")
            sys.exit()
        if(bet < 0):
            print("You can not do negative bets! BEGONE")
            sys.exit()
        qnum = quantumRoll()
        if(qnum > 10 & qnum <= 21):
            print("Congratulations! You won second third! Number: ", qnum)
            cash = cash + (bet * 3) - bet
            print("You won: ", (bet*3 - bet), " Total cash: ", cash)
        else:
            print("Sorry, you lost! The Roulette picked: ", qnum)
            cash = cash - bet
            if(cash <= 0):
                print("Balance is 0/Negative, EXIT THE CASINO IMMEDIATELY.")
                sys.exit()
        print("Play another game? y/n")
        yn = input()
        if(yn == "y"):
            newGame()
        else:
            sys.exit()
    if(game == "3/3"):
        print("Betting last third! *Disadvantage* Payout is 3.1x")
        print("How much will you bet?")
        bet = int(input())
        if(bet > cash):
            print("Sorry, you cannot bet more than you own! Restart and try again")
            sys.exit()
        if(bet < 0):
            print("You can not do negative bets! BEGONE")
            sys.exit()
        qnum = quantumRoll()
        if(qnum > 21):
            print("Congratulations! You won last third! Number: ", qnum)
            cash = cash + (bet * 3.1) - bet
            print("You won: ", (bet*3.1 - bet), " Total cash: ", cash)
        else:
            print("Sorry, you lost! The Roulette picked: ", qnum)
            cash = cash - bet
            if(cash <= 0):
                print("Balance is 0/Negative, EXIT THE CASINO IMMEDIATELY.")
                sys.exit()
        print("Play another game? y/n")
        yn = input()
        if(yn == "y"):
            newGame()
        else:
            sys.exit()
    else: 
        exit()

startGame()


# In[ ]:




