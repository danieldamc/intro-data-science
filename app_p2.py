from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv', index_col=0)

"""
Disparidades salariales entre niveles de experiencia: Investigue la relación entre los niveles de experiencia 
(nivel inicial, nivel medio, nivel superior, nivel ejecutivo) y los salarios para cada nivel de experiencia. 
Compare los salarios promedio para cada nivel de experiencia.
"""

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 2', style={'textAlign':'center'}),
    html.P(children='Disparidades salariales entre niveles de experiencia: Investigue la relación entre los niveles de experiencia (nivel inicial, nivel medio, nivel superior, nivel ejecutivo) y los salarios para cada nivel de experiencia. Compare los salarios promedio para cada nivel de experiencia.', style={'textAlign':'center'}),
    dcc.Dropdown(salaries_df.company_location.unique(), 'US', id='company-dropdown'),
    dcc.Graph(id='graph-content')
])


@callback(
    Output('graph-content', 'figure'),
    [Input('company-dropdown', 'value')]
)  
def update_graph(company):
    dff = salaries_df[(salaries_df["company_location"] == company)] 

    #print(dff[['work_year', 'salary_in_usd']])

    average_salary_per_year = dff.groupby(['work_year', 'experience_level'])['salary_in_usd'].mean().reset_index()
    
    fig = px.line(average_salary_per_year, x='work_year', y='salary_in_usd', color = 'experience_level', markers=True)
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    fig.update_yaxes(range=[0, average_salary_per_year['salary_in_usd'].max() + 20000])
    fig.update_yaxes(tickmode='linear', dtick=50000)
    fig.update_layout(
        autosize=False,
        width=1800,
        height=720,
    )
    #add a title for axis
    fig.update_xaxes(title_text="Work Year")
    fig.update_yaxes(title_text="Average Salary in USD")
    fig.update_layout(title_text=f'Average Salary Trend per experience level in {company}', title_x=0.5)

    return fig



if __name__ == '__main__':
    app.run(debug=True)
