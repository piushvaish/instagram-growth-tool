import sys
import pandas as pd
import numpy as np

from darts import TimeSeries
from darts.models import  AutoARIMA
                          

import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

import warnings
warnings.filterwarnings("ignore")
import logging
logging.disable(logging.CRITICAL)

df = pd.read_csv("resources/profile_growth.csv")
df['Date'] = pd.to_datetime(df['Date'])
# Create a TimeSeries, specifying the time and value columns
series = TimeSeries.from_dataframe(df, 'Date', 'Followers')

# 90 days change
days_increase = str(round((df['Followers'][0] - df['Followers'][90]) / df['Followers'][90] * 100,2)) + "%"

# forecast series
series_df = pd.read_csv("resources/series_df.csv")
forecast_df = pd.read_csv("resources/forecast_df.csv")

 
figure1 = go.Figure()
figure1.add_trace(go.Scatter(x=df['Date'], y=df['Followers'],
                    mode='lines',
                    name='Followers',
                    line=dict(color='rgb(115,115,115)', width=2),
                    connectgaps=True)
                    )

figure1.add_annotation(
        text=days_increase,
             xref="x domain", 
             yref="y domain",
             # The arrow head will be 25% along the x axis, starting from the left
             x=0.25, 
            # The arrow head will be 40% along the y axis, starting from the bottom
             y=0.40, 
             font=dict(
            family="Courier New, monospace",
            size=18,
            color="#ffffff"
            ),
            showarrow=False,
            bordercolor='rgb(67,67,67)',
            borderwidth=1,
            borderpad=10,
            bgcolor='rgb(189,189,189)',
            opacity=0.8
        )

figure1.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showspikes=True
    ),
    autosize=True,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    font_family="Courier New",
    title_font_family="Times New Roman",
    title="Growth",
    hovermode="x unified",
    legend_title_text=str(days_increase) + "%",
    legend = dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=1,
    font=dict(
            family="Arial",
            size=12,
            color="black"
    ),
    ),
    plot_bgcolor='white'
)

# discovery
figure2 = go.Figure()

figure2.add_trace(go.Scatter(x=df['Date'], y=df['Impressions'],
                    mode='lines+markers',
                    name='Impressions',
                    line=dict(color='rgb(67,67,67)', width=2),
                    connectgaps=True))
figure2.add_trace(go.Scatter(x=df['Date'], y=df['Reach'],
                    mode='lines+markers',
                    name='Reach',
                    line=dict(color='rgb(189,189,189)', width=2),
                    connectgaps=True))


figure2.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showspikes=True
    ),
    autosize=True,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    font_family="Courier New",
    title_font_family="Times New Roman",
    hovermode="x unified",
    legend_title_text='Discovery',
    legend = dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01,
    font=dict(
            family="Arial",
            size=12,
            color="black"
    ),
    ),
    plot_bgcolor='white'
)

# forecast
# Create traces
figure3 = go.Figure()
figure3.add_trace(go.Scatter(x=series_df['Date'], y=series_df['Followers'],
                    mode='lines',
                    name='ToDate',
                    line=dict(color='rgb(67,67,67)', width=2),
                    connectgaps=True))
figure3.add_trace(go.Scatter(x=forecast_df['Date'], y=forecast_df['Followers'],
                    mode='lines+markers',
                    name='Forecast',
                    line=dict(color='rgb(49,130,189)', width=2),
                    connectgaps=True))

figure3.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showspikes=True
    ),
    autosize=True,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    font_family="Courier New",
    title_font_family="Times New Roman",
    hovermode="x unified",
    legend_title_text='Forecast',
    legend = dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01,
    font=dict(
            family="Arial",
            size=12,
            color="black"
    ),
    ),
    plot_bgcolor='white'
)

tab_2_layout = html.Div(children=[
    html.Div([
    html.H4(children='''
       Number of Followers
    '''),
    html.Div(
    dcc.Graph(
        id='growth-graph',
        figure=figure1)
    )],style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
    html.H4(children='''
       Impressions & Reach
    '''),
    html.Div(
    dcc.Graph(
        id='discovery-graph',
        figure=figure2)
    )],style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
    html.H4(children='''
       Forecast
    '''),
    html.Div(
    dcc.Graph(
        id='forecast-graph',
        figure=figure3)
    )],style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
],className='nine columns')