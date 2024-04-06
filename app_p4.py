from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv')
salaries_df = salaries_df.drop(columns=['Unnamed: 0'])

"""
Disparidades salariales regionales: Examine cómo varían los salarios entre las diferentes 
residencias de los empleados y las ubicaciones de las empresas (países). 
Identifique regiones/países donde los científicos de datos tienden a ganar salarios más altos en comparación con otros.
"""

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 4', style={'textAlign':'center'}),
    dcc.Dropdown(salaries_df.experience_level.unique(), 'EN', id='ex-dropdown'),
    dcc.Slider(0, 20, 1, value=10, marks={0:{'label':'0'}, 20:{'label':'20'}}, tooltip={"placement": "bottom", "always_visible": True}, id='threshold-slider'),
    dcc.Graph(id='pie-graph'),
    dcc.Graph(id='bar-graph'),
])


@callback(
    Output('bar-graph', 'figure'),
    [Input('threshold-slider', 'value'),
     Input('ex-dropdown', 'value')]
)  
def update_bar_graph(threshold, experience_level):
    dff = salaries_df[(salaries_df["experience_level"] == experience_level)]

    average_salary_company_location = dff.groupby(['company_location'])['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=False)

    fig = px.histogram(average_salary_company_location, y='salary_in_usd', x='company_location', title=f'Company Location Pie Chart')
    return fig

@callback(
    Output('pie-graph', 'figure'),
    [Input('threshold-slider', 'value'),
     Input('ex-dropdown', 'value')]
)  
def update_pie_graph(threshold, experience_level):
    dff = salaries_df[(salaries_df["experience_level"] == experience_level)]
    count_df = pd.DataFrame(dff.company_location.value_counts()).reset_index(inplace=False)

    other_count = count_df[count_df['count'] < threshold]['count'].sum()

    other_row = {'company_location': 'OTHER', 'count': other_count}
    filtered_list = count_df[count_df['count'] >= threshold].to_dict('records')
    filtered_list.append(other_row)

    other_df = pd.DataFrame(filtered_list)
    fig = px.pie(other_df, values='count', names='company_location', title=f'Company Location Pie Chart')
    return fig



if __name__ == '__main__':
    app.run(debug=True)
