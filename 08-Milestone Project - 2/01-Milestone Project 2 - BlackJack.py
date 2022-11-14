# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:39:42 2022

@author: Aaron
"""

class Hand:
    def __init__ (self, cards):
        self.cards = cards
    def hitHand (self, newCard):
        self.cards = self.cards.append(newCard)
    def getHandValue(self):
        ace = False
        count = 1
        total = [0, 0]
        soft = False
        for card in self.cards:
            if card.getcardName() = 'A' and ace = 0
                total[1] = total[0] + 1
                total[0] = total[0] + 11
                ace = 1
            elif card.getcardName() = 'A' and ace > 0
                total[0] = total[0] + 1
                total[1] = total[1] + 1
                ace = ace+1
            elif 
    
class Card:
    def __init__ (self, num):
        if num in list(range(2,11,1)):
            self.cardvValue = num
            self.cardName = str(num)
        elif num in list(range(11,14,1)):
            self.cardvalue = 10
            if num == 11:
                self.cardName = 'J'
            elif num == 12:
                self.cardName = 'Q'
            elif num == 13:
                self.cardName = 'K'
        else:
            self.cardvalue = 1
            self.cardName = 'A'
     
    def getcardValue(self):
        return self.cardvalue
    
    def getcardName(self):
        return self.cardName
        