import random

class player:
    def __init__(self, cards: list[int]):
        self.card = cards
        self.score = 0
        self.cardInHand = cards[random.randint(0, len(cards)-1)]
    def placeCardInHand(self, pastChoices):
        # pdb.set_trace()
        choice = self.card[random.randint(0, len(self.card)-1)]
        self.cardInHand = choice
        return choice 
    
    def PlayerResponse(self, card: int):
        for i in range(len(self.card)):
            if (card == self.card[i]):
                self.card.remove(self.card[i])
                return True
        return False

    def GoFish(self, card: int):
        self.card.append(card)
        
    def AskPlayer(self) -> int:
        return self.cardInHand

    def GetScore(self):
        return self.score
    
    def PlayerReceived(self):
            self.score+=1
            for i in range(0, len(self.card)):
                if (self.cardInHand == self.card[i]):
                    self.card.remove(self.card[i])
                    break
            
        
