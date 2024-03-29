#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


ipl_match = pd.read_csv('C:/Users/DEV/Downloads/IPL_Matches_2008_2022.csv')


# In[3]:


# Finding the shape of the dataset
ipl_match.shape


# In[4]:


# Info of the dataset IPL_match
ipl_match.info()


# In[5]:


# we have to change the date format datatype.


# In[6]:


ipl_match['Date'] = pd.to_datetime(ipl_match['Date'])


# In[7]:


ipl_match


# In[8]:


# Toss win equal to match win
ipl_match[ipl_match['TossWinner'] == ipl_match['WinningTeam']]['ID'].count()


# In[9]:


# Percentage of toss win
ipl_match[ipl_match['TossWinner'] == ipl_match['WinningTeam']]['ID'].count()/ipl_match.shape[0]


# In[10]:


ipl_match['WinningTeam'].value_counts()


# In[11]:


ipl_match['TossWinner'].value_counts()


# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns
chart = sns.countplot(data = ipl_match , x = 'WinningTeam', orient = "h")
chart.set_xticklabels(chart.get_xticklabels(), rotation=90)


# In[13]:


chart = sns.countplot(data = ipl_match , x = 'TossWinner', orient = "h")
chart.set_xticklabels(chart.get_xticklabels(), rotation=90)


# In[14]:


toss_winner_match_winner = ipl_match[ipl_match['TossWinner'] == ipl_match['WinningTeam']]


# In[15]:


toss_winner_match_winner['TossWinner'].value_counts()


# In[16]:


chart = sns.countplot(data = toss_winner_match_winner, x= 'TossWinner', orient = "h")
chart.set_xticklabels(chart.get_xticklabels(), rotation=90)


# In[17]:


pd.DataFrame(toss_winner_match_winner['TossWinner'].value_counts()/(ipl_match['Team1'].value_counts() + ipl_match['Team2'].value_counts())).sort_values(by= 0,ascending = False)


# In[18]:


pd.DataFrame(ipl_match['TossWinner'].value_counts()/(ipl_match['Team1'].value_counts() + ipl_match['Team2'].value_counts())).sort_values(by=0,ascending = False)


# In[19]:


ipl_match.groupby(['City','TossWinner'])['TossWinner'].count().unstack()


# In[20]:


ipl_match.groupby(['City','WinningTeam'])['WinningTeam'].count().unstack()


# In[21]:


ipl_match


# In[22]:


ipl_match.groupby(['TossWinner','TossDecision'])['TossWinner'].count().unstack()


# In[23]:


ipl_match.groupby(['WinningTeam','WonBy'])['WinningTeam'].count().unstack()


# In[24]:


ipl_match['Player_of_Match'].value_counts().sort_values(ascending = False).head(10)


# In[25]:


pd.DataFrame(ipl_match.groupby('Season')['Player_of_Match'].value_counts())


# In[26]:


ipl_match.groupby(['City','WonBy'])['City'].count().unstack()


# In[27]:


venue_dict = {'Wankhede Stadium':'Wankhede Stadium, Mumbai','Eden Gardens':'Eden Gardens, Kolkata',
              'Brabourne Stadium':'Brabourne Stadium, Mumbai',
             'Arun Jaitley Stadium':'Arun Jaitley Stadium, Delhi',
             'M Chinnaswamy Stadium': 'M.Chinnaswamy Stadium',
             'MA Chidambaram Stadium, Chepauk, Chennai':'MA Chidambaram Stadium, Chepauk',
             'Dr DY Patil Sports Academy':'Dr DY Patil Sports Academy, Mumbai',
             'Punjab Cricket Association IS Bindra Stadium':'Punjab Cricket Association Stadium, Mohali',
             'Punjab Cricket Association IS Bindra Stadium, Mohali':'Punjab Cricket Association Stadium, Mohali',
             'Maharashtra Cricket Association Stadium':'Maharashtra Cricket Association Stadium, Pune'}


# In[28]:


ipl_match['Venue'] = ipl_match['Venue'].replace(venue_dict)
ipl_match


# In[31]:


# Now, We merge the two datasets
ball_by_ball = pd.read_csv('C:/Users/DEV/Downloads/IPL_Ball_by_Ball_2008_2022.csv')
ball_by_ball
Merged_Data = ipl_match.merge(ball_by_ball,how = 'inner',on = 'ID')
Merged_Data


# In[32]:


Merged_Data.info()


# In[33]:


Merged_Data['Venue'].unique()


# In[34]:


# There are multiple spellings for a single stadium. Let us convert all the values


# In[35]:


venue_dict = {'Wankhede Stadium':'Wankhede Stadium, Mumbai','Eden Gardens':'Eden Gardens, Kolkata',
              'Brabourne Stadium':'Brabourne Stadium, Mumbai',
             'Arun Jaitley Stadium':'Arun Jaitley Stadium, Delhi',
             'M Chinnaswamy Stadium': 'M.Chinnaswamy Stadium',
             'MA Chidambaram Stadium, Chepauk, Chennai':'MA Chidambaram Stadium, Chepauk',
             'Dr DY Patil Sports Academy':'Dr DY Patil Sports Academy, Mumbai',
             'Punjab Cricket Association IS Bindra Stadium':'Punjab Cricket Association Stadium, Mohali',
             'Punjab Cricket Association IS Bindra Stadium, Mohali':'Punjab Cricket Association Stadium, Mohali',
             'Maharashtra Cricket Association Stadium':'Maharashtra Cricket Association Stadium, Pune'}


# In[36]:


Merged_Data['Venue'] = Merged_Data['Venue'].replace(venue_dict)
Merged_Data


# In[38]:


# Top 10 Batsman of all seasons
top_10_batsman_of_all_seasons = pd.DataFrame(Merged_Data.groupby('batter')['total_run'].sum().sort_values(ascending = False).head(10))
top_10_batsman_of_all_seasons


# In[40]:


# Most wicket takers of all seasons
Wicket_taken_balls = Merged_Data[Merged_Data['isWicketDelivery']==1]
Top_10_wicket_Takers = pd.DataFrame(Wicket_taken_balls.groupby('bowler')['isWicketDelivery'].sum().sort_values(ascending = False).head(10))
Top_10_wicket_Takers


# In[41]:


# Top 10 Bowlers with minimum economy
Total_Runs = Merged_Data.groupby('bowler')['total_run'].sum().sort_values(ascending=False)
b = pd.DataFrame(Total_Runs)
b


# In[42]:


Total_deliveries_by_bowler = Merged_Data.groupby('bowler')['overs'].count().sort_values(ascending=False)
Total_deliveries_by_bowler = Total_deliveries_by_bowler[Total_deliveries_by_bowler > 200]
a = pd.DataFrame(Total_deliveries_by_bowler)
a


# In[43]:


Economy_of_Bowler = pd.DataFrame((Total_Runs / Total_deliveries_by_bowler).sort_values(ascending = True)).head(10)
Economy_of_Bowler


# In[44]:


# Strike Rate of batsman
Batsman_total_runs = Merged_Data.groupby('batter')['total_run'].sum().sort_values(ascending=False)
Batsman_total_runs


# In[45]:


Total_balls_faced_by_batsman = Merged_Data.groupby('batter')['batter'].count().sort_values(ascending=False)
Total_balls_faced_by_batsman = Total_balls_faced_by_batsman[Total_balls_faced_by_batsman > 200]
Total_balls_faced_by_batsman


# In[47]:


df_bats_SR = pd.DataFrame(((Batsman_total_runs / Total_balls_faced_by_batsman)*100).sort_values(ascending = False))
df_bats_SR


# In[49]:


Caught = Merged_Data[Merged_Data['kind'] == 'caught']
Caught


# In[50]:


# Fielders Who caught maximum catches
Caught.groupby('fielders_involved')['fielders_involved'].count().sort_values(ascending = False).head(10)


# In[51]:


sixes_by_stadium = Merged_Data[Merged_Data['total_run'] == 6]


# In[52]:


# Maximum Sixes by stadium
pd.DataFrame(sixes_by_stadium['Venue'].value_counts()).head(11)


# In[53]:


fours_by_stadium = Merged_Data[Merged_Data['total_run'] == 4]


# In[54]:


# Highest number of fours by stadium
pd.DataFrame(fours_by_stadium['Venue'].value_counts()).head(11)


# In[55]:


# Last 5 overs analysis
last_5_overs = Merged_Data[Merged_Data['overs'] > 14]


# In[56]:


# Average run in last 5 overs
Average_runs_in_last_5_overs = last_5_overs['total_run'].mean()*30
Average_runs_in_last_5_overs


# In[58]:


wicket_in_last_5_overs = last_5_overs[last_5_overs['isWicketDelivery']== 1]


# In[59]:


total_innings = last_5_overs.groupby('ID')['ID'].nunique().sum()*2
total_innings


# In[60]:


Avg_wickets_in_last_5_overs = (wicket_in_last_5_overs.shape[0] / total_innings)


# In[61]:


# Average run in last 5 overs season wise
# First filter for last 5 overs. Then apply groupby season. Then fetch the mean for total run columns
(pd.DataFrame(last_5_overs.groupby('Season')['total_run'].mean()*30))


# In[62]:


#Average Wickets in last 5 overs season wise
# First filter for last 4 overs and is wicket delivery. then groupby season ftech a column and then its mean
wickets_last_5_over = Merged_Data[(Merged_Data['overs']>15) & (Merged_Data['isWicketDelivery']==1)]
wickets_last_5_over


# In[63]:


wickets_last_5_over.groupby('Season')['isWicketDelivery'].count()


# In[64]:


wickets_last_5_over.groupby('Season')['ID'].count()/ipl_match.groupby('Season')['ID'].count()


# In[65]:


# Most player wicket in last 5 overs
wickets_last_5_over.groupby(['player_out'])['player_out'].count().sort_values(ascending = False).head(10)


# In[67]:


fours_in_last_5_overs = last_5_overs[last_5_overs['batsman_run']==4]


# In[68]:


fours_in_last_5_overs.groupby('batter')['batter'].count().sort_values(ascending = False).head(10)


# In[70]:


sixes_in_last_5_overs = last_5_overs[last_5_overs['batsman_run']== 6]


# In[71]:


sixes_in_last_5_overs.groupby('batter')['batter'].count().sort_values(ascending = False).head(10)


# In[73]:


Zeros_in_last_5_overs = last_5_overs[last_5_overs['batsman_run']== 0]


# In[74]:


Zeros_in_last_5_overs.groupby('batter')['batter'].count().sort_values(ascending = False).head(10)


# In[76]:


last_5_overs.groupby('bowler')['batsman_run'].sum().sort_values(ascending = False).head(10)


# In[ ]:




