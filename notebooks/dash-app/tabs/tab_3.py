import dash
from dash import dcc
from dash import html
import pandas as pd

choices=['Comparison of Models',
'Final Model Metrics',
'ROC-AUC',
'Confusion Matrix',
'Feature Importance']

tab_3_layout = html.Div([
    html.H3('Model Evaluation Statistics'),
    html.Div([
        html.Div([
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                id='page-2-radios',
                options=[{'label': i, 'value': i} for i in choices],
                value='Comparison of Models'
            ),
        ],className='three columns'),
        html.Div([
            dcc.Graph(id='page-2-graphic')
        ],className='nine columns',style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    ], className=' twelve columns')




])
