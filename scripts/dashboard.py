import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

# Laden der Excel-Daten
file_path = '/data/bereinigte_daten.xlsx'
df = pd.read_excel(file_path)

# Beibehalten der kategorischen Merkmale als Strings
df['country'] = df['country'].astype('category')
df['PSP'] = df['PSP'].astype('category')
df['card'] = df['card'].astype('category')

# Layout des Dashboards
app.layout = html.Div([
    html.H1("Kreditkarten Transaktionsvorhersage Dashboard"),

    dcc.Tabs([
        dcc.Tab(label='Modellleistung', children=[
            html.Div([
                html.H2("Erfolgsrate der Transaktionen"),
                dcc.Graph(id='success-rate-graph')
            ]),
            html.Div([
                html.H2("Modellmetriken"),
                dcc.Graph(id='model-metrics-graph')
            ])
        ]),
        dcc.Tab(label='Kosteneinsparungen', children=[
            html.Div([
                html.H2("Kosteneinsparungen vor und nach Einführung des Modells"),
                dcc.Graph(id='cost-savings-graph')
            ]),
            html.Div([
                html.H2("Prognose zukünftiger Kosten"),
                dcc.Graph(id='cost-forecast-graph')
            ])
        ]),
        dcc.Tab(label='Transaktionsanalyse', children=[
            html.Div([
                html.H2("Transaktionsanalyse nach Kategorien"),
                dcc.Graph(id='transaction-analysis-graph')
            ])
        ])
    ]),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])

# Callback für die Graphen
@app.callback(
    Output('success-rate-graph', 'figure'),
    Output('model-metrics-graph', 'figure'),
    Output('cost-savings-graph', 'figure'),
    Output('cost-forecast-graph', 'figure'),
    Output('transaction-analysis-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graphs(n_intervals):
    # Erfolgsrate
    success_rate_fig = px.bar(df.groupby('PSP')['success'].mean().reset_index(), 
                              x='PSP', y='success', 
                              title='Erfolgsrate der Transaktionen nach PSP', 
                              labels={'PSP': 'PSP', 'success': 'Erfolgsrate'})

    # Modellmetriken (Dummy-Daten, da reale Modellmetriken nicht verfügbar)
    metrics_data = pd.DataFrame({
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
        'Value': [0.8, 0.75, 0.7, 0.72]
    })
    model_metrics_fig = px.bar(metrics_data, x='Metric', y='Value', title='Modellmetriken', labels={'Metric': 'Metrik', 'Value': 'Wert'})

    # Kosteneinsparungen
    cost_savings_fig = px.line(df.groupby('country')['amount'].sum().reset_index(), 
                               x='country', y='amount', 
                               title='Kosteneinsparungen vor und nach Einführung des Modells', 
                               labels={'country': 'Land', 'amount': 'Gesamtbetrag'})

    # Kostenprognose (Dummy-Daten)
    cost_forecast_fig = px.line(df.groupby('country')['amount'].mean().reset_index(), 
                                x='country', y='amount', 
                                title='Prognose zukünftiger Kosten', 
                                labels={'country': 'Land', 'amount': 'Durchschnittlicher Betrag'})

    # Transaktionsanalyse
    transaction_analysis_fig = px.scatter(df, 
                                          x='amount', y='success', 
                                          color='PSP', 
                                          title='Transaktionsanalyse nach Kategorien', 
                                          labels={'amount': 'Betrag', 'success': 'Erfolg', 'PSP': 'PSP'},
                                          hover_data=['country', 'card', '3D_secured'])

    return success_rate_fig, model_metrics_fig, cost_savings_fig, cost_forecast_fig, transaction_analysis_fig

if __name__ == '__main__':
    app.run_server(debug=True)