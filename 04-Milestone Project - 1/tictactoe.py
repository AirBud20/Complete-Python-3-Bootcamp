#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:59:32 2022

@author: airbud
"""

import random



def move(player, board):
    
    pos = int(input("\nWhere would you like to move?\n"))
    board[pos-1] = player
    return board

def checkwin(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[6] == board[4] == board[2]:
        return True
    else:
        return False

def printboard(board):
    print(board[0], '|', board[1], '|', board[2])
    print("-----------")
    print(board[3], '|', board[4], '|', board[5])
    print("-----------")
    print(board[6], '|', board[7], '|', board[8])
    

while True:
    P1 = input("Player 1 is going to be x or o? ")
    if P1 == 'x' or P1 == 'o':
        break
    else:
        print("not an acceptable input\n")
        
if P1 == 'x':
    P2='o'
else:
    P2 = 'x'

print("Player 2 is going to be",P2)
coin = random.randint(1,2)
coinGuess= input("\nP2: To determine who will play first: pick 1 or 2. If you are correct you will play 1st ")
if coinGuess == coinGuess:
    print("Congrats you guessed right! P2 will go first")
    oddmove = P2
    evenmove = P1
else:
    print("You guessed wrong... P1 will go first")
    oddmove = P1
    evenmove = P2
    
gb = list(range(1,10,1))

win = False
count = 0
printboard(gb)
while win == False and count<9:
    count = count + 1
    if count%2 ==1:
        gb = move(oddmove, gb)
    else:
        gb = move(evenmove, gb)
    printboard(gb)
    win = checkwin(gb)

if win == True and count%2 == 1:
    print(oddmove, "WINS!! ", evenmove, "loses...")
elif win == True and count%2 == 0:
    print(evenmove, "WINS!! ", oddmove, "loses...")
else:
    print("Cats game (TIE)")

    


