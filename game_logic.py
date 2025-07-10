import random

# Initialize global variables
Dealercard1 = 0
Dealercard2 = 0
Playercard1 = 0
Playercard2 = 0
Dealersum = 0
Playersum = 0
standOrHit = ""
Player_hand = []
Dealer_hand = []
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

# Dealer logic
def Dealerlogic(Dealer_hand, Dealersum):

    while Dealersum < 17:
        Dealercard3 = random.choice(cards)
        Dealer_hand.append(Dealercard3)
        Dealersum += Dealercard3

        # Adjust for Aces
        while Dealersum > 21 and 11 in Dealer_hand:
            Dealer_hand[Dealer_hand.index(11)] = 1
            Dealersum = sum(Dealer_hand)

        print(f"Dealer Total and Dealer hand: {Dealersum, Dealer_hand}")

    return Dealer_hand, Dealersum


# Player logic
def Playerlogic(Player_hand, Playersum):

    Playercard3 = random.choice(cards)
    Player_hand.append(Playercard3)
    Playersum += Playercard3

    # Adjust for Aces
    while Playersum > 21 and 11 in Player_hand:
        Player_hand[Player_hand.index(11)] = 1
        Playersum = sum(Player_hand)
    print(f"Player Total and Player hand: {Playersum, Player_hand}")

    if Playersum < 21:
        standOrHit = input("Do you want to stand or hit? ")

    return Player_hand, Playersum, standOrHit
