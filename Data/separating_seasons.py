'''
7/30/2019

Hamlin Liu

Separating the game data into seasons
'''

import pandas as pd
import numpy as np 
from datetime import datetime



def create_seasons(dates):
    # creates a dictionary of seasons from all the dates in the date column
    dates_li = [date.split('/') for date in dates] # reading the dates
    seasons = {}
    for i in range(len(dates_li)): #adding the index of the dates
        date = dates_li[i]
        s = '/'
        month = int(date[0])
        year = int(date[2])
        if month >= 11:
            year += 1
        if year not in seasons:
            seasons[year] = [i]
            continue
        seasons[year].append(i)
    return seasons

def newSeasonDF(targets, df, year, start):
    # utilizes a previous dataset, the dates in that data set, a set year, and a time that it starts
    # outputs a new csv file for each season
    newdf = pd.DataFrame(columns = list(df.columns))
    
    
    print('done finding the target dates', str(datetime.now()-start)[:9])
    newdf = newdf.append(df.loc[targets, :], ignore_index = True, sort=False)



    newdf = newdf.drop('Unnamed: 0', 1)

    newdf.to_csv('Seasons/' + str(year - 1) + '-' + str(year) + '_season.csv')



    return newdf

gamesdf = pd.read_csv('data_tournament.csv')




#============================ creating the csvs

start = datetime.now()

dates = gamesdf['date']

seasons  =  create_seasons(dates)

print('done creating dictionary', str(datetime.now()-start)[:9])



df = []
for i in seasons:
    print(i)
    df = newSeasonDF(seasons[i], gamesdf, i, start)











