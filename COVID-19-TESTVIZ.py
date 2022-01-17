#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use ('fivethirtyeight')

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv', parse_dates=['Date'])
df.head()

df['Total Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)


# In[21]:


# Worldwide Cases
worldwide_df = df.groupby(['Date']).sum()
w = worldwide_df.plot(figsize=(5,5))
w.set_xlabel('Date')
w.set_ylabel('# of Cases Worldwide')
w.title.set_text('Worldwide Covid Insights')
plt.show()


# In[42]:


us_df = df[df['Country']=='US'].groupby(['Date']).sum()
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)

ax.plot(worldwide_df[['Total Cases']], label ='Worldwide')
ax.plot(us_df[['Total Cases']], label='United States')



ax.set_xlabel('Date')
ax.set_ylabel('# of Total Cases')
ax.title.set_text('Worldwide vs. United States Total Cases')
plt.legend(loc = 'upper left')
plt.show


# In[85]:


us_df['Daily Deaths'] = us_df['Daily Deaths'].sub(us_df['Deaths'].shift())
us_df['Daily Confirmed'] = us_df['Daily Confirmed'].sub(us_df['Confirmed'].shift())


fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111)
ax.set_xlabel('Date')
ax.set_ylabel('# Of People Affected')
ax.title.set_text('US Daily Cases and Deaths')
ax.bar(us_df['Date'], us_df['Daily Confirmed'], color='b', label ='US daily Confirmed Cases')
ax.bar(us_df['Date'], us_df['Daily Deaths'], color='r', label = 'US daily Deaths')
plt.legend(loc = 'upper left')
plt.show


# In[109]:


from datetime import date, timedelta
yesterday = date.today()- timedelta(days=1)
yesterday.strftime('%Y-%m-%d')

today_df = df[df['Date']==yesterday]
top_10 = today_df.sort_values(['Confirmed'], ascending=False)[:10]
top_10.loc['rest-of-world'] = today_df.sortvalues(['Confirmed'], ascending=False)[:10].sum()


# In[ ]:




