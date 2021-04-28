import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from django.utils import timezone
from datetime import datetime

from django_plotly_dash import DjangoDash


def prices(file_path):
    external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

    current_year = datetime.date.today().year
    

    app = DjangoDash('PriceHistory', external_stylesheets=external_stylesheets)

    df = pd.read_csv(file_path)

    x = df['DATE'].to_list()
    y = df['PRICE'].to_list()

    fig = px.line(df, x, y)

    colors = {
        'background': 'black',
        'paper': 'black',
        'text': 'navajowhite'
    }

    fig.update_layout(
    plot_bgcolor=colors['background'], # background
    paper_bgcolor=colors['paper'],     # graph area
    font_color=colors['text']          # text
)

    app.layout = html.Div([
        dcc.Graph(
            id='graph-1',
            figure=fig
        )
    ])

    return app
