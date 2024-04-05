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
    html.H1(children='Grafico de Linea', style={'textAlign':'center'}),
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
    
    fig = px.line(average_salary_per_year, x='work_year', y='salary_in_usd', color = 'experience_level', title=f'Average Salary Trend for {company}')
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    fig.update_yaxes(range=[0, average_salary_per_year['salary_in_usd'].max() + 20000])
    fig.update_yaxes(tickmode='linear', dtick=50000)
    fig.update_layout(
        autosize=False,
        width=1600,
        height=1000,
    )
    #add a title for axis
    fig.update_xaxes(title_text="Work Year")
    fig.update_yaxes(title_text="Average Salary in USD")

    return fig



if __name__ == '__main__':
    app.run(debug=True)
