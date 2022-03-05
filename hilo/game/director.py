from game.cards import Cards


class Director:
    # controls input, output and player turn.

    
    # defining class attributes
    def __init__(self):
        self.total_points = 300
        self.is_playing = True
        self.user_guess = ''
        self.cards = Cards()
        self.drawn_card = None
    
    # function for game loop
    def game_start(self):
        
        # create instance of card class to show first card
        
        # format of first card [number, suit]
        
        first_card = self.cards.draw()
        print(f'\nThe first card is {first_card[0]}, {first_card[1]}')
        while self.is_playing == True:
            
            self.get_input()
            drawn_card = self.cards.draw()
            self.drawn_card = drawn_card
            self.update_game()
            self.output()

    
    # function to get input
    def get_input(self):
        self.user_guess = input('Guess higher or lower. (h/l): ')

    # function to compare user input, draw cards, and apply points.
    def update_game(self):
        give_points = self.cards.is_higher_or_lower(self.user_guess)
        

        if give_points:
            self.total_points += 100
        else:
            self.total_points -= 75

        if self.total_points <= 0:
            self.output()
        
        """the method for points will be in the cards class, right?"""
        # Cards.points()


    #function to show output
    def output(self):
       
       #for when we have the points method up
        if self.total_points <= 0:
            print(f'\nYour total points are {self.total_points}')
            print('Game Over!')  
            self.is_playing = False
        else:
            print(f'\nYour total points are {self.total_points}') 
            print(f'The next card was: {self.drawn_card}')