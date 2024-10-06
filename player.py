import random

class player:
    def __init__(self, cards: list[int]):
        self.__card = cards
        self.score = 0
        self.cardInHand = cards[random.randint(0, len(cards)-1)]
    def placeCardInHand(self, pastChoices):
        # pdb.set_trace()
        choice = self.__card[random.randint(0, len(self.__card)-1)]
        self.cardInHand = choice
        return choice 
    
    def PlayerResponse(self, card: int):
        for i in range(len(self.__card)):
            if (card == self.__card[i]):
                self.__card.remove(self.__card[i])
                return True
        return False

    def GoFish(self, card: int):
        self.__card.append(card)
        
    def AskPlayer(self) -> int:
        return self.cardInHand

    def GetScore(self):
        return self.score
    
    def PlayerReceived(self):
            self.score+=1
            for i in range(0, len(self.__card)):
                if (self.cardInHand == self.__card[i]):
                    self.__card.remove(self.__card[i])
                    break
            
        
