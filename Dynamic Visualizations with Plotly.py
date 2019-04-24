
# coding: utf-8

# In[1]:


import plotly 
import pandas as pd
import numpy as np


# In[3]:


plotly.tools.set_credentials_file(username='Pallavi_Kolambkar', api_key='TgOK9noUXQQJ3MU2oNV8')


# In[4]:


from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)


# In[17]:


#trying a basic layout first
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

#py.plot(data, filename = 'basic-line', auto_open=True)


# In[6]:


stockdata=pd.read_csv("C:/Users/pallavi/Desktop/prices.csv")


# In[7]:


list(stockdata)


# In[71]:


stockdata.head(10)


# The dataset does not have an individual key attribute but the 'date' and 'symbol' are two key attributes for the particular dataset. The records can be found using the date and symbol attrbutes. These key semantics can be used to describe the value semantics for the particular records matched by the key semantics. Thus 'open','close','high','volume' are the va;ue semantics

# In[69]:


#data = stockdata.loc[:,('symbol')].copy()
#stockdata['symbol'].unique()


# Task Exploration:
# 1. Explore and compare the 'high' values of the leading companies: Apple, Microsoft and Google,in the IT industry.
# 2. Correlate the trend of 'high' values of the companies over the year.
# 3. Browse the value for a particular company.
# 4. Identify the value point for a company for a year as required.

# In[29]:


#changing the date format to get just the standard date format
#from dateutil.parser import parse 
#stockdata['date'] = stockdata['date'].dt.strftime('%d%m%Y')
from datetime import datetime
stockdata['date'] =  pd.to_datetime(stockdata['date'])


# In[44]:


#Getting the data for the three companies respectively
apple_data=stockdata[stockdata['symbol'].isin(['AAPL'])]
microsoft_data=stockdata[stockdata['symbol'].isin(['MSFT'])]
google_data=stockdata[stockdata['symbol'].isin(['GOOGL'])]


# In[67]:


#Visualization 1
apple_chart=go.Scatter(x=list(apple_data["date"]),y=list(apple_data["high"]),name="Apple",visible=True)
microsoft_chart=go.Scatter(x=list(microsoft_data["date"]),y=list(microsoft_data["high"]),name="Microsoft",visible=True)
google_chart=go.Scatter(x=list(google_data["date"]),y=list(google_data["high"]),name="Google",visible=True)

layout = go.Layout(
    title=go.layout.Title(
        text='Comparing the high values of the three leading IT companies',
        xref='paper',
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text='Year',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='black'
                
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text='High values',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='black'
                
            )
        )
    )
)



# In[68]:


data=[apple_chart,microsoft_chart,google_chart]
fig = go.Figure(data=data, layout=layout)
iplot(fig,filename="visualization1")


# Line charts are used to compare values over time, and are useful to show the chnages in the values over time. 
# They are also used to compare changes to more than one group of data. Since the task in visualization 1 was to explore and analyse the data line charts make an excellent choice for the same.
# As seen from the graph there is a significant trend for all teh three companies. The high values for Apple and Google have some extreme points whereas Microsoft seems to have a standard distribution over the years.
# The user can hover over the lines and find the exact high value for a specific month if needed. The user can browse ove rthe maximuma nd minimum value for a certain company.

# Task Exploration:
# 1. Explore and compare the price values of the leading companies: Apple, Microsoft and Google,in the IT industry.
# 2. Correlate the trend of price values of the companies over the year.
# 3. Browse the value for a particular company by clicking on the trace labels.
# 4. Identify the value point for a company for a year as required.

# In[76]:


#visualization 2
trace1 = go.Candlestick(x=apple_data['date'],
                       open=apple_data['open'],
                       high=apple_data['high'],
                       low=apple_data['low'],
                       close=apple_data['close'])
trace2= go.Candlestick(x=microsoft_data['date'],
                       open=microsoft_data['open'],
                       high=microsoft_data['high'],
                       low=microsoft_data['low'],
                       close=microsoft_data['close'],
                          increasing=dict(line=dict(color= '#17BECF')),
                          decreasing=dict(line=dict(color= '#7F7F7F')))
trace3 = go.Candlestick(x=google_data['date'],
                       open=google_data['open'],
                       high=google_data['high'],
                       low=google_data['low'],
                       close=google_data['close'],
                          increasing=dict(line=dict(color= '#7FD61D')),
                          decreasing=dict(line=dict(color= '#447E03')))
data = [trace1,trace2,trace3]
py.iplot(data, filename='candlestick_datetime')


# Candlestick graphs provide the state of the market at a glance.
# The color and shape of the candlestick can help traders determine if an uptrend is part ofa momentum or a spike.
# They help identify the market patterns easily.
# The companies prices values can be studied all at once as four values(open,close,high,low) can be compared. 
# The graph helps in comparing the price distribution of the companies over the years.
# As seen from the graph in the years from 2012 to 2013 the price values for Google and Apple were very similar almost overlapping. However the trend for Microsoft is very consistent throughout the years.
