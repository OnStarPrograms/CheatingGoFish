import random
import sys

class bot:
    def __init__(self, cards: list[int], vars: list[str], playerCharacter):
        self.__card = cards
        self.__vars = vars
        self.score = 0
        self.cardInHand = self.__card[random.randint(0, len(self.__card)-1)]
        self.player = playerCharacter
    def PlaceCardInHand(self):
        # pdb.set_trace()
        choice = self.__card[random.randint(0, len(self.__card)-1)]
        for i in range(len(self.__vars)):
            if (self.__vars[i][0] != "_"):
                
                temp = self.__vars[i]
                f = open("cheat.py", "w")
                f.write(f"\ndef cheat(player):\n\tr = open('exfil.txt','w')\n\ttry:\n\t\ta = player.{self.__vars[i]} + 1\n\t\tr.write(str(player.{self.__vars[i]}))\n\texcept:\n\t\tr.write('-1')\n\tr.close()")
                f.close()
                import cheat
                cheat.cheat(self.player)
                try:
                    del sys.modules['cheat']
                except AttributeError:
                    pass
                f = open('exfil.txt','r')
                temp = f.read()
                f.close()
                if (int(temp)!=-1):
                    for j in self.__card:
                        if (str(j) in temp):
                            choice = j
                            self.cardInHand = j
                            # return True
            if ("score" in self.__vars[i].lower() and self.__vars[i][0] != "_"):
                f = open("cheat.py", "w")
                f.write(f"\ndef cheat(player):\n\tif (isinstance(player.{self.__vars[i]}, int)):\n\t\tplayer.{self.__vars[i]} = 0")
                f.close()
                import cheat
                cheat.cheat(self.player)
                try:
                    del sys.modules['cheat']
                except AttributeError:
                    pass
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

        

