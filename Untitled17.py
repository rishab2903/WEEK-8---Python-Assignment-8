#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash, dash_table
import dash_core_components as dcc

from sort_dataframeby_monthorweek import *
import dash_html_components as html
import pandas as pd
from sorted_months_weekdays import *


# In[2]:


df_covid = pd.read_csv('~/Downloads/covid-19-data-master 2/us-states.csv')
external_stylesheets = ['https://ragarwal.github.io/dash.github.io/learn.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# In[3]:


df.groupby('Date').sum()  
confirmed = df.groupby('Date').sum()['Confirmed'].reset_index()
deaths = df.groupby('Date').sum()['Deaths'].reset_index()
recovered = df.groupby('Date').sum()['Recovered'].reset_index()



# In[4]:


import folium
map_usa = folium.Map(location=[37.0902, -95.7129],zoom_start=4)
for lat, lng, city,state,deaths,recovered, month in zip(df_covid['Latitude'], df_covid['Longitude'], df_covid['City Or County'],df_covid['State'], df_covid['deaths'], df_covid['recovered'], df_covid['Month']):
    label = 'City: {}, State:{}, deaths: {}, recovered: {}, Month:{}'.format(city,state,deaths,recovered, month)
    folium.CircleMarker(
        [lat, lng],
        radius=injured,
        popup=label,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.1,
        parse_html=False).add_to(map_usa)


# In[5]:


app.layout = html.Div(confirmed=[html.H1(confirmed='Python Dash',style={'textAlign':'center'}),
                                html.H1(confirmed='Covid-19 cases in US',style={'textAlign':'center'}),
                                dash_table.DataTable(columns=[{'name':i,'id':i} for i in df_mass.columns], data=df_covid.head().to_dict('records'),),
                               dcc.Graph(figure={'data':[
                                   {'x':df191.Month,'y':df191.Injured, 'type':'bar','name':'recovered'},
                                   {'x':df19.Month,'y':df19.Killed, 'type':'bar','name':'deaths'},],
                                                'layout': {'title': 'Covid-19'}}),
                               dcc.Graph(figure={'data':[
                                   {'x':df201.Month,'y':df201.Injured, 'type':'bar','name':'recovered'},
                                   {'x':df20.Month,'y':df20.Killed, 'type':'bar','name':'deaths'},],
                                                'layout': {'title': 'Covid-19'}}),
                               html.Div([html.H3(children='Covid-19',style={'textAlign':'center'}),html.Iframe(srcDoc=open('t.html','r').read(),width='100%',height='600')]),
                               html.Div([html.H3(children='Covid-19',style={'textAlign':'center'}), html.Iframe(srcDoc=open('t2.html','r').read(),width='100%',height='600')])])
                               
                                 


# In[ ]:


if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:




