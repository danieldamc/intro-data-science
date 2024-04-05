from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv')
salaries_df = salaries_df.drop(columns=['Unnamed: 0'])

# Impacto del tipo de empleo en los salarios: Explore cómo los tipos de empleo 
# (a tiempo parcial, a tiempo completo, por contrato, autónomo) influyen en los
# salarios. Analice si ciertos tipos de empleo tienden a ofrecer salarios más altos que otro.

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 3', style={'textAlign':'center'}),
    dcc.Dropdown(salaries_df.company_location.unique(), 'US', id='company-dropdown'),
    dcc.Graph(id='line-graph'),
    dcc.Graph(id='pie-graph'),
])

@callback(
    Output('line-graph', 'figure'),
    [Input('company-dropdown', 'value')]
)  
def update_graph(company):
    dff = salaries_df[(salaries_df["company_location"] == company)] 

    average_salary_per_year = dff.groupby(['work_year', 'employment_type'])['salary_in_usd'].mean().reset_index()
    
    fig = px.line(average_salary_per_year, x='work_year', y='salary_in_usd', color = 'employment_type', title=f'Average Salary Trend for {company}')
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

@app.callback(
    Output('pie-graph', 'figure'),
    [Input('company-dropdown', 'value')]
)
def update_pie_graph(company):
    dff = salaries_df[(salaries_df["company_location"] == company)] 
    type_count = pd.DataFrame(dff.employment_type.value_counts()).reset_index(inplace=False)

    fig = px.pie(type_count, values='count', names='employment_type', title=f'Employment Type for {company}')
    return fig      


if __name__ == '__main__':
    app.run(debug=True)