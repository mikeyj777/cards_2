import numpy as np

from card_deck.standard_deck import Standard_Deck

num_players = 5
include_dealer = True
cards_per_hand = 2


class Dealt_Cards(Standard_Deck):

    def __init__(self, num_players = 0, include_dealer = False, cards_per_hand = 0, shuffle_it = True, cards_to_specify = [], specified_card_locations = []):

        self.num_players = num_players
        self.include_dealer = include_dealer
        self.cards_per_hand = cards_per_hand
        self.hands = []
        self.deck_position = 0

        super().__init__(shuffle_it = shuffle_it, cards_to_specify = cards_to_specify, specified_card_locations = specified_card_locations)
    
    def deal_hands(self, num_players = 0, cards_per_hand = 0, include_dealer = None):

        if include_dealer is None:
            include_dealer = self.include_dealer

        if num_players < 1:
            num_players = self.num_players
        
        if cards_per_hand < 1:
            cards_per_hand = self.cards_per_hand
        
        hands_to_deal = num_players
        if include_dealer:
            hands_to_deal += 1
        
        self.hands = np.zeros((hands_to_deal, cards_per_hand))
        for hand_card in range(cards_per_hand):
            for i in range(hands_to_deal):
                self.hands[i,hand_card] = self.get_next_card()
    
    def get_next_card(self):

        if self.deck_position >= len(self.deck):
            print('that\'s all the cards')
            return
        
        card = self.deck[self.deck_position]
        self.deck_position += 1

        return card

    def reshuffle(self):
        self.deck_position = 0
        self.shuffle()