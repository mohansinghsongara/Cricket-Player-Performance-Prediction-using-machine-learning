#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv('matches - matches (1).csv')


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.tail(1)


# In[6]:


data.shape


# In[7]:



data.describe()


# In[8]:


data.info()


# In[9]:


data.head()


# In[10]:


data[["winner",'team1','team2']].shape


# In[11]:


data[["winner",'team1','team2']]


# In[12]:


data.iloc[[1,444,6]]


# In[13]:


mask =data ['city']=='hyderabad'


# In[14]:


mask = data['city']=='Hyderabad'
data[mask].shape[0]


# In[15]:


def get_city_match_count(winner):
    mask = data['winner']==winner
    return data[mask].shape[0]


# In[16]:


get_city_match_count('Royal Challengers Bangalore')


# In[17]:


mask1 = data['winner'] =='Mumbai Indians'
mask2 = data['date']>"2010-01-01"

data[mask1 & mask2].shape[0]


# In[18]:


data['season'].value_counts()


# In[19]:


import matplotlib.pyplot as plt


# In[20]:


data['winner'].value_counts().head().plot(kind = ('pie') )


# In[21]:


data['toss_decision'].value_counts()


# In[22]:


data['win_by_runs'].plot(kind='hist')


# In[23]:


data['winner'].value_counts()


# In[24]:


myseries = data['winner'].value_counts()
myseries


# In[25]:


myseries['Gujarat Lions']


# In[26]:


myseries.index


# In[27]:


data['team1'].value_counts()+data['team2'].value_counts()


# In[28]:


data.head()


# In[29]:


data.drop_duplicates(subset=['city','season']).shape


# In[30]:


data.drop_duplicates('season',keep='last')[['season','winner']].sort_values('season')


# In[31]:


data['winner'].value_counts().head(1).index[0]


# In[32]:


runs =data.groupby('player_of_match')
runs


# In[33]:


runs.get_group('GJ Maxwell').shape


# In[34]:


import pandas as pd


# In[35]:


match = pd.read_csv('deliveries.csv')
match


# In[36]:


mask = match['batsman_runs']==3
new_delivery=match[mask]


# In[37]:


new_delivery.shape[0]


# In[38]:


new_delivery.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False).head(5)


# In[39]:


vk = match[match['batsman']=='Yuvraj Singh']
vk.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head(3)


# In[40]:


def run_scored (batsman_name):
    vk = match[match['batsman']== batsman_name] 
    return vk.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head(3)


# In[41]:


run_scored('Yuvraj Singh')


# In[42]:


# isin()
# find the most destructive death over batsman in the history of IPL
# strike Rate = (Number of runs/Number of balls)/100
# min batsman 200 balls in over 16-20


# In[43]:


match.groupby('batsman')['batsman_runs'].count()


# In[44]:


death_over = match[match['over']>15]


# In[45]:


all_batsman = death_over.groupby('batsman')['batsman_runs'].count()
x = all_batsman>200
batsman_list =all_batsman[x].index.tolist()


# In[46]:


# Runs scored by all these 43 batsman
# balls played by these 43 batsman

final =match[match['batsman'].isin(batsman_list)]


# In[47]:


final.groupby('batsman')['batsman_runs'].sum()


# In[48]:


runss = final.groupby('batsman')['batsman_runs'].sum()


# In[49]:


balls = final.groupby('batsman')['batsman_runs'].count()


# In[50]:


sr = (runss/balls)*100
sr


# ### Merge
# 

# In[51]:


# Merge
new = match.merge(data,left_on='match_id',right_on='id')


# In[52]:


print(match.shape)
print(data.shape)


# In[53]:


new.groupby(['season','batsman'])['batsman_runs'].sum().sort_values(ascending=False).reset_index().drop_duplicates(subset='season',keep='first')


# In[54]:


match.head()


# In[55]:


mask=match['batsman_runs']==6
six = match[mask]
six.shape


# In[56]:


pt=six.pivot_table(index='over',columns='batting_team',values='batsman_runs',aggfunc='count')


# In[57]:


import seaborn as sns


# In[58]:


pt=six.pivot_table(index='over',columns='batting_team',values='batsman_runs',aggfunc='count')


# In[59]:


sns.heatmap(pt)


# In[60]:


data


# In[61]:


data.corr()


# In[62]:


sns.heatmap(data.corr())


# In[63]:


data.rename(columns={'city':'place','date':'dom'},inplace=True)


# In[64]:


data


# #### set_index()and reset_index()

# In[65]:


data.set_index('id',inplace=True)


# In[67]:


data.reset_index(inplace=True)


# In[68]:


data


# In[71]:


data['winner'].value_counts().reset_index()


# #### 1.Dropping missing data using dropna()

# In[75]:


data.shape


# In[79]:


data.dropna(axis=1,how='all').shape


# In[82]:


data.dropna(subset=['umpire3']).shape


# In[81]:


data


# #### Filling missing values using fillna()

# In[83]:


data.fillna(0)


# In[84]:


data['umpire3'].fillna('not specified',inplace= True)


# In[85]:


data['']


# In[ ]:




