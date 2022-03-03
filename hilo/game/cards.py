import random

# Purpose: Create cards and check values.
class Cards:

    def __init__(self):
        # Stores previous card
        self.previous_card = None
        
        # Stores current card which will be displayed to the user
        self.card = [0, 'Wowza']

        # Variable that checks to see if the game is starting up or has already been played once.
        self.second_time = 0


    # Create a list of cards and store
    def create_deck(self):
        card_list = []
        for suit in ['Spade', 'Club', 'Diamond', 'Heart']:
            for number in range(1, 14):
                card_list.append([number, suit])

        print(card_list)
        return card_list

    def draw(self):
        # If the game is starting up for the first time create a deck of cards
        if not self.second_time:
            card_list = self.create_deck()
            assert len(card_list) == 52, 'For loops are off if this fires'
            self.second_time += 1
            print('\n\n n \n\n')


        # Keeps track of the previous card 
        self.previous_card = self.card[0]
        
        # Choose a random card out of the 52 that have been created within the deck.
        self.card = card_list[random.randint(0, len(card_list) - 1)]
        
        
        return self.card

    # Check user guess and return if the user was correct or not.
    def is_higher_or_lower(self, card, user_guess):
        if user_guess.lower() == 'h':
            
            points += 100
        else:
            pass
        
        # user_guess > card
        print('it lives')
    pass



# Currently the code below checks to make sure that a drawn card is actually retrieved
player1 = Cards()
print('\n\n', player1.draw(), ' -- The previous is the card drawn \n\n')
print(player1.previous_card)