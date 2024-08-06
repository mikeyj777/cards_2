import pandas as pd

from card_deck.dealt_cards import Dealt_Cards

# num_players = 0, include_dealer = False, cards_per_hand = 0, cards_to_specify = [], specified_card_locations = []):
class Trick_Taking(Dealt_Cards):

    def __init__(self, num_players=0, cards_to_specify=[], specified_card_locations=[], bidding_restriction = False):
        super().__init__(num_players=num_players, include_dealer=False, shuffle_it=True, cards_to_specify=cards_to_specify, specified_card_locations = specified_card_locations)
        self.board = []
        self.num_players = num_players
        scoring_df_columns = [f'player_{x}' for x in range(num_players)]
        self.scoring_df = pd.DataFrame(columns = scoring_df_columns)
        self.bidding_restriction = bidding_restriction

    def play_game(self):
        pass

    def bid(self):
        pass
    
    def play_round(self):
        pass

    def score_round(self):
        pass