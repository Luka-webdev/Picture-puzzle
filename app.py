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
    html.Label('Ekran powitalny'),
    dcc.Link('Przejdź dalej by wybrać obraz', href='/select')
])
select_img = html.Div([
    html.Label('Wybierz obraz'),
    dcc.Link('Przejdź dalej by zagrać', href='/game')
])
game = html.Div([
    html.Label('Witaj w grze'),
    dcc.Link('Wróć by zmienić obraz', href='/select')
])


@app.callback(
    Output('wrapper', 'children'),
    [Input('url', 'pathname')]
)
def show_pages(path):
    if path == '/select':
        return select_img
    elif path == '/game':
        return game
    else:
        return welcome_screen


if __name__ == '__main__':
    app.run_server(debug=True)
