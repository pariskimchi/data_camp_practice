



# Iterating with .iterrows()

win_perc_list = []

for i, row in baseball_df.iterrows():
    
    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins,games_played)

    win_perc_list.append(win_perc)

baseball_df['WP'] = win_perc_list

