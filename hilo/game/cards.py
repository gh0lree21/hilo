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
        # print(deck)
        return deck

    def draw(self):
        # If the game is starting up for the first time create a deck of cards
        if not self.second_time:
            self.create_deck()

            # Generates first card of the game
            self.card = self.deck[random.randint(0, len(self.deck) - 1)]
            
            # This variable makes sure that this only runs once per game
            self.second_time += 1
            assert self.second_time < 2

            # Uncomment the following to make sure that self.second_time is working
            # properly and that this only runs once per game.
            # print('\n\n self: Second Time', self.second_time, '\n\n')

        else:
            # Keeps track of the previous card 
            self.previous_card = self.card[0]

            # print('This is previous.card:', self.previous_card)
        
            # Choose a random card out of the 52 that have been created within the deck.
            self.card = self.deck[random.randint(0, len(self.deck) - 1)]            
            
            self.deck.remove(self.card)
            # print(self.deck)


            # print('This is Current card:', self.card[0])
        
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


# player1 = Cards()
# Currently the code below checks to make sure that a drawn card is actually retrieved and that the
# corrosponding card is removed from the deck.
# for _ in range(0, 53):
#     print('\n\n', player1.draw(), ' -- card drawn \n\n')
#     print(player1.previous_card)