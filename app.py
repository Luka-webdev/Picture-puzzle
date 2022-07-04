import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import numpy as np
import cv2
import base64
from PIL import Image as im
import imutils
from screeninfo import get_monitors

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
    html.Div([
        html.H1('Wczytaj obraz'),
        html.P('^'),
        dcc.Upload(html.A('Kliknij tutaj'), id='load')
    ], id='loadArea'),
    html.Div(id='picture')
], id='game')


@app.callback(
    Output('wrapper', 'children'),
    [Input('url', 'pathname')]
)
def show_pages(path):
    if path == '/select':
        return select_img
    else:
        return welcome_screen


@app.callback(
    Output('picture', 'children'),
    [Input('load', 'contents')]
)
def load_picture(contents):
    screen = get_monitors()[0]
    print(screen)
    if contents != None:
        img = base64.b64decode(contents.split(",")[1])
        img = np.frombuffer(img, dtype=np.uint8)
        img = cv2.imdecode(img, flags=1)
        width, height, _ = img.shape
        print(img.shape)
        # img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
        # img = imutils.resize(image=img, width=500)
        print(img.shape)
        return html.Img(src=im.fromarray(img), id='loadedPicture')


if __name__ == '__main__':
    app.run_server(debug=True)
