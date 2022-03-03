import random

class Cards:

    def __init__(self, user_guess):
        card_list = self.create_deck
        pass


    def create_deck():
        # Create  a list of cards and store 
        card_list = []
        for suit in ['Spade', 'Club', 'Diamond', 'Heart']:
            for number in range(1, 14):
                card_list.append([number, suit])

        print(card_list)
        return card_list

    def draw(self):
        card_list = self.create_deck()
        card = card_list[random.randint(0, len(card_list) - 1)]
        print(card[0])


    def is_higher(card):
        if 1-6 > 7:
            points += 100
        else:
            points -=75
        
        # user_guess > card
        print('it lives')
    pass

    def is_lower():
        pass