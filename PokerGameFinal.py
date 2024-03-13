import random


class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit


    def getRank(self):
        return self.rank


    def getSuit(self):
        return self.suit

    def getValue(self):
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        return ranks.index(self.rank)



    def __str__(self):
        return self.rank + self.suit 


class Deck:
    def __init__ (self):
        self.deck = []
        self.buildDeck()

    
    def buildDeck(self):
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        for s in suits:
            for r in ranks:
                self.deck.append(Card(r,s))
                
    def deal(self):
        return self.deck.pop(random.randint(0,len(self.deck)-1))

    
    def getCardsRemaining(self):
        return len(self.deck)

    
    def __str__(self):
        answer = ""
        for card in self.deck:
            answer += str(card) + "\n"
        return answer

class Poker:
    def __init__(self):
        self.pokerDeck = Deck()
        self.playerOneHand = []
        self.playerTwoHand = []


    def setPlayerHandRandom(self):
        for i in range(5):
            self.playerOneHand.append(self.pokerDeck.deal())
            self.playerTwoHand.append(self.pokerDeck.deal())


    def setPlayerHandManual(self, p1Hand,p2Hand):
        for i in range(0,len(p1Hand),3):
            self.playerOneHand.append(Card(p1Hand[i],p1Hand[i+1]))

        for i in range(0,len(p2Hand),3):
            self.playerTwoHand.append(Card(p2Hand[i],p2Hand[i+1]))

    def getPlayerOneHand(self):
        return self.playerOneHand

    def getPlayerTwoHand(self):
        return self.playerTwoHand

       
            
    def isPair(self,pHand):
        count = 0
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        for r in ranks:
            count = 0
            for i in range(len(pHand)):
                if(pHand[i].getRank() == r):
                    count += 1
                    
            if count == 2:
                return True
        return False

    def isPairHighCard(self,pHand):
        count = 0
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        for r in ranks:
            count = 0
            for i in range(len(pHand)):
                if(pHand[i].getRank() == r):
                    count += 1
                    
            if count == 2:
                for a in range(len(pHand)):
                    if(pHand[a].getRank() == r):
                        return pHand[a].getValue()
        return 0


    def isTwoPair(self,pHand):
        count = 0
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        pHandSub = []
        for i in range(len(pHand)):
             pHandSub.append(pHand[i])                      

        for r in ranks:
            count = 0
            for i in range(len(pHandSub)):
                if(pHandSub[i].getRank() == r):
                    count += 1
                    
            if count == 2:
                for a in range(len(pHandSub)-1, -1, -1):
                    if(pHandSub[a].getRank() == r):
                        pHandSub.pop(a)
                        
                for r in ranks:
                    count = 0
                    for i in range(len(pHandSub)):
                        if(pHandSub[i].getRank() == r):
                            count += 1
                            
                    if count == 2:
                        for a in range(len(pHandSub)-1, -1, -1):
                            if(pHandSub[a].getRank() == r):
                                pHandSub.pop(a)
                        return True
        return False

    def isThreeKind(self,pHand):
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        count = 0
        for r in ranks:
            for i in range(len(pHand)):
                if(pHand[i].getRank() == r):
                    count += 1
                    
            if count == 3:
                return True
            count = 0
        return False


    def isFullHouse(self,pHand):
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        if self.isPair(pHand) == True and self.isThreeKind(pHand) == True:
            return True
        return False


    def isFourKind(self,pHand):
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        count = 0
        for r in ranks:
            for i in range(len(pHand)):
                if(pHand[i].getRank() == r):
                    count += 1
                    
            if count == 4:
                return True
            count = 0
        return False


    def isFlush(self,pHand):
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        count = 0
        for s in suits:
            for i in range(len(pHand)):
                if(pHand[i].getSuit() == s):
                    count += 1
                    
            if count == 5:
                return True
            count = 0
        return False

    def isStraight(self,pHand):
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        highNumber = 0

        for i in range(len(self.playerOneHand)):
            if(pHand[i].getValue() > highNumber):
                highNumber = pHand[i].getValue()

        for i in range(len(self.playerOneHand)):
            if(pHand[i].getValue() == highNumber-1):
                for i in range(len(self.playerOneHand)):
                    if(pHand[i].getValue() == highNumber-2):
                        for i in range(len(self.playerOneHand)):
                            if(pHand[i].getValue() == highNumber-3):
                                for i in range(len(self.playerOneHand)):
                                    if(pHand[i].getValue() == highNumber-4):
                                        return True

        return False


    def isStraightFlush(self,pHand):
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        if self.isStraight(pHand) == True and self.isFlush(pHand) == True:
            return True
        return False



    def isHighCard(self,p1Hand,p2Hand):
        ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        suits = ["S","D","H","C"]
        for i in range(5):
            highNumber1 = 0
            highNumber2 = 0
            count1 = 0
            count2 = 0

            for i in range(0,len(self.playerOneHand)):
                if(p1Hand[i].getValue() > highNumber1):
                    highNumber1 = p1Hand[i].getValue()
                    count1 = i
            else:
                p1Hand.pop(count1)
                

            for i in range(0,len(self.playerTwoHand)):
                if(p2Hand[i].getValue() > highNumber2):
                    highNumber2 = p2Hand[i].getValue()
                    count2 = i
            else:
                p2Hand.pop(count2)
                

            if(highNumber1 > highNumber2):
                return "Player A Wins by High Card"
            elif(highNumber2 > highNumber1):
                return "Player B Wins by High Card"

        return "Tie by High Card"

    def getHandLevel(self,pHand):
        pHandLevel = 0
        if(self.isStraightFlush(pHand) == True):
            pHandLevel = 9
        elif(self.isFourKind(pHand) == True):
            pHandLevel = 8
        elif(self.isFullHouse(pHand) == True):
            pHandLevel = 7
        elif(self.isFlush(pHand) == True):
            pHandLevel = 6
        elif(self.isStraight(pHand) == True):
            pHandLevel = 5
        elif(self.isThreeKind(pHand) == True):
            pHandLevel = 4
        elif(self.isTwoPair(pHand) == True):
            pHandLevel = 3
        elif(self.isPair(pHand) == True):
            pHandLevel = 2
        else:
            pHandLevel = 1

        return pHandLevel
            
    def pokerGameRunner(self):
        p1HandLevel = self.getHandLevel(self.getPlayerOneHand())
        p2HandLevel = self.getHandLevel(self.getPlayerTwoHand())
        print("A handLevel = " + str(p1HandLevel))
        print("B handLevel = " + str(p2HandLevel))
        if(p1HandLevel > p2HandLevel):
            print("Player A Wins")
        elif(p1HandLevel < p2HandLevel):
            print("Player B Wins")
        elif(p1HandLevel == 2 and p2HandLevel == 2):          
            if((self.isPairHighCard(self.getPlayerOneHand())) > (self.isPairHighCard(self.getPlayerTwoHand()))):
                print("Tied Hand Level - Player A Wins by Higher Pair Value")
            else:
                print("Tied Hand Level - Player B Wins by Higher Pair Value")

        else:
            print("Tied Hand Level - " + str(self.isHighCard(self.getPlayerOneHand(),self.getPlayerTwoHand())))


    def __str__ (self):
        p1List = []
        p2List = []
        for i in range(len(self.playerOneHand)):
              p1List.append(self.playerOneHand[i].getRank() + self.playerOneHand[i].getSuit())                      

        for i in range(len(self.playerTwoHand)):
            p2List.append(self.playerTwoHand[i].getRank() + self.playerTwoHand[i].getSuit())
        
        return "\nPlayer 1's hand: \n" + str(p1List) + "\nPlayer 2's hand: \n" + str(p2List)
