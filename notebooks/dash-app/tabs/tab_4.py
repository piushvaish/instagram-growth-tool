import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import pandas as pd


filepath='resources/final_probs.csv'
df=pd.read_csv(filepath)
names=df['username'].values
index=df['username'].index.values
nameslist = list(zip(index, names))

tab_4_layout = html.Div([
    html.H3('Results for Testing Dataset'),
    html.Div([
        html.Div([
            html.Div('Select a profile to view their predicted probability:'),
            dcc.Dropdown(
                id='page-3-dropdown',
                options=[{'label': k, 'value': i} for i,k in nameslist],
                value=nameslist[0][0]
            ),

        ],className='three columns'),
        html.Div([
            html.Div(id='page-3-content', style={'fontSize':18}),
            html.Table(id='follower-characteristics'),
            html.Div(id='follower_probability', style={'fontSize':18, 'color':'red'})
            
        ],className='nine columns',style = {'display': 'inline-block'}),
    ],className='twelve columns'),

])
