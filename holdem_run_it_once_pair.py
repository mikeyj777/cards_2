import pandas as pd
from poker.hold_em import Hold_Em

import datetime

num_players = 2

max_players = 9
max_runs = 10
max_hands = 1000

# vary number of players, only two are in all-in hand

res_list = []

for num_players in range(2, max_players + 1):
    # vary nubmer of time it's run
    for num_runs in range(1, max_runs + 1):
        player_1_makes_pair = 0
        for i in range(max_hands):
            # ace-king for hero / qj for villain
            hold_em = Hold_Em(num_players=num_players, cards_to_specify=[11, 12, 9 + 13, 10 + 13, 7, 8, 32, 40], specified_card_locations=[0, num_players, 1, num_players + 1, (num_players * 2) + 1, (num_players * 2) + 2, (num_players * 2) + 3, (num_players * 2) + 5])
            # get board full up to turn
            hold_em.deal_hands()
            hold_em.deal_flop()
            hold_em.deal_turn()
            pair_made = False
            for curr_run in range(1, num_runs + 1):
                if pair_made:
                    break
                for _ in range(2):
                    card = hold_em.get_next_card()
                if card % 13 == 11: # or card % 13 == 12:
                    player_1_makes_pair += 1
                    pair_made = True
        
        res_list.append({ 
            'num_players': num_players,
            'num_runs': num_runs,
            'num_hands': max_hands,
            'player_1_makes_pair': player_1_makes_pair
        })

res_df = pd.DataFrame(res_list)
d_stamp = datetime.datetime.now(datetime.UTC).strftime("%Y_%m_%d_%H_%M_%S")
res_df.to_csv(f'hold_em_runits_pair_{d_stamp}.csv', index=False)


apple = 1
