# Code source: https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Commented out is the original code:
# might need to play the video again 15:46   https://www.youtube.com/watch?v=ln8dyS2y4Nc&t=876s
# also might need to play with Dash tables

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
# sidebar div for the links to each page in the if-elif
sidebar = html.Div(
    [
        html.Center(html.Strong(html.H5("Edge Nav", className="display-6"))),
        html.Hr(),
        dbc.Nav(
            [
                html.Strong(dbc.NavLink("Crude Fin Charts - Brent", href="/", active="exact")),
                html.Strong(dbc.NavLink("Crude Fin Charts - WTI", href="/wti_charts", active="exact")),
                html.Strong(dbc.NavLink("Crude Fundamental", href="/cl_fund", active="exact")),
                html.Br(),
                html.Br(),
                html.Strong(dbc.NavLink("Nat Gas Fin Charts", href="/ng_charts", active="exact")),
                html.Strong(dbc.NavLink("NGLs Fin Charts", href="/ngl_charts", active="exact")),
                html.Strong(dbc.NavLink("NG Fundamental", href="/ng_fund", active="exact")),
                html.Br(),
                html.Br(),
                html.Strong(dbc.NavLink("Products Fundamental", href="/prod_fund", active="exact")),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


# PUT ALL IFRAMES INTO A DIV TO MAKE RESPONSIVE
# this is what is in the wordpress site - need to translate to Dash:
# <div style="border-radius: 20px 20px 40px 40px; overflow: hidden;">
# <iframe width="600" height="500" framework="0" scrolling="no"
# src="//plotly.com/~bpieri/1728.embed?autosize=true&link=false"></iframe></div>

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [html.Div([html.Iframe('Brent Candlestick',
                                      src='//plotly.com/~bpieri/1730.embed?autosize=true&link=false',
                                      height="600px",
                                      width="80%",
                                      style={'textAlign': 'center', })]),
                html.Div([html.Iframe('Brent Forward',
                                      src='//plotly.com/~bpieri/913.embed?autosize=true&link=false',
                                      height="600px",
                                      width="80%",
                                      style={'textAlign': 'center', })]),
                html.Div([html.Iframe('Brent Pivot',
                                      src='//plotly.com/~bpieri/715.embed?autosize=true&link=false',
                                      height="600px",
                                      width="80%",
                                      style={'textAlign': 'center', })]),
                html.Div([html.Iframe('Brent Long Term',
                                      src='//plotly.com/~bpieri/1518.embed?autosize=true&link=false',
                                      height="600px",
                                      width="80%",
                                      style={'textAlign': 'center', })]),

                ]
    elif pathname == "/wti_charts":
        return [
            html.Iframe('WTI Candlestick',
                        src='//plotly.com/~bpieri/1728.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('WTI Forward',
                        src='//plotly.com/~bpieri/929.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('WTI Pivot',
                        src='//plotly.com/~bpieri/711.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Brent-WTI Long Term',
                        src='//plotly.com/~bpieri/1547.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('WTI Long Term',
                        src='//plotly.com/~bpieri/1508.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),

        ]
    elif pathname == "/cl_fund":
        return [
            html.Iframe('Crude Refining',
                        src='//plotly.com/~bpieri/455.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Crude Commercial Stocks',
                        src='//plotly.com/~bpieri/453.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Crude SPR Stocks',
                        src='//plotly.com/~bpieri/449.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Crude & Products Stocks',
                        src='//plotly.com/~bpieri/456.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Crude Fundamental Table',
                        src='//plotly.com/~bpieri/1217.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
        ]

    elif pathname == "/ng_charts":
        return [
            html.Iframe('NG Candlestick',
                        src='//plotly.com/~bpieri/1732.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('NG Forward',
                        src='//plotly.com/~bpieri/915.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('NG Pivot',
                        src='//plotly.com/~bpieri/708.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('NG Long Term',
                        src='//plotly.com/~bpieri/1512.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
        ]
    elif pathname == "/ngl_charts":
        return [
            html.Iframe('NGLs % WTI',
                        src='//plotly.com/~bpieri/1535.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Ethane Long Term',
                        src='//plotly.com/~bpieri/1527.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Propane Long Term',
                        src='//plotly.com/~bpieri/1525.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Isobutane Long Term',
                        src='//plotly.com/~bpieri/1523.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Normal Butane Long Term',
                        src='//plotly.com/~bpieri/1529.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Natural Gasoline Long Term',
                        src='//plotly.com/~bpieri/1531.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
        ]
    elif pathname == "/ng_fund":
        return [
            html.Iframe('NG Storage',
                        src='//plotly.com/~bpieri/441.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('NG Supply Demand',
                        src='//plotly.com/~bpieri/460.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('LNG Import Export',
                        src='//plotly.com/~bpieri/454.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Pipe Import Export',
                        src='//plotly.com/~bpieri/452.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
        ]
    elif pathname == "/prod_fund":
        return [
            html.Iframe('Motor Gas Stocks',
                        src='//plotly.com/~bpieri/445.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Distillate Stocks',
                        src='//plotly.com/~bpieri/447.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Residual Fuel Oil',
                        src='//plotly.com/~bpieri/450.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Other Oils Stocks',
                        src='//plotly.com/~bpieri/458.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Fuel Ethanol Stocks',
                        src='//plotly.com/~bpieri/448.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Propane Propylene Stocks',
                        src='//plotly.com/~bpieri/457.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
            html.Iframe('Kerosene Jet Fuel',
                        src='//plotly.com/~bpieri/450.embed?autosize=true&link=false',
                        height="600px",
                        width="80%",
                        style={'textAlign': 'center'}),
        ]

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
