'''
Higher or lower
* 8 cards randomly choose
Player has to choose- randomly guess- that the next card will be higher or lower than the previous card
If player guessed correctly- 20 Points
If guessed incorrectly- 15 Points
Same value as the previous card- then also incorrect

* deck of 52 cards- a list of dict
*the Jack of Clubs would be represented as the following dictionary:
{'rank': 'Jack', 'suit': 'Clubs', 'value': 11}

'''
import random

Suit_Tuple = ('Spades','Hearts','Clubs','Diamonds')
Rank_Tuple = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

NCards = 8

#Pass in a deck and this function returns a random card from the deck
def getCard(deck_list):
    this_card = deck_list.pop()
    return this_card

def shuffle(deck_list):
    deck_list_out = deck_list.copy()
    random.shuffle(deck_list_out)
    return deck_list_out

# Main code
starting_deck_list = []
# enumerate function is used to iterate over a sequence (such as a list, tuple, or string) and
# keep track of the index of the current item

# *the Jack of Clubs would be represented as the following dictionary:
# {'rank': 'Jack', 'suit': 'Clubs', 'value': 11}
for suit in Suit_Tuple:
    for this_value, rank in enumerate(Rank_Tuple):
        card_dict = {'rank':rank, 'suit':suit, 'value':this_value + 1}
        starting_deck_list.append(card_dict)

score = 50
game_deck_list = shuffle(starting_deck_list)
print(game_deck_list)

current_card_deck = getCard(game_deck_list)
current_card_rank = current_card_deck['rank']
current_card_value = current_card_deck['value']
current_card_suit = current_card_deck['suit']

print("Starting card is-", current_card_rank + " of " + current_card_suit)

# play one game of this many cards-
for card_number in range(0, NCards):
    answer = input(f"Will the next card be higher or lower than {current_card_rank} of {current_card_suit} ? (enter h or l): ")
    answer = answer.casefold()

    next_card_deck =  getCard(game_deck_list)
    next_card_rank = next_card_deck['rank']
    next_card_suit = next_card_deck['suit']
    next_card_value = next_card_deck['value']

    print(f"Next card is {next_card_rank} of {next_card_suit}")

    if answer == 'h':
        if next_card_value > current_card_value:
            print("You got it right")
            score += 20

        else:
            print("Sorry it was not higher")
            score -= 15

    elif answer == '1':
        if next_card_value < current_card_value:
            score += 20
            print("You got it right it was lower")
        else:
            score -= 15
            print("Sorry it was not lower")

    print("Your score is:", score)
    print()
    current_card_rank = next_card_rank
    current_card_value = next_card_value
    current_card_suit = current_card_suit

    go_again = input("To play again, press Enter of q to quit:")
    if go_again == 'q':
        break








