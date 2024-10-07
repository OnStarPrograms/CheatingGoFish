from imports.bot import bot
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
    mbot = bot(deal2, dir(mplayer), mplayer)
    prevMoves = [0,0,0]
    point = 0
    while (True):
        if len(deck1) == 0 or len(deal1) == 0 or len(deck2) == 0 or mbot.GetScore() >= 5:
            print("Cheater Win")
            break
        elif mplayer.GetScore() >=5:
            print("Player Wins")
            break
        
        mplayer.PlaceCardInHand(prevMoves)
        mbot.PlaceCardInHand()
        player2Choice = mbot.AskPlayer()
        _match = mplayer.PlayerResponse(player2Choice)
        if (_match):
            mbot.PlayerReceived()
        else:
            choicer = random.randint(0, len(deck2)-1)
            mbot.GoFish(deck2[choicer])
            deck2.remove(deck2[choicer])
            
        player1Choice = mplayer.AskPlayer()
        _match = mbot.PlayerResponse(player1Choice)
        if (_match):
            mplayer.PlayerReceived()
        else:
            choicer = random.randint(0, len(deck1)-1)
            mplayer.GoFish(deck1[choicer])
            deck1.remove(deck1[choicer])

       

        prevMoves[point] = player2Choice
        point = (point+1)%3


main()
