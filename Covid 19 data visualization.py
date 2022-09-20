#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
print('modules are imported')


# In[2]:


#loading the dataset
dataset_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(dataset_url)


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df = df[df.Confirmed > 0 ]
df.head()


# In[7]:


df[df.Country == 'Italy']


# In[8]:


#A choropleth map is a map that is used to represent a special variations of a quantity which in our case, the quantity is a number of confirmed cases.
fig = px.choropleth(df , locations = 'Country' , locationmode='country names', color='Confirmed', animation_frame = 'Date')
fig.update_layout(title_text = 'Global Spread of COVID-19')
fig.show()


# In[9]:


#Deaths
fig = px.choropleth(df , locations = 'Country' , locationmode='country names', color='Deaths', animation_frame = 'Date')
fig.update_layout(title_text = 'Global Deaths of COVID-19')
fig.show()


# In[10]:


#China
df_china = df[df.Country == 'China']
df_china.head()


# In[11]:


df_china = df_china[['Date' , 'Confirmed']]
df_china.head()


# In[12]:


#Adding Infection Rate
df_china['Infection Rate'] = df_china['Confirmed'].diff()
df_china.head()


# In[13]:


df_china.tail()


# In[14]:


px.line(df_china , x ='Date' , y = ['Confirmed' , 'Infection Rate'])


# In[15]:


df_china['Infection Rate'].max()


# In[16]:


#maximum infection rate for all of the countries
countries = list(df['Country'].unique())
#countries
max_infection_rates = []
for c in countries :
    MIR = df[df.Country == c].Confirmed.diff().max()
    max_infection_rates.append(MIR)   
#print(max_infection_rates)


# In[17]:


#creat a new dataframe
df_MIR = pd.DataFrame()
df_MIR['Country'] = countries
df_MIR['Max Infection Rate'] = max_infection_rates
df_MIR


# In[18]:


#barchart : maximum infection rate of each country
#log_y=True  : add more scales to y axis
px.bar(df_MIR, x='Country', y='Max Infection Rate', color='Country', title='Global Maximum Infection', log_y=True)


# In[19]:


#How National vaccinations Impacts Covid-19 transmission in Italy


# In[20]:


italy_vaccinations_start_date = '2021-01-06'
italy_vaccinations_ayear_later = '2022-01-06'


# In[21]:


df.head()


# In[22]:


df_italy = df[df.Country == 'Italy']
df_italy.head()


# In[23]:


df_italy['Infection Rate'] = df_italy.Confirmed.diff()
df_italy.head()


# In[24]:


#visualization
fig = px.line(df_italy , x='Date' , y='Infection Rate' , title="Before and After vaccinations in Italy")
#fig.show()
fig.add_shape(
    dict(
    type ="line",
    x0= italy_vaccinations_start_date,
    y0=0,
    x1=italy_vaccinations_start_date,
    y1=df_italy['Infection Rate'].max(),
    line = dict(color ='red' , width =2 )
    )
)
fig.add_annotation(
    dict(
    x = italy_vaccinations_start_date,
    y = df_italy['Infection Rate'].max(),
    text = 'starting date of the vaccinations'
    )
)
fig.add_shape(
    type ="line",
    x0= italy_vaccinations_ayear_later,
    y0=0,
    x1=italy_vaccinations_ayear_later,
    y1=df_italy['Infection Rate'].max(),
    line = dict(color ='orange' , width =2 )   
    )

fig.add_annotation(
    dict(
    x = italy_vaccinations_ayear_later,
    y = df_italy['Infection Rate'].max(),
    text = 'A year later'
    )
)


# In[25]:


df_italy.head()


# In[26]:


df_italy['Deaths Rate'] = df_italy.Deaths.diff()


# In[27]:


#check the dataframe again
df_italy.head()


# In[28]:


#visualization - line chart
fig = px.line(df_italy, x='Date' , y=['Infection Rate' , 'Deaths Rate'])
fig.show()


# In[29]:


