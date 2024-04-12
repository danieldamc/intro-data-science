from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import numpy as np
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv', index_col=0)

"""
Impacto del tipo de empleo en los salarios: Explore cómo los tipos de empleo 
(a tiempo parcial, a tiempo completo, por contrato, autónomo) influyen en los
salarios. Analice si ciertos tipos de empleo tienden a ofrecer salarios más altos que otro.
"""

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 3', style={'textAlign':'center'}),
    html.P(children='Impacto del tipo de empleo en los salarios: Explore cómo los tipos de empleo (a tiempo parcial, a tiempo completo, por contrato, autónomo) influyen en los salarios. Analice si ciertos tipos de empleo tienden a ofrecer salarios más altos que otro.', style={'textAlign':'center'}),
    #dcc.Dropdown(salaries_df.company_location.unique(), 'US', id='company-dropdown'),
    dcc.Dropdown(np.concatenate([salaries_df.company_location.unique(), ['GLOBAL']]), 'GLOBAL', id='company-dropdown'),
    html.Div(children=[
        dcc.Graph(id='line-graph'),
        dcc.Graph(id='pie-graph'),
    ], style={'display':'flex'}),
])

@callback(
    Output('line-graph', 'figure'),
    [Input('company-dropdown', 'value')]
)  
def update_graph(company):
    if company != 'GLOBAL':
        dff = salaries_df[salaries_df["company_location"] == company]
    else:
        dff = salaries_df
    #dff = salaries_df[(salaries_df["company_location"] == company)] 

    average_salary_per_year = dff.groupby(['work_year', 'employment_type'])['salary_in_usd'].mean().reset_index()
    
    fig = px.line(average_salary_per_year, x='work_year', y='salary_in_usd', markers=True, color = 'employment_type')
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    fig.update_yaxes(range=[0, average_salary_per_year['salary_in_usd'].max() + 20000])
    fig.update_yaxes(tickmode='linear', dtick=50000)
    fig.update_layout(
        autosize=False,
        width=1300,
        height=720,
    )
    #add a title for axis
    fig.update_xaxes(title_text="Work Year")
    fig.update_yaxes(title_text="Average Salary in USD")
    fig.update_layout(title_text=f'Salary per contract type', title_x=0.5)

    return fig

@app.callback(
    Output('pie-graph', 'figure'),
    [Input('company-dropdown', 'value')]
)
def update_pie_graph(company):
    
    if company != 'GLOBAL':
        dff = salaries_df[(salaries_df["company_location"] == company)]
    else:
        dff = salaries_df
    
    #dff = salaries_df[(salaries_df["company_location"] == company)] 
    type_count = pd.DataFrame(dff.employment_type.value_counts()).reset_index(inplace=False)

    fig = px.pie(type_count, values='count', names='employment_type', hole=.4)
    fig.update_layout(
        autosize=False,
        width=500,
        height=720,
    )
    
    fig.update_layout(title_text=f'Number of employees per contract type', title_x=0.5)
    return fig      


if __name__ == '__main__':
    app.run(debug=True)