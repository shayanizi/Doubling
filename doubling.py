#!/usr/bin/python
class Doubling:
    def __init__(self,balance):
        self.balance=balance
    def cal(self):
        self.balance = self.balance / 2
        while True:
            n = {1,2,3,4,5,6,7,8,9}
            for i in n:
                if self.balance>0 :
                    self.balance=self.balance/2
                    self.balance2=(self.balance)
                    print ("Your volome is >> ",self.balance2)
                else:
                    print ("Error 404")
            break
d=Doubling(float(input("Insert your Balance >> ")))
d2=Doubling.cal(d)
print("You have Nine levels\n")
print("Start with the latest issue at every level you lose your business\t ")
print("Otherwise you win the trade and go to the next level\n\t")