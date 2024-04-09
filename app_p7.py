from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import numpy as np
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv', index_col=0)

"""
Títulos de trabajo y salario: Analizar la relación entre puestos de trabajo específicos y salarios. 
Identifique qué puestos de trabajo suelen exigir salarios más altos y cuáles están asociados con salarios más bajos.
"""

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 7', style={'textAlign':'center'}),
    html.P(children='Títulos de trabajo y salario: Analizar la relación entre puestos de trabajo específicos y salarios. Identifique qué puestos de trabajo suelen exigir salarios más altos y cuáles están asociados con salarios más bajos.', style={'textAlign':'center'}),
    dcc.Dropdown(np.concatenate([salaries_df.company_location.unique(), ['Global']]), 'Global', id='company-dropdown'),
    dcc.Dropdown(np.concatenate([salaries_df.experience_level.unique(), ['Global']]), 'Global', id='ex-dropdown'),
    html.Div(children=[dcc.Graph(id='top10-bar-graph'), dcc.Graph(id='bottom10-bar-graph')], style={'display':'flex'}),
])


@callback(
    Output('top10-bar-graph', 'figure'),
    [Input('ex-dropdown', 'value'),
     Input('company-dropdown', 'value')]
)  
def top10_bar_graph(experience_level, company_location):
    if company_location != 'Global' and experience_level != 'Global':
        dff = salaries_df[(salaries_df["experience_level"] == experience_level) & (salaries_df["company_location"] == company_location)]
    elif company_location != 'Global':
        dff = salaries_df[(salaries_df["company_location"] == company_location)]
    elif experience_level != 'Global':
        dff = salaries_df[(salaries_df["experience_level"] == experience_level)]
    else:
        dff = salaries_df

    average_salary_by_job_title = dff.groupby('job_title')['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=False)[:10]

    fig = px.histogram(average_salary_by_job_title, y='salary_in_usd', x='job_title')
    fig.update_xaxes(title_text="Job Title")
    fig.update_yaxes(title_text="Average Salary in USD")
    fig.update_layout(title_text=f'10 highest paying job titles', title_x=0.5)
    return fig

@callback(
    Output('bottom10-bar-graph', 'figure'),
    [Input('ex-dropdown', 'value'),
     Input('company-dropdown', 'value')]
)  
def bottom10_bar_graph(experience_level, company_location):
    if company_location != 'Global' and experience_level != 'Global':
        dff = salaries_df[(salaries_df["experience_level"] == experience_level) & (salaries_df["company_location"] == company_location)]
    elif company_location != 'Global':
        dff = salaries_df[(salaries_df["company_location"] == company_location)]
    elif experience_level != 'Global':
        dff = salaries_df[(salaries_df["experience_level"] == experience_level)]
    else:
        dff = salaries_df

    average_salary_by_job_title = dff.groupby('job_title')['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=True)[0:10]

    fig = px.histogram(average_salary_by_job_title, y='salary_in_usd', x='job_title')
    fig.update_xaxes(title_text="Job Title")
    fig.update_yaxes(title_text="Average Salary in USD")
    fig.update_layout(title_text=f'10 lowest paying job titles', title_x=0.5)
    return fig

if __name__ == '__main__':
    app.run(debug=True)