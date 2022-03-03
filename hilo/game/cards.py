import random

# Purpose: Create cards and check values.
class Cards:

    def __init__(self):
        # Stores previous card
        self.previous_card = None
        
        # Stores current card which will be displayed to the user
        self.card = None

        # Variable that checks to see if the game is starting up or has already been played once.
        self.second_time = 0

        self.deck = None


    # Create a list of cards and store
    def create_deck(self):
        deck = []
        for suit in ['Spade', 'Club', 'Diamond', 'Heart']:
            for number in range(1, 14):
                deck.append([number, suit])
        self.deck = deck
        print(deck)
        return deck

    def draw(self):
        # If the game is starting up for the first time create a deck of cards
        if not self.second_time:
            self.create_deck()

            self.card = self.deck[random.randint(0, len(self.deck) - 1)]
            
            # assert len(card_list) == 52, 'For loops are off if this fires'
            
            # Makes sure that this if statement only runs once
            self.second_time += 1
            print('\n\n self: Second Time', self.second_time, '\n\n')

        else:

            # Keeps track of the previous card 
            self.previous_card = self.card[0]
            print('This is self.card:', self.card[0])
        
            # Choose a random card out of the 52 that have been created within the deck.
            self.card = self.deck[random.randint(0, len(self.deck) - 1)]
        
        
        return self.card

    # Check user guess and return if the user was correct or not.
    def is_higher_or_lower(self, user_guess):
        if user_guess.lower() == 'h':
            if self.card[0] < self.previous_card:
                return True
            else:
                False
        else:
            if self.card[0] > self.previous_card:
                return False
            else:
                return True
            pass
        
        # user_guess > card
        print('it lives')


player1 = Cards()
# Currently the code below checks to make sure that a drawn card is actually retrieved
for _ in range(0, 4):
    print('\n\n', player1.draw(), ' -- card drawn \n\n')
    print(player1.previous_card)