import pandas as pd

from trick_taking.oh_heck import Oh_Heck

oh = Oh_Heck(num_players=5)
ans = []
trials = 10000
for i in range(trials):
    oh.deal_hands(num_players=oh.num_players, cards_per_hand=2)
    h = oh.hands
    ans.append(len(h[h < 13]))
    oh.reshuffle()


ans_df = pd.DataFrame(ans, columns=['trump_count'])
print(ans_df.value_counts() / trials)

apple = 1