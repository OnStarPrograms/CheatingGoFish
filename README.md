# CheatingGoFish

### __OverView__

You recently joined a programming competition to build a robot capable of playing GoFish  
__Except Something is Horribly Wrong__ _(Hint*: Look at how many times you are losing)_

Try Figuring the problem out!  
> __Specs__
```diff
- write the class in player.py
- the main file is gofish.py
- You can solve this all in player.py
```
---
> __Required Functions (Spelled this way)__
```diff
+ "__init__"
which accepts an array of your initial given hand (list[int])
- Must initialize a score to zero

+ "placeCardInHand"
Accepts an array of the enemies past card choices (list[int]) 
- you take a card from your hand to be your card choice
example:
    - choice = self.Hand[random.randint(0, len(self.card)-1)]

+ "PlayerResponse"
Must accept a card (int)
compare the card to your own hand 
-    - if there is a match you must remove the matched card and return True
-    - otherwise return False

+ "GoFish"
Must accept a card (int) and append it to your hand

+ "AskPlayer()"
Must return your chosen card you wish to ask for (from placeCardInHand)

+ "GetScore()"
Must return your score

+ "Player Recieved":
    - Must Increase score by 1
    - Must fully delete your chosen card from you hand 
-       (this is why you choose a card to play and store in a var)
```

_Ask Aiden for either the answer code or sample code of the player class_
