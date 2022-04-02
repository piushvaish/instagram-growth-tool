import dash
from dash import dcc
from dash import html
import base64

insta_photo=base64.b64encode(open('resources/clean_instagram_logo2.png', 'rb').read())


tab_1_layout = html.Div([
    html.H3('Introduction'),
    html.Div([
    html.Div([
        dcc.Markdown("This dashboard is a template for capstone presentations of machine learning. Though simple, it has several important features:"),
        dcc.Markdown("* Time Series Modelling to forecast the number of followers based on current activity."),
        dcc.Markdown("* A cleaned dataset with a clearly defined problem and target variable."),
        dcc.Markdown("* A predictive model that has been trained on a portion of the data, and tested on a set-aside portion."),
        dcc.Markdown("* Evaluation metrics showing the performance of the model on the testing data."),
        dcc.Markdown("* Individual results of the testing dataset, for further analysis of incorrect predictions."),
        dcc.Markdown("* A feature to receive new user inputs that makes predictions based on the new data."),
        dcc.Markdown("* An interactive user interface deployed on a cloud platform and accessible to potential reviewers."),
        html.A('View code on github', href='https://github.com/piushvaish/instagram-growth-strategy'),
    ],className='ten columns'),
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(insta_photo.decode())),
    ],className='two columns'),


    ],className='nine columns'),

])
