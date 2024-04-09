from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

'''
Trabajo Remoto y Salario: Investigar la relación entre el alcance del trabajo remoto 
(sin trabajo remoto, parcialmente remoto, totalmente remoto) y los salarios. 
Analice si las personas que trabajan de forma remota tienden a ganar más o menos
en comparación con quienes trabajan en entornos de oficina tradicionales.
'''

salaries_df = pd.read_csv('Salaries.csv', index_col=0)
app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 5', style={'textAlign':'center'}),
    html.P(children='Trabajo Remoto y Salario: Investigar la relación entre el alcance del trabajo remoto (sin trabajo remoto, parcialmente remoto, totalmente remoto) y los salarios. Analice si las personas que trabajan de forma remota tienden a ganar más o menos en comparación con quienes trabajan en entornos de oficina tradicionales.', style={'textAlign':'center'}),
    dcc.Dropdown(salaries_df.company_location.unique(), 'US', id='company-dropdown'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    [Input('company-dropdown', 'value')]
)  

def update_graph(company):
    dff = salaries_df[(salaries_df["company_location"] == company)] 

    average_salary_per_remote_ratio = dff.groupby(['work_year', 'remote_ratio'])['salary_in_usd'].mean().reset_index()
    print(average_salary_per_remote_ratio)

    #get sum of salary_in_usd for each work_year
    sum_of_salaries = []

    for year in average_salary_per_remote_ratio['work_year'].unique():
        sum_of_salaries.append(average_salary_per_remote_ratio[average_salary_per_remote_ratio['work_year'] == year]['salary_in_usd'].sum())

    print(sum_of_salaries)
    
    fig = px.bar(average_salary_per_remote_ratio, x='work_year', y='salary_in_usd', color='remote_ratio', title=f'Average Salary per Remote Ratio for {company}', barmode='group')

    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    fig.update_yaxes(range=[0, max(sum_of_salaries)*1.1])
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


