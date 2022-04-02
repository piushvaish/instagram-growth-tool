import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import numpy as np
import joblib
import pickle
import pandas as pd

filepath='resources/final_probs.csv'
df=pd.read_csv(filepath)
names=df['username'].values
index=df['username'].index.values
nameslist = list(zip(index, names))

tab_5_layout = html.Div([
    dbc.Row([html.H4(children='Would the profile become a follower?')]),
    dbc.Row([
        dbc.Col(html.Label(children='Media Count:  ')),
        dbc.Col(dcc.Input(id='mediacount', 
                  type='number', 
                  min=0, max=1000, step=1, value=0))
    ],style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='Followers:')),
        dbc.Col(dcc.Input(id='followers', 
                  type='number', 
                  min=0, max=1000, step=1, value=0))
    ],style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='Followees:')),
        dbc.Col(dcc.Input(id='followees', 
                  type='number', 
                  min=0, max=1000, step=1, value=0))
    ],style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Br(),
    dbc.Row([
       dbc.Col(html.Label(children='Is Private:')),
       dbc.Col(dcc.RadioItems(
                id='is_private',
                options=[{'label': i, 'value': i} for i in [0,1]],
                value=0,
                ))
    ],style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    dbc.Row([
        dbc.Col(html.Label(children='Is Business Account:')),
        dbc.Col(dcc.RadioItems(
                id='is_business_account',
                options=[{'label': i, 'value': i} for i in [0,1]],
                value=0,
                ))
    ],style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    dbc.Row([
        dbc.Col(html.Label(children='Has Public Story:')),
        dbc.Col(dcc.RadioItems(
                id='has_public_story',
                options=[{'label': i, 'value': i} for i in [0,1]],
                value=1,
                )) 
    ],style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Br(),
    dbc.Row([dbc.Button('Submit', id='submit_val', n_clicks=0, color="primary", style={'text-align':'center','fontSize':18})]),
    html.Br(),
    dbc.Row([html.Div(id='prediction_output')], style={'color':'red','text-align':'center','fontSize':18})
    
    ],className='twelve columns', style = {'padding': '0px 0px 0px 150px', 'width': '50%'})