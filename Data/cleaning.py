'''

Adding tournament columns to differentiate games that are tournaments and non tournaments

Author: Hamlin Liu

'''

import pandas as pd 
import numpy as np 



#==========================cleaning out games.csv


#reading csv
gamesdf = pd.read_csv('games.csv', dtype = {'pts' : 'str'})


# checking for value error in the csv using the points column
# correcting error by referring to sports reference
# error 1 -> index 9094 
# error 2 -> index 13491
# errors -> index 19633, 49710, 59456, 68595

#games at 13491, 68595 have no opponent data
opp_fta = np.array(list(gamesdf.loc[:, "opp_fta"]))

non_opponent = []
for p in range(len(opp_fta)):
    try:
        int(opp_fta[p])
    except ValueError:
        non_opponent.append(p)


#games at 18 have 0 ft_per
# sports reference --> leaves ft_per blank causing columns to be shifted

empty_fta = []

ft = np.array(list(gamesdf.loc[:, "ft"]))
fta = np.array(list(gamesdf.loc[:, "fta"]))
ft_per = np.array(list(gamesdf.loc[:, "ft_per"]))
for p in range(len(ft_per)):
    if ft[p] == 0 and fta[p] == 0 and ft_per[p] != 0:
        empty_fta.append(p)


#unshifting those games
err_games = []
for err in empty_fta:
    err_games.append(list(gamesdf.iloc[err]))

for game in err_games:
    game.insert(16, 0)
    game.pop()



for i in range(len(err_games)):
    gamesdf.iloc[empty_fta[i], :] = err_games[i]

opp_fta = np.array(list(gamesdf.loc[:, "opp_fta"]))
non_opponent = []
for p in range(len(opp_fta)):
    try:
        int(opp_fta[p])
    except ValueError:
        non_opponent.append(p)

for empty in non_opponent:
    gamesdf.drop(gamesdf.index[empty])

gamesdf.to_csv('data_cleaned.csv')






#============================adding tournament columns



dates = np.array(list(gamesdf.loc[:, "date"]))

#compiling dates
dates_ = []

for date in dates:
    tournament_date = date.split('/')
    dates_.append(tournament_date)

dates_1 = []

for date in dates_:
    d = []
    for i in date:
        i = int(i)
        d.append(i)
    dates_1.append(d)


tournament = []

#differentiating between tournament and non tournament
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

#adding tournaments into a column

gamesdf["Tournament"] = tournament

gamesdf.head()


gamesdf.to_csv('data_tournament.csv')
