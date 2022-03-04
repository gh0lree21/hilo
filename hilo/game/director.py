from game.cards import Cards


class Director:
    # controlls input, output and player turn.

    
    # defining class attributes
    def __init__(self):
        self.total_points = 300
        self.is_playing = True
        self.user_guess = ''

    
    # function for game loop
    def game_start(self):
        
        # create instance of card class to show first card
        
        # format of first card [number, suit]
        
        first_card = Cards.draw()
        print(f'the first card is{first_card}')
        while self.is_playing == True:
            
            self.get_input()
            Cards.draw()
            self.update_game()
            self.output()

    
    # function to get input
    def get_input(self):
        self.user_guess = input('Guess higher or lower. (h/l)')

    # function to compare user input, draw cards, and apply points.
    def update_game(self):
        Cards.is_higher_or_lower()
        
        """the mothod for points will be in the cards class, right?"""
        # Cards.points()


    #function to show output
    def output(self):
       
       #for when we have the points method up
        print('Your total points are ')    