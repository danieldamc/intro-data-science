from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv')
salaries_df = salaries_df.drop(columns=['Unnamed: 0'])

# Tendencias salariales a lo largo del tiempo: Analice cómo han evolucionado los salarios en 
# ciencia de datos a lo largo de los años examinando la distribución de los salarios en 
# diferentes años laborales. Identifique cualquier tendencia o patrón significativo en el crecimiento o disminución del salario a lo largo del tiempo.

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 4', style={'textAlign':'center'}),
    dcc.Slider(0, 20, 1, value=10, marks={0:{'label':'0'}, 20:{'label':'20'}},tooltip={"placement": "bottom", "always_visible": True}, id='threshold-slider'),
    dcc.Graph(id='pie-graph')
])


@callback(
    Output('pie-graph', 'figure'),
    [Input('threshold-slider', 'value')]
)  
def update_graph(threshold):
    count_df = pd.DataFrame(salaries_df.company_location.value_counts()).reset_index(inplace=False)

    other_count = count_df[count_df['count'] < threshold]['count'].sum()

    other_row = {'company_location': 'OTHER', 'count': other_count}
    filtered_list = count_df[count_df['count'] >= threshold].to_dict('records')
    filtered_list.append(other_row)

    other_df = pd.DataFrame(filtered_list)
    fig = px.pie(other_df, values='count', names='company_location', title=f'Company Location Pie Chart')
    return fig



if __name__ == '__main__':
    app.run(debug=True)
