'''Títulos de trabajo y salario: Analizar la relación entre
 puestos de trabajo específicos y salarios. 
 Identifique qué puestos de trabajo suelen exigir salarios más altos
   y cuáles están asociados con salarios más bajos.'''

from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv')
salaries_df = salaries_df.drop(columns=['Unnamed: 0'])

app = Dash(__name__, external_stylesheets=['p7.css'])

app.layout = html.Div([
    html.H1(children='Grafico de Donut', style={'textAlign': 'center'}),
    dcc.Dropdown(options=[{'label': location, 'value': location} for location in salaries_df.company_location.unique()], value='US', id='company-dropdown'),
    html.Div(className='graphs-container', children=[
        dcc.Graph(id='graph-content1', className='graph'),
        dcc.Graph(id='graph-content2', className='graph'),
        dcc.Graph(id='graph-content3', className='graph'),
        dcc.Graph(id='graph-content4', className='graph'),
    ])
], style={'display': 'flex', 'flexDirection': 'column'})


@callback(
    [Output('graph-content1', 'figure'),
    Output('graph-content2', 'figure'),
    Output('graph-content3', 'figure'),
    Output('graph-content4', 'figure')],
    [Input('company-dropdown', 'value')]
)  

def update_graph(company):
    dff = salaries_df[(salaries_df["company_location"] == company)] 

    average_salary_per_job_title = dff.groupby(['experience_level', 'job_title'])['salary_in_usd'].mean().reset_index()


    list_of_figs = []
    for exp in average_salary_per_job_title['experience_level'].unique():
        #combine all the figures to show on one graph
        fig = px.pie(average_salary_per_job_title[average_salary_per_job_title['experience_level'] == exp], values='salary_in_usd', names='job_title', title=f'Salary Distribution per Job Title in {company} for {exp} experience level')
        list_of_figs.append(fig)

    
    
    return list_of_figs

if __name__ == '__main__':
    app.run(debug=True)