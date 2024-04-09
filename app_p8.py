from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd
import numpy as np

salaries_df = pd.read_csv('Salaries.csv', index_col=0)

not_usd_salaries_df = salaries_df[salaries_df['salary_currency'] != 'USD'].reset_index(drop=True)
not_usd_salaries_df['convertion_rate'] = not_usd_salaries_df['salary_in_usd']/not_usd_salaries_df['salary']
convertion_rate_df = pd.DataFrame(not_usd_salaries_df.groupby(['salary_currency', 'work_year'])['convertion_rate'].mean().reset_index())


"""
Análisis de conversión de moneda: Evalúe el impacto de las fluctuaciones monetarias en los salarios 
de la ciencia de datos comparando los salarios en diferentes monedas con sus valores equivalentes en USD. 
Identifique cualquier diferencia significativa en los niveles salariales después de la conversión de moneda.
"""

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 8', style={'textAlign':'center'}),
    html.P(children='Análisis de conversión de moneda: Evalúe el impacto de las fluctuaciones monetarias en los salarios de la ciencia de datos comparando los salarios en diferentes monedas con sus valores equivalentes en USD. Identifique cualquier diferencia significativa en los niveles salariales después de la conversión de moneda.', style={'textAlign':'center'}),
    dcc.Dropdown(np.concatenate([salaries_df.salary_currency.unique(), ['ALL']]), 'ALL', id='salary-dropdown'),
    dcc.Graph(id='line-graph'),
])

@callback(
    Output('line-graph', 'figure'),
    [Input('salary-dropdown', 'value')]
)  
def line_graph(salary_currency):

    if salary_currency != 'ALL':
        dff = convertion_rate_df[convertion_rate_df["salary_currency"] == salary_currency]
    else:
        dff = convertion_rate_df

    print(dff)

    fig = px.line(dff, y='convertion_rate', x='work_year', color='salary_currency')
    fig.update_xaxes(title_text="Work Year")
    fig.update_yaxes(title_text="Convertion Rate")
    fig.update_layout(title_text=f'Convertion Rate of Salary', title_x=0.5)
    return fig

if __name__ == '__main__':
    app.run(debug=True)