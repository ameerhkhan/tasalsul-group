# https://plotly.com/python/time-series/

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from django.utils import timezone
from datetime import datetime

from django_plotly_dash import DjangoDash


def prices(product_df):
    external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

    # current_year = datetime.date.today().year
    # current_year = datetime.now().year
    current_year = datetime.today().year
    
    df_test = pd.read_csv('pricing/assets/historical_pricing.csv')

    app = DjangoDash('PriceHistory', external_stylesheets=external_stylesheets)

    # df = product_df.copy()
    df = df_test.copy()

    x = df['DATE'].to_list()
    y = df['PRICE'].to_list()

    fig = px.line(df, x, y)
    # Use date string to set xaxis range (for manually selecting range.)
    # fig.update_layout(xaxis_range=['2016-07-01','2016-12-31'],
    #               title_text="Manually Set Date Range")

    # can also use area chart which is more aesthetically pleasing.

    # df = px.data.stocks(indexed=True)-1
    # fig = px.area(df, facet_col="company", facet_col_wrap=2)
    
    # fig = px.area(df, x, y, hover_data=y, facet_col_wrap=2)


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

    # for the range slider..
    # fig.update_xaxes(rangeslider_visible=True)

#     Or if you want buttons for month, year etc,
#     fig.update_xaxes(
#     rangeslider_visible=True,
#     rangeselector=dict(
#         buttons=list([
#             dict(count=1, label="1m", step="month", stepmode="backward"),
#             dict(count=6, label="6m", step="month", stepmode="backward"),
#             dict(count=1, label="YTD", step="year", stepmode="todate"),
#             dict(count=1, label="1y", step="year", stepmode="backward"),
#             dict(step="all")
#         ])
#     )
# )

    app.layout = html.Div([
        dcc.Graph(
            id='graph-1',
            figure=fig
        )
    ])

    return app
