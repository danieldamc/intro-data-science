'''Tamaño de la empresa y salario: Explore cómo el tamaño de la empresa empleadora
 (pequeña, mediana, grande) afecta los salarios de la ciencia de datos. 
 Determine si los científicos de datos que trabajan para empresas más grandes
 tienden a ganar salarios más altos en comparación con los de empresas más pequeñas.'''

from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv')
salaries_df = salaries_df.drop(columns=['Unnamed: 0'])

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Grafico de Barra', style={'textAlign':'center'}),
    dcc.Dropdown(salaries_df.company_location.unique(), 'US', id='company-dropdown'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    [Input('company-dropdown', 'value')]
)  

def update_graph(company):
    dff = salaries_df[(salaries_df["company_location"] == company)] 

    average_salary_per_size = dff.groupby(['work_year', 'company_size'])['salary_in_usd'].mean().reset_index()
    print(average_salary_per_size)

    
    fig = px.bar(average_salary_per_size, x='work_year', y='salary_in_usd', color='company_size', title=f'Average Salary per company size in {company}', barmode='group')

    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    fig.update_yaxes(range=[0, max(average_salary_per_size['salary_in_usd'])*1.1])
    fig.update_yaxes(tickmode='linear', dtick=50000)
    fig.update_layout(
        autosize=False,
        width=1600,
        height=600,
    )

    
    fig.update_xaxes(title_text="Work Year")
    fig.update_yaxes(title_text="Average Salary in USD")

    return fig

if __name__ == '__main__':
    app.run(debug=True)