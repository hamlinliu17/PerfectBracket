import pandas as pd 
import numpy as np 


gamesdf = pd.read_csv('games.csv')


dates = np.array(list(gamesdf.loc[:, "date"]))

dates_ = []
tourn_start = '03-14'
tourn_end = '04-04'

for date in dates:
    tournament_date = date.split('-')
    dates_.append(tournament_date)

dates_1 = []

for date in dates_:
    d = []
    for i in date:
        i = int(i)
        d.append(i)
    dates_1.append(d)


tournament = []

for date in dates_1:
    month = date[1]
    day = date[2]
    if month == 3 or month == 4:
        if day >= 12:
            tournament.append(True)
            continue
        tournament.append(False)
    else:
        tournament.append(False)

tournament = np.array(tournament)

gamesdf