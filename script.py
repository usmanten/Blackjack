import random
from game_logic import Dealerlogic, Playerlogic, cards

# Start the game
response = input("Welcome. Do you want to play a game of Blackjack? Type 'Y' or 'N': ")

if response.lower() == 'y':
    print("Welcome to Blackjack!")

    # Deal cards
    Dealercard1, Dealercard2 = random.choice(cards), random.choice(cards)
    Dealer_hand = [Dealercard1, Dealercard2]
    Playercard1, Playercard2 = random.choice(cards), random.choice(cards)
    Player_hand = [Playercard1, Playercard2]

    Dealersum = sum(Dealer_hand)
    Playersum = sum(Player_hand)

    print("Dealer cards:", Dealer_hand)
    print("Player cards:", Player_hand)

    # Check for instant win
    standOrHit = ''
    match (Dealersum == 21, Playersum == 21):
        case (True, True):
            print("It's a draw!")
        case (True, False):
            print("You lose!")
        case (False, True):
            print("You win!")
        case (False, False):
            standOrHit = input("Do you want to stand or hit? ")

    while standOrHit.lower() in ['hit', 'h']:
        Player_hand, Playersum, standOrHit = Playerlogic(Player_hand, Playersum)

    if standOrHit.lower() not in ['stand', 's']:
        print("Unexpected Response. Game will assume you want to stand.")
        Dealer_hand, Dealersum = Dealerlogic(Dealer_hand, Dealersum)
    else:
        Dealer_hand, Dealersum = Dealerlogic(Dealer_hand, Dealersum)

    # Final outcome
    match (Dealersum > 21, Playersum > 21):
        case (True, True):
            print("You lose!")
        case (True, False):
            print("You win!")
        case (False, True):
            print("You lose!")
        case (False, False):
            if Dealersum > Playersum:
                print("Dealer wins!")
            elif Playersum > Dealersum:
                print("Player wins!")
            else:
                print("It's a draw!")

elif response.lower() == 'n':
    print("Thank you! Maybe next time!")
else:
    print("Unexpected response. Please try again.")
