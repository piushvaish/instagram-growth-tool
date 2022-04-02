import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import pickle
import joblib
from tabs import tab_1, tab_2, tab_3, tab_4, tab_5
from utils import display_eval_metrics


df=pd.read_csv('resources/final_probs.csv')


## Instantiante Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config['suppress_callback_exceptions'] = True
app.title='Instagram Growth Strategy'

# Load Preprocess
preprocess = joblib.load('resources/preprocess.joblib')
### load ML model ###########################################
with open('resources/final_model.pkl', 'rb') as f:
    model = pickle.load(f)


## Layout
app.layout = html.Div([
    html.H1('Instagram Growth Strategy'),
    dcc.Tabs(id="tabs-template", value='tab-1-template', children=[
        dcc.Tab(label='Introduction', value='tab-1-template'),
        dcc.Tab(label='Time Series', value='tab-2-template'),
        dcc.Tab(label='Model Evaluation', value='tab-3-template'),
        dcc.Tab(label='Testing Results', value='tab-4-template'),
        dcc.Tab(label='User Inputs', value='tab-5-template')
        
    ]),
    html.Div(id='tabs-content-template')
])


############ Callbacks

@app.callback(Output('tabs-content-template', 'children'),
              [Input('tabs-template', 'value')])
def render_content(tab):
    if tab == 'tab-1-template':
        return tab_1.tab_1_layout
    elif tab == 'tab-2-template':
        return tab_2.tab_2_layout
    elif tab == 'tab-3-template':
        return tab_3.tab_3_layout
    elif tab == 'tab-4-template':
        return tab_4.tab_4_layout
    elif tab == 'tab-5-template':
        return tab_5.tab_5_layout

# Tab 2 callbacks

@app.callback(Output('page-2-graphic', 'figure'),
              [Input('page-2-radios', 'value')])
def radio_results(value):
    return display_eval_metrics(value)

# Tab 3 callback # 1
@app.callback(Output('page-3-content', 'children'),
              [Input('page-3-dropdown', 'value')])
def page_3_dropdown(value):
    name=df.loc[value, 'username']
    return f'You have selected "{name}"'

# Tab 3 callback # 2
@app.callback(Output('follower_probability', 'children'),
              [Input('page-3-dropdown', 'value')])

def page_3_follower(value):
    follower=df.loc[value, 'follower_probability']
    actual = df.loc[value,'actual']
    follower=round(follower*100)
    return f'Predicted probability of following is {follower}%, Actual status is {actual}'

# Tab 3 callback # 2
@app.callback(Output('follower-characteristics', 'children'),
              [Input('page-3-dropdown', 'value')])
def page_3_characteristics(value):
    mydata=df.drop(['actual', 'follower_probability', 'username'], axis=1)
    mydata=df[['is_private', 'mediacount', 'followers', 'followees', 'is_business_account', 'has_public_story']]
    return html.Table(
        [html.Tr([html.Th(col) for col in mydata.columns])] +
        [html.Tr([
            html.Td(mydata.iloc[value][col]) for col in mydata.columns
        ])]
    )

# Tab 4 Callback # 1
@app.callback(Output('prediction_output', 'children'),
              Input('submit_val', 'n_clicks'), State('mediacount', 'value'),
              State('followers', 'value'), State('followees', 'value'),
              State('is_private', 'value'),
              State('is_business_account', 'value'),
              State('has_public_story', 'value'))
def update_output(n_clicks, mediacount, followers, followees, is_private,
                  is_business_account, has_public_story):
    inputs = [
        mediacount, followers, followees, is_private, is_business_account,
        has_public_story
    ]
    keys = [
        'mediacount', 'followers', 'followees', 'is_private',
        'is_business_account', 'has_public_story'
    ]
    dict6 = dict(zip(keys, inputs))
    df = pd.DataFrame([dict6])
    # drop unnecessary columns, and reorder columns to match the final model.

    df = df[[
        'is_private', 'mediacount', 'followers', 'followees',
        'is_business_account', 'has_public_story'
    ]]

    df_new = preprocess.transform(df)
    prob = model.predict_proba(df_new)
    final_prob = round(float(prob[0][1]) * 100, 1)
    return (f'Probability of Survival: {final_prob}%')



####### Run the app #######
if __name__ == '__main__':
    app.run_server(debug=True)
