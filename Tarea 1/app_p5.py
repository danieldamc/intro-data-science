from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import numpy as np
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
    #dcc.Dropdown(salaries_df.company_location.unique(), 'US', id='company-dropdown'),
    dcc.Dropdown(np.concatenate([salaries_df.company_location.unique(), ['GLOBAL']]), 'GLOBAL', id='company-dropdown'),
    html.Div(children=[
        dcc.Graph(id='graph-content'),
        dcc.Graph(id='pie-graph'),
    ], style={'display':'flex'}),
])

@callback(
    Output('graph-content', 'figure'),
    [Input('company-dropdown', 'value')]
)  

def update_graph(company):
    if company != 'GLOBAL':
        dff = salaries_df[salaries_df["company_location"] == company]
    else:
        dff = salaries_df
    
    #dff = salaries_df[(salaries_df["company_location"] == company)] 

    average_salary_per_remote_ratio = dff.groupby(['remote_ratio'])['salary_in_usd'].mean().reset_index()
    fig = px.bar(average_salary_per_remote_ratio, x='remote_ratio', y='salary_in_usd')

    fig.update_yaxes(range=[0, average_salary_per_remote_ratio['salary_in_usd'].max() + 20000])
    fig.update_yaxes(tickmode='linear', dtick=50000)
    fig.update_layout(
        autosize=False,
        width=1100,
        height=720,
    )
    fig.update_layout(xaxis_type='category')
    
    fig.update_layout(title_text=f'Average Salary per Remote Ratio in {company}', title_x=0.5)

    
    fig.update_xaxes(title_text="Remote option")
    fig.update_yaxes(title_text="Average Salary in USD")
    #change color of the bars (blue, red, green)
    fig.update_traces(marker_color=['#ef553b', '#00cc96', '#636efa'])

    return fig

@app.callback(
    Output('pie-graph', 'figure'),
    [Input('company-dropdown', 'value')]
)
def update_pie_graph(company):
    
    if company != 'GLOBAL':
        dff = salaries_df[(salaries_df["company_location"] == company)]
    else:
        dff = salaries_df

    #dff = salaries_df[(salaries_df["company_location"] == company)] 
    type_count = pd.DataFrame(dff.remote_ratio.value_counts()).reset_index(inplace=False)

    fig = px.pie(type_count, values='count', names='remote_ratio', hole=.4)
    fig.update_layout(
        autosize=False,
        width=700,
        height=720,
    )
    
    fig.update_layout(title_text=f'Number of employees per remote option in {company}', title_x=0.5)

    list_colors = ['#636efa', '#ef553b', '#00cc96']
    fig.update_traces(marker=dict(colors=list_colors))
    
    return fig   

if __name__ == '__main__':
    app.run(debug=True)


