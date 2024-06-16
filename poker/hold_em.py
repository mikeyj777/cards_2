from card_deck.dealt_cards import Dealt_Cards

# num_players = 0, include_dealer = False, cards_per_hand = 0, cards_to_specify = [], specified_card_locations = []):
class Hold_Em(Dealt_Cards):

    def __init__(self, num_players=0, cards_to_specify=[], specified_card_locations=[]):
        self.board = []
        super().__init__(num_players, include_dealer=False, cards_per_hand=2, shuffle_it=True, cards_to_specify=cards_to_specify, specified_card_locations = specified_card_locations)

    def deal_all_stages(self):
        self.deal_flop()
        self.deal_turn()
        self.deal_river()

    def deal_flop(self):
        # burn 1
        card = self.get_next_card()
        
        # turn 3
        for i in range(3):
            card = self.get_next_card()
            self.board.append(card)
        

    def deal_turn(self):
        # burn 1
        card = self.get_next_card()

        # turn 1
        card = self.get_next_card()
        self.board.append(card)

    def deal_river(self):
        # burn 1
        card = self.get_next_card()

        # turn 1
        card = self.get_next_card()
        self.board.append(card)

