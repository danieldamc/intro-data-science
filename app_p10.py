'''Explore dos parámetros de interés de manera libre y haga correlaciones.
ver proprcion de remote en casos donde el sujeto vive en el mismo lugar que el centro de trabajo
'''
from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv', index_col=0)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Grafico de Donut', style={'textAlign':'center'}),
    dcc.Dropdown(salaries_df.company_location.unique(), 'US', id='company-dropdown'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    [Input('company-dropdown', 'value')]
)  

def update_graph(company):
    dff = salaries_df[(salaries_df["employee_residence"] == company)] 

    remote_ratio_df = dff['remote_ratio'].value_counts().reset_index()
    #order the values in the remote_ratio column
    remote_ratio_df = remote_ratio_df.sort_values(by='remote_ratio')
    #print(remote_ratio_df)
    fig = px.pie(remote_ratio_df, values='count', names='remote_ratio', title=f'Proportion of Remote Work in {company} for workers living in said location', hole=0.3, color_discrete_sequence=px.colors.sequential.RdBu)

    return fig

    
    

if __name__ == '__main__':
    app.run(debug=True)