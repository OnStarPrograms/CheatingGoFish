from cheater import cheater
from player import player
import random

def main():
    deck1 = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    deck2 = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    deal1 = []
    deal2 = []
    for i in range(6):
        choicer = random.randint(0, len(deck1)-1)
        deal1.append(deck1[choicer])
        deck1.remove(deck1[choicer])
        choicer = random.randint(0, len(deck2)-1)
        deal2.append(deck2[choicer])
        deck2.remove(deck2[choicer])

        
    mplayer = player(deal1)
    mcheater = cheater(deal2, dir(mplayer), mplayer)
    prevMoves = [0,0,0]
    point = 0
    while (True):
        mplayer.placeCardInHand(prevMoves)
        mcheater.placeCardInHand()
        
        if mcheater.GetScore() >= 5:
            print("Cheater Win")
            break
        elif mplayer.GetScore() >=5:
            print("Player Wins")
            break
        player2Choice = mcheater.AskPlayer()
        _match = mplayer.PlayerResponse(player2Choice)
        if (_match):
            mcheater.PlayerRecieved()
        else:
            choicer = random.randint(0, len(deck2)-1)
            mcheater.GoFish(deck2[choicer])
            deck2.remove(deck2[choicer])
            
        player1Choice = mplayer.AskPlayer()
        _match = mcheater.PlayerResponse(player1Choice)
        if (_match):
            mplayer.PlayerRecieved()
        else:
            choicer = random.randint(0, len(deck1)-1)
            mplayer.GoFish(deck1[choicer])
            deck1.remove(deck1[choicer])

       

        prevMoves[point] = player2Choice
        point = (point+1)%3


main()
