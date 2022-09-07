import pandera as pa
import plotly.express as px
import sys, os

from dash import Dash, html, dcc, Input, Output
from dash.dash_table import DataTable
from pandera.typing import DataFrame
from typing import List, Optional


#Following lines are for assigning parent directory dynamically.
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
pp_dir_path = os.path.abspath(os.path.join(parent_dir_path, os.pardir))
sys.path += [parent_dir_path, pp_dir_path]


from clients.CoinGeckoClient import CoinGeckoClient
from schemas.DailyMarketSchema import DailyMarketSchema


""" Script Parameters
"""

SUBSET_ID = "adaxtz"
NUMBER_OF_DAYS = 30
METRICS = ["prices", "total_volumes", "market_caps"]

###################


# visit http://127.0.0.1:8050/ to visualize the report
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Create Client
client_usd = CoinGeckoClient(SUBSET_ID, "usd")

# Get market data
df_market = client_usd.daily_market_data(NUMBER_OF_DAYS, metrics=METRICS)


@pa.check_types
def dashboard_daily_market(
    dataframe: DataFrame[DailyMarketSchema],
    metrics: Optional[List[str]] = None
) -> html.Div:
    """Return dashboard with Data Quality metrics on a daily_market DataFrame.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        A dataframe that is validated using schemas.DailarketSchema
    """
    bottom_table = dataframe[dataframe["dates"] == dataframe["dates"].max()]

    assets = dataframe["asset_name"].unique()

    return html.Div(children=[
        html.H1(children='Data Quality Report'),
        html.Div([
            html.Div(
                dcc.Dropdown(
                    metrics, 
                    "prices", 
                    id='filter-metric',
                    clearable=False,
                    placeholder="Select a metric"
                ), style={'width': '20%', 'display': 'inline-block'}
            ),
            html.Div(
                dcc.Dropdown(
                    assets, 
                    assets[0], 
                    id='filter-asset',
                    clearable=False,
                    placeholder="Select an asset"
                ), style={'width': '20%', 'display': 'inline-block'})
        ]),
        dcc.Graph(id="metric_line_chart"),
        DataTable(bottom_table.to_dict('records'))
    ])

@app.callback(
    Output("metric_line_chart", "figure"),
    Input("filter-metric", "value"),
    Input("filter-asset", "value"))
def update_metric_line_chart(metric: str, asset: str):
    df = df_market[["dates", "asset_name", metric]]
    df = df[df["asset_name"] == asset].sort_values(by=["dates"])
    fig = px.line(
        df,
        x="dates", y=metric,
        color="asset_name",
        labels = {
            "dates": "Date",
            metric: f"{metric} ($USD)"
        }
    )
    return fig


if __name__ == "__main__":
    # Generate and deploy Data Quality report
    app.layout = dashboard_daily_market(df_market, metrics=METRICS)
    app.run_server(debug=True)
