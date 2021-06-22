# https://plotly.com/python/time-series/

import pandas as pd
import plotly.express as px
# from django.utils import timezone
# from datetime import datetime

# from django_plotly_dash import DjangoDash


def prices(product_name):
    df = pd.read_csv('pricing/assets/historical_pricing.csv')
    df_copy = df.copy()

    product_df = df_copy.loc[df['NAME'] == product_name]
    x = product_df['DATE'].to_list()
    y = product_df['PRICE'].to_list()

    # fig = px.line(df, x, y)

    fig = px.area(df, x="DATE", y="PRICE")

    # https://plotly.com/python/reference/layout/#layout-paper_bgcolor

    colors = {
    'background': 'rgba(0,0,0,0)',
    'paper': 'rgba(0,0,0,0)',
    'text': 'black',
    'colorway': 'red'
    }
    fig.update_layout(
    plot_bgcolor=colors['background'], # background
    paper_bgcolor=colors['paper'],     # graph area total div
    font_color=colors['text'],         # text
    colorway=(colors['colorway'], colors['colorway'])
    )

    fig.update_traces(line_color='red')
    fig.update_xaxes(rangeslider_visible=True)

    return fig