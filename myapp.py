import dash
from dash import Dash,dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load gapminder dataset
df = pldata.gapminder()

# Create Series of unique countries
countries = df['country'].unique()

# Initialize Dash app
app = Dash(__name__)
server = app.server # <-- This is the line you need to add

app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in countries],
        value='Canada',  # initial value
        clearable=False
    ),
    dcc.Graph(id='gdp-growth')
])

# Callback to update graph based on selected country
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    # Filter dataframe by selected country
    filtered_df = df[df['country'] == selected_country]

    # Create line plot
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f'GDP Per Capita Over Time for {selected_country}',
        labels={'year': 'Year', 'gdpPercap': 'GDP Per Capita'}
    )

    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 