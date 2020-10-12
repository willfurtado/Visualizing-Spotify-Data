########################
## Personal DataFrame ##
########################

from secrets import PODCAST_ARTISTS, WHITE_NOISE

import numpy as np
import pandas as pd
import seaborn as sns
import json
import time
import matplotlib.pyplot as plt

plt.style.use('ggplot')


#######################
## Loading DataFrame ##
#######################

#Loading First half of dataset
with open('../personal_data/StreamingHistory0.json') as file:
    data = json.load(file)
df0 = pd.DataFrame(data)

#Loading second half of dataset
with open('../personal_data/StreamingHistory1.json') as file:
    data1 = json.load(file)
df1 = pd.DataFrame(data1)

#Appending both together to create one complete DataFrame
df = df0.append(df1, ignore_index=True)

#Replacing millseconds column with a seconds column
df['secPlayed'] = round(df['msPlayed'] / 1000, 1)
df = df.drop(columns=['msPlayed'])

#Converting string format to datetime format of endTime column
STRTIME_FORMAT = '%Y-%m-%d %H:%M'
df['endTime'] = pd.to_datetime(df['endTime'], format=STRTIME_FORMAT)

######################
## Music & Podcasts ##
######################

music = df[~df['artistName'].isin(PODCAST_ARTISTS + WHITE_NOISE)].reset_index(drop=True)
podcasts = df[df['artistName'].isin(PODCAST_ARTISTS)].reset_index(drop=True)


