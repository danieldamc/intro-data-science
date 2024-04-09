from dash import Dash, html, dash_table, callback, Output, Input, dcc
import plotly.express as px
import pandas as pd

salaries_df = pd.read_csv('Salaries.csv', index_col=0)

'''
Explore dos parámetros de interés de manera libre y haga correlaciones.
ver proporcion de remote en casos donde el sujeto vive en el mismo lugar que el centro de trabajo
'''

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pregunta 10', style={'textAlign':'center'}),
    html.P(children='Explore dos parámetros de interés de manera libre y haga correlaciones.', style={'textAlign':'center'}),
    dcc.Dropdown(salaries_df.company_location.unique(), 'US', id='company-dropdown'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    [Input('company-dropdown', 'value')]
)  

def update_graph(company):
    dff = salaries_df[(salaries_df["company_location"] == company)]
    dfff = dff.groupby(['experience_level', 'company_size']).size().reset_index(name='value').sort_values(by='company_size', ascending=False)
    print(dfff)
    fig = px.bar(dfff, x='company_size', y='value', color='experience_level', barmode='group')
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    fig.update_yaxes(range=[0, dfff['value'].max()*1.1])
    fig.update_yaxes(tickmode='linear', dtick=10)
    fig.update_layout(
        autosize=False,
        width=1700,
        height=720,
    )
    fig.update_xaxes(title_text="Company Size")
    fig.update_yaxes(title_text="Number of employees")
    fig.update_layout(title_text=f'Number of employees per company size and experience level in {company}', title_x=0.5)

    return fig

    
    

if __name__ == '__main__':
    app.run(debug=True)