#normalization - columns 
df_italy['Infection Rate'] = df_italy['Infection Rate']/df_italy['Infection Rate'].max()
df_italy['Deaths Rate'] = df_italy['Deaths Rate']/df_italy['Deaths Rate'].max()


# In[30]:


#line chart
fig = px.line(df_italy, x='Date' , y= ['Infection Rate' , 'Deaths Rate'])
fig.add_shape(
    dict(
    type ="line",
    x0= italy_vaccinations_start_date,
    y0=0,
    x1= italy_vaccinations_start_date,
    y1=1,
    line = dict(color ='red' , width =2 )
    )
)
fig.add_annotation(
    dict(
    x = italy_vaccinations_start_date,
    y = 1,
    text = 'starting date of the vaccinations'
    )
)
fig.add_shape(
    dict(
    type ="line",
    x0= italy_vaccinations_ayear_later,
    y0=0,
    x1= italy_vaccinations_ayear_later,
    y1=1,
    line = dict(color ='orange' , width =2 )   
    )
)
fig.add_annotation(
    dict(
    x = italy_vaccinations_ayear_later,
    y = 0,
    text = 'A year later'
    )
)


# In[31]:


Germany_lockdown_start_date = '2020-03-23'
Germanay_lockdown_a_month_later = '2020-04-23'


# In[32]:


df_germany = df[df.Country == 'Germany']


# In[33]:


df_germany['Infection Rate'] = df_germany.Confirmed.diff()


# In[34]:


fig = px.line(df_germany , x='Date' , y='Infection Rate' , title="Before and After Lockdown in Germany")
#fig.show()
fig.add_shape(
    dict(
    type ="line",
    x0= Germany_lockdown_start_date,
    y0=0,
    x1=Germany_lockdown_start_date,
    y1=df_germany['Infection Rate'].max(),
    line = dict(color ='red' , width =2 )
    )
)
fig.add_annotation(
    dict(
    x = Germany_lockdown_start_date,
    y = df_germany['Infection Rate'].max(),
    text = 'starting date of the lockdown'
    )
)
fig.add_shape(
    dict(
    type ="line",
    x0= Germanay_lockdown_a_month_later ,
    y0=0,
    x1=Germanay_lockdown_a_month_later ,
    y1=df_germany['Infection Rate'].max(),
    line = dict(color ='orange' , width =2 )   
    )
)
fig.add_annotation(
    dict(
    x = Germanay_lockdown_a_month_later ,
    y = df_germany['Infection Rate'].max(),
    text = 'A month later'
    )
)


# In[35]:


df_germany['Deaths Rate'] = df_germany.Deaths.diff()


# In[36]:


fig = px.line(df_germany, x='Date' , y=['Infection Rate' , 'Deaths Rate'])
fig.show()


# In[37]:


df_germany['Infection Rate'] = df_germany['Infection Rate']/df_germany['Infection Rate'].max()
df_germany['Deaths Rate'] = df_germany['Deaths Rate']/df_germany['Deaths Rate'].max()


# In[38]:


fig = px.line(df_germany, x='Date' , y= ['Infection Rate' , 'Deaths Rate'])
fig.add_shape(
    dict(
    type ="line",
    x0= Germany_lockdown_start_date,
    y0=0,
    x1= Germany_lockdown_start_date,
    y1=1,
    line = dict(color ='red' , width =2 )
    )
)
fig.add_annotation(
    dict(
    x = Germany_lockdown_start_date,
    y = 1,
    text = 'starting date of the lockdown'
    )
)
fig.add_shape(
    dict(
    type ="line",
    x0= Germanay_lockdown_a_month_later ,
    y0=0,
    x1= Germanay_lockdown_a_month_later ,
    y1=1,
    line = dict(color ='orange' , width =2 )   
    )
)
fig.add_annotation(
    dict(
    x = Germanay_lockdown_a_month_later ,
    y = 0,
    text = 'A month later'
    )
)


# In[ ]:





# In[ ]:





# In[ ]:




