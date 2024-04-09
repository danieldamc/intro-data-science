from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd
import numpy as np

salaries_df = pd.read_csv('Salaries.csv', index_col=0)
n_countries = salaries_df.company_location.nunique()

"""
Tendencias salariales a lo largo del tiempo: Analice cómo han evolucionado los salarios en 
ciencia de datos a lo largo de los años examinando la distribución de los salarios en 
diferentes años laborales. Identifique cualquier tendencia o patrón significativo en el crecimiento o disminución del salario a lo largo del tiempo.
"""

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 1', style={'textAlign':'center'}),
    html.P(children='Tendencias salariales a lo largo del tiempo: Analice cómo han evolucionado los salarios en ciencia de datos a lo largo de los años examinando la distribución de los salarios en diferentes años laborales. Identifique cualquier tendencia o patrón significativo en el crecimiento o disminución del salario a lo largo del tiempo.', style={'textAlign':'center'}),
    dcc.Dropdown(np.concatenate([salaries_df.experience_level.unique(), ['ALL']]), 'ALL', id='exp-dropdown'),
    
    #dcc.Slider(0, n_countries, 1, value=10, marks={0:{'label':'0'}, 20:{'label':'20'}}, tooltip={"placement": "bottom", "always_visible": True}, id='threshold-slider'),
    dcc.Graph(id='graph-content')
])


@callback(
    Output('graph-content', 'figure'),
    [Input('exp-dropdown', 'value')]
)  
def update_graph(experience_level):

    if experience_level != 'ALL':
        dff = salaries_df[salaries_df["experience_level"] == experience_level]
    else:
        dff = salaries_df

    average_salary_global = dff.groupby(['work_year'])['salary_in_usd'].mean().reset_index()
    average_salary_global["employee_residence"] = ["Global" for i in range(len(average_salary_global))]
    average_salary_global = average_salary_global.to_dict('records')
    #filter average_salary_per_country
    df = dff.groupby(['work_year', 'employee_residence'])['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=False)
    filtered_df = df.groupby('employee_residence').filter(lambda x: len(x) >= 3).reset_index(drop=True)

    average_salary_per_country = filtered_df.groupby(['employee_residence'])['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=False)
    #get top 5 countries and bottom 5 countries
    average_salary_per_country = average_salary_per_country.head(5)["employee_residence"].to_list() + average_salary_per_country.tail(5)["employee_residence"].to_list()
    average_salary_per_country = dff[dff['employee_residence'].isin(average_salary_per_country)].groupby(['employee_residence', 'work_year'])['salary_in_usd'].mean().reset_index().to_dict('records')
    dfff = average_salary_per_country + average_salary_global
    dfff = pd.DataFrame(dfff)

    
    fig = px.line(dfff, x='work_year', y='salary_in_usd', color="employee_residence",markers=True, title=f'Average Salary Trend globally')
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    fig.update_yaxes(range=[0, dfff['salary_in_usd'].max() + 20000])
    fig.update_yaxes(tickmode='linear', dtick=50000)
    fig.update_layout(
        autosize=False,
        width=1800,
        height=720,
    )
    #add a title for axis
    fig.update_xaxes(title_text="Work Year")
    fig.update_yaxes(title_text="Average Salary in USD")

    return fig



if __name__ == '__main__':
    app.run(debug=True)
