import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='wrapper')
])

welcome_screen = html.Div([
    html.Div([
        html.P(id='title1', children="Pic"),
        html.P(id='title2', children="ture"),
        html.P(id='title3', children=" Puz"),
        html.P(id='title4', children="zle"),
    ], id='logo'),
    dcc.Link('Dalej', href='/select', id='link')
], id='welcomeScreen')

select_img = html.Div([
    html.Label('Wybierz obraz'),
])


@app.callback(
    Output('wrapper', 'children'),
    [Input('url', 'pathname')]
)
def show_pages(path):
    if path == '/select':
        return select_img
    else:
        return welcome_screen


if __name__ == '__main__':
    app.run_server(debug=True)
