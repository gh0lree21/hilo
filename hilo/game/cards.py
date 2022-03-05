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
    
        # Stores all 52 cards
        self.deck = None


    # Create a list of cards and store into deck list
    def create_deck(self):
        deck = []
        for suit in ['Spade', 'Club', 'Diamond', 'Heart']:
            for number in range(1, 14):
                deck.append([number, suit])
        self.deck = deck

        return deck

    def draw(self):
        # If the game is starting up for the first time create a new deck of cards
        if not self.second_time:
            self.create_deck()

            # Generates first card of the game
            self.card = self.deck[random.randint(0, len(self.deck) - 1)]
            
            # This variable makes sure that this only runs once per game
            self.second_time += 1
            assert self.second_time < 2

        else:
            # Keeps track of the previous card 
            previous_card = self.card[0]
            self.previous_card = previous_card
       
            # Choose a random card out of the 52 that have been created within the deck.
            self.card = self.deck[random.randint(0, len(self.deck) - 1)]    
            
            # Removes used card from deck
            self.deck.remove(self.card)
        
        return self.card

    # Check user guess and return if the user was correct or not.
    def is_higher_or_lower(self, user_guess):
        assert type(user_guess) == str
        assert user_guess.lower() == 'h' or user_guess.lower() == 'l', 'A string was passed other that l or h'
        
        print('Self.previous_card is:', self.previous_card)
        print('Self.card is:', self.card)
        if user_guess.lower() == 'h':
            if self.card[0] >= self.previous_card:
                return True
            else:
                False
        else:
            if self.card[0] <= self.previous_card:
                return True
            else:
                return False