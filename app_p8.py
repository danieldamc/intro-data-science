from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv', index_col=0)

"""
Títulos de trabajo y salario: Analizar la relación entre puestos de trabajo específicos y salarios. 
Identifique qué puestos de trabajo suelen exigir salarios más altos y cuáles están asociados con salarios más bajos.
"""

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Grafico de Linea', style={'textAlign':'center'}),
    dcc.Dropdown(salaries_df.experience_level.unique(), 'MI', id='ex-dropdown'),
    html.Div(children=[dcc.Graph(id='top10-bar-graph'), dcc.Graph(id='bottom10-bar-graph')], style={'display':'flex'}),
])


@callback(
    Output('top10-bar-graph', 'figure'),
    [Input('ex-dropdown', 'value')]
)  
def top10_bar_graph(experience_level):
    average_salary_by_job_title = salaries_df.groupby('job_title')['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=False)[:10]

    fig = px.histogram(average_salary_by_job_title, y='salary_in_usd', x='job_title')
    fig.update_xaxes(title_text="Job Title")
    fig.update_yaxes(title_text="Average Salary in USD")
    fig.update_layout(title_text=f'10 highest paying job titles', title_x=0.5)
    return fig

@callback(
    Output('bottom10-bar-graph', 'figure'),
    [Input('ex-dropdown', 'value')]
)  
def bottom10_bar_graph(experience_level):
    average_salary_by_job_title = salaries_df.groupby('job_title')['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=True)[0:10]

    fig = px.histogram(average_salary_by_job_title, y='salary_in_usd', x='job_title')
    fig.update_xaxes(title_text="Job Title")
    fig.update_yaxes(title_text="Average Salary in USD")
    fig.update_layout(title_text=f'10 lowest paying job titles', title_x=0.5)
    return fig

if __name__ == '__main__':
    app.run(debug=True)