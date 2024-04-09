from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv', index_col=0)

'''
Explore dos parámetros de interés de manera libre y haga correlaciones.
ver proporcion de remote en casos donde el sujeto vive en el mismo lugar que el centro de trabajo
'''

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 9', style={'textAlign':'center'}),
    html.P(children='Análisis de satisfacción salarial: Identificar factores que contribuyen a una mayor satisfacción salarial entre los profesionales de la ciencia de datos.', style={'textAlign':'center'}),
    dcc.Dropdown(salaries_df.company_location.unique(), 'US', id='company-dropdown'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    [Input('company-dropdown', 'value')]
)  

def update_graph(company):
    dff = salaries_df[(salaries_df["company_location"] == company)]
    dfff = dff.groupby(['company_size', 'experience_level'])['salary_in_usd'].mean().reset_index().sort_values(by='company_size', ascending=False)
    print(dfff)
    fig = px.bar(dfff, x='company_size', y='salary_in_usd', color='experience_level', barmode='group')
    fig.update_layout(
        autosize=False,
        width=1600,
        height=720,
    )

    return fig

    
    

if __name__ == '__main__':
    app.run(debug=True)