'''

Adding tournament columns to differentiate games that are tournaments and non tournaments

Author: Hamlin Liu

'''

import pandas as pd 
import numpy as np 

#reading csv
gamesdf = pd.read_csv('games.csv', dtype = {'pts' : 'str'})


# checking for value error in the csv
# error 1 -> index 9094 
# error 2 -> index 13491
# error 3 -> index 19633

pts = np.array(list(gamesdf.loc[:, "pts"]))

error_indices = []
for p in range(len(pts)):
    try:
        int(pts[p])
    except ValueError:
        error_indices.append(p)









'''

dates = np.array(list(gamesdf.loc[:, "date"]))

#compiling dates
dates_ = []

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

'''