from trick_taking.trick_taking import Trick_Taking

class Oh_Heck(Trick_Taking):

    def __init__(self, num_players=0, cards_to_specify=[], specified_card_locations=[], bidding_restriction = True):
        super().__init__(num_players=num_players, cards_to_specify=cards_to_specify, specified_card_locations = specified_card_locations, bidding_restriction=bidding_restriction)

