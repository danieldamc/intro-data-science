from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import numpy as np
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv', index_col=0)

"""
Disparidades salariales regionales: Examine cómo varían los salarios entre las diferentes 
residencias de los empleados y las ubicaciones de las empresas (países). 
Identifique regiones/países donde los científicos de datos tienden a ganar salarios más altos en comparación con otros.
"""

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 4', style={'textAlign':'center'}),
    html.P(children='Disparidades salariales regionales: Examine cómo varían los salarios entre las diferentes residencias de los empleados y las ubicaciones de las empresas (países). Identifique regiones/países donde los científicos de datos tienden a ganar salarios más altos en comparación con otros.', style={'textAlign':'center'}),
    #dcc.Dropdown(salaries_df.experience_level.unique(), 'MI', id='ex-dropdown'),
    dcc.Dropdown(np.concatenate([salaries_df.experience_level.unique(), ['ALL']]), 'ALL', id='ex-dropdown'),
    # change slider to a top n
    html.Div(children=[dcc.Graph(id='company-bar-graph'), dcc.Graph(id='company-pie-graph')], style={'display':'flex'}),
    html.Div(children=[dcc.Graph(id='residence-bar-graph'), dcc.Graph(id='residence-pie-graph')], style={'display':'flex'}),
])


@callback(
    Output('company-bar-graph', 'figure'),
    [Input('ex-dropdown', 'value')]
)  
def update_company_bar_graph(experience_level):
    if experience_level != 'ALL':
        dff = salaries_df[(salaries_df["experience_level"] == experience_level)]
    else:
        dff = salaries_df
    #dff = salaries_df[(salaries_df["experience_level"] == experience_level)]

    average_salary_company_location = dff.groupby(['company_location'])['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=False)

    fig = px.histogram(average_salary_company_location, y='salary_in_usd', x='company_location')
    fig.update_layout(title_text=f'Company Location Bar Chart', title_x=0.5)
    fig.update_xaxes(title_text="Company Location")
    fig.update_yaxes(title_text="Average Salary in USD")

    fig.update_layout(
        autosize=False,
        width=1200,
        height=360,
    )
    return fig

@callback(
    Output('company-pie-graph', 'figure'),
    [Input('ex-dropdown', 'value')]
)  
def update_company_pie_graph(experience_level):

    if experience_level != 'ALL':
        dff = salaries_df[(salaries_df["experience_level"] == experience_level)]
    else:
        dff = salaries_df

    #dff = salaries_df[(salaries_df["experience_level"] == experience_level)]
    count_df = pd.DataFrame(dff.company_location.value_counts()).reset_index(inplace=False)

    other_count = count_df[count_df['count'] < 4]['count'].sum()

    other_row = {'company_location': 'OTHER', 'count': other_count}
    filtered_list = count_df[count_df['count'] >= 4].to_dict('records')
    filtered_list.append(other_row)

    other_df = pd.DataFrame(filtered_list)
    fig = px.pie(other_df, values='count', names='company_location')
    fig.update_layout(title_text=f'Company Location Pie Chart', title_x=0.5)
    fig.update_layout(
        autosize=False,
        width=500,
        height=360,
    )
    return fig

@callback(
    Output('residence-bar-graph', 'figure'),
    [Input('ex-dropdown', 'value')]
)  
def update_residence_bar_graph(experience_level):
    
    if experience_level != 'ALL':
        dff = salaries_df[(salaries_df["experience_level"] == experience_level)]
    else:
        dff = salaries_df
    #dff = salaries_df[(salaries_df["experience_level"] == experience_level)]

    average_salary_residence = dff.groupby(['employee_residence'])['salary_in_usd'].mean().reset_index().sort_values(by='salary_in_usd', ascending=False)

    fig = px.histogram(average_salary_residence, y='salary_in_usd', x='employee_residence')
    
    #style
    fig.update_layout(title_text=f'Employee Residence Bar Chart', title_x=0.5)
    
    fig.update_xaxes(title_text="Employee Residence")
    fig.update_yaxes(title_text="Average Salary in USD")
    fig.update_layout(
        autosize=False,
        width=1200,
        height=360,
    )
    return fig

@callback(
    Output('residence-pie-graph', 'figure'),
    [Input('ex-dropdown', 'value')]
)  
def update_residence_pie_graph(experience_level):

    if experience_level != 'ALL':
        dff = salaries_df[(salaries_df["experience_level"] == experience_level)]
    else:
        dff = salaries_df

    #dff = salaries_df[(salaries_df["experience_level"] == experience_level)]
    count_df = pd.DataFrame(dff.employee_residence.value_counts()).reset_index(inplace=False)

    other_count = count_df[count_df['count'] < 4]['count'].sum()

    other_row = {'employee_residence': 'OTHER', 'count': other_count}
    filtered_list = count_df[count_df['count'] >= 4].to_dict('records')
    filtered_list.append(other_row)

    other_df = pd.DataFrame(filtered_list)
    fig = px.pie(other_df, values='count', names='employee_residence')

    #style
    fig.update_layout(title_text=f'Employee Residence Pie Chart', title_x=0.5)
    fig.update_xaxes(title_text="Employee Residence")
    fig.update_yaxes(title_text="Average Salary in USD")
    fig.update_layout(
        autosize=False,
        width=500,
        height=360,
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)
