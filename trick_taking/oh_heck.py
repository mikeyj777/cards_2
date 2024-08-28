import copy
import numpy as np

from trick_taking.trick_taking import Trick_Taking

class Oh_Heck(Trick_Taking):

    def __init__(self, num_players=0, cards_to_specify=[], specified_card_locations=[], bidding_restriction = True, use_trump = True):
        super().__init__(num_players=num_players, cards_to_specify=cards_to_specify, specified_card_locations = specified_card_locations, bidding_restriction=bidding_restriction)
        self.trump_suit = -1
        self.card_designations = {
            'low': 5, # less than a 7 is considered a low card
            'med': 10, # less than a queen is considered a med card.  queen and greater is high
        }

    def play_game(self):
        # start at max cards
        max_cards = len(self.deck) // self.num_players
        # debug xxx apple
        max_cards = 5
        for num_cards in range(max_cards, 0, -1):
            # deal to each player
            self.deal_hands(num_players=self.num_players, cards_per_hand=num_cards)
            

            # trump suit stored as follows:
            # suits are clubs, diamonds, hearts, then spades (alpha order)
            # each suit is assigned a number (0 - clubs, 1- diamonds, 2 - hearts, 3 - spades)
            # the card after players are dealt is the trump suit
            trump_card = self.get_next_card()
            # take the int of the trump card with a divisor of 13.
            # this calculates the suit (0 - clubs, 1- diamonds, 2 - hearts, 3 - spades)
            # if dealing the entire deck as playing cards, a trump card will not be specified
            if num_cards * self.num_players != 52:
                self.trump_suit = int(trump_card/13)
            # each player bids
            self.bid()
            apple = 1

            # play round

            # score round
    
    def bid(self):
        total_bids = 0
        self.hand_designations = []
        for i in range(self.num_players):
            hand = self.hands[i]
            # count num of trump cards
            trump_cards = {
                'low': 0,
                'med': 0,
                'high': 0
            }
            offsuit_cards = copy.deepcopy(trump_cards)
            count_of_cards_per_suit = {
                0: 0,
                1: 0,
                2: 0,
                3: 0
            }
            for card in hand:
                count_of_cards_per_suit[int(card/13)] += 1
                if card % 13 < self.card_designations['low']:
                    if int(card/13) == self.trump_suit:
                        trump_cards['low'] += 1
                    else:
                        offsuit_cards['low'] += 1
                elif card % 13 > self.card_designations['med']:
                    if int(card/13) == self.trump_suit:
                        trump_cards['high'] += 1
                    else:
                        offsuit_cards['high'] += 1
                else:
                    if int(card/13) == self.trump_suit:
                        trump_cards['med'] += 1
                    else:
                        offsuit_cards['med'] += 1
            
            self.hand_designations.append({
                'trump': trump_cards,
                'offsuit': offsuit_cards,
                'num_trump': sum(trump_cards.values()),
                'count_of_cards_per_suit': count_of_cards_per_suit,
            })
        if i == self.num_players - 1:
            if self.bidding_restriction:
                pass
                    
    
    def play_round(self):
        pass

    def score_round(self):
        pass
