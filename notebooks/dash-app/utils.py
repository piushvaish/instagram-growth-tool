import pandas as pd
import plotly
import plotly.graph_objs as go
import pickle
from sklearn.metrics import roc_auc_score
from tabs.tab_3 import choices
import json

def display_eval_metrics(value):

    ### Comparison of Possible Models
    if value==choices[0]:
        compare_models=pd.read_csv('resources/compare_models.csv', index_col=0)
        # Let's display that with plotly.
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=compare_models.loc['F1 score'].index,
            y=compare_models.loc['F1 score'],
            name=compare_models.index[0],
            marker_color='rgb(107,174,214)'
        ))

        fig.add_trace(go.Bar(
            x=compare_models.loc['Accuracy'].index,
            y=compare_models.loc['Accuracy'],
            name=compare_models.index[1],
            marker_color='rgba(219, 64, 82, 0.6)'
        ))

        fig.add_trace(go.Bar(
            x=compare_models.loc['AUC score'].index,
            y=compare_models.loc['AUC score'],
            name=compare_models.index[2],
            marker_color='rgb(7,40,89)'
        ))

        fig.update_layout(
            title='Comparison of Possible Models',
            xaxis = dict(title = 'Predictive models'), # x-axis label
            yaxis = dict(title = 'Score'), # y-axis label
            
        )
        return fig

    ### Final Model Metrics
    elif value==choices[1]:
        file = open('resources/eval_scores.pkl', 'rb')
        evals=pickle.load(file)
        file.close()
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=list(evals.keys()),
            y=list(evals.values())
        ))

        fig.update_traces(marker_color='rgb(107,174,214)', marker_line_color='rgb(8,48,107)',
                        marker_line_width=1.5, opacity=0.6)

        fig.update_layout(
            title='Evaluation Metrics for Random Forest Model (Testing Dataset = 578 profiles)',
            xaxis = {'title': 'Metrics'},
            yaxis = {'title': 'Percent'}, 

        )
        return fig

    # Receiver Operating Characteristic (ROC): Area Under Curve
    elif value==choices[2]:

        with open('resources/roc_dict.json') as json_file:
            roc_dict = json.load(json_file)
        FPR=roc_dict['FPR']
        TPR=roc_dict['TPR']
        y_test=pd.Series(roc_dict['y_test'])
        predictions=roc_dict['predictions']

        roc_score=round(100*roc_auc_score(y_test, predictions),1)
        fig = go.Figure()

        fig.add_trace(go.Scatter(
                x=FPR, 
                y=TPR,
                mode='lines',
                name=f'AUC: {roc_score}',
                marker_color='rgb(150,150,150)'
                ))
        fig.add_trace(go.Scatter(
                x=[0,1], 
                y=[0,1],
                mode='lines',
                name='Baseline Area: 50.0',
                marker_color='rgb(37,37,37)'
                ))
        fig.update_layout(
            title='Receiver Operating Characteristic (ROC): Area Under Curve',
            xaxis={'title': 'False Positive Rate (100-Specificity)','scaleratio': 1,'scaleanchor': 'y'},
            yaxis={'title': 'True Positive Rate (Sensitivity)'}
            )
        return fig

    # Confusion Matrix
    elif value==choices[3]:
        with open('resources/roc_dict.json') as json_file:
            roc_dict = json.load(json_file)
        FPR=roc_dict['FPR']
        TPR=roc_dict['TPR']
        y_test=pd.Series(roc_dict['y_test'])
        
        cm=pd.read_csv('resources/confusion_matrix.csv')
        fig = go.Figure()

        fig.add_trace(go.Table(
            header=dict(values=cm.columns,
                        line = dict(color='rgb(150,150,150)'),
                        fill = dict(color='rgb(150,150,150)'),
                        align = ['left'] * 5),
            cells=dict(values=[cm[f'n={len(y_test)}'], cm['pred: follower'], cm['pred: non-follower']],
                    line = dict(color='#7D7F80'),
                    fill = dict(color='white'),
                    align = ['left'] * 5)))

        fig.update_layout(
            title = f'Confusion Matrix: Random Forest Model (Testing Dataset)'
        )
        return fig

    # Odds of Survival (Coefficients)
    elif value==choices[4]:
        coeffs=pd.read_csv('resources/coefficients.csv')
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=coeffs['feature'],
            y=coeffs['coefficient']
        ))

        fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                        marker_line_width=1.5, opacity=0.6)

        fig.update_layout(
            title='Number of Followers is a good indication of becoming a follower.',
            xaxis = {'title': 'Instagram Features'},
            yaxis = {'title': 'Odds of Becoming a Follower'}, 

        )
        return fig
