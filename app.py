from cmath import pi
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import numpy as np
import cv2
import base64
from PIL import Image as im
import imutils
import random
from screeninfo import get_monitors

external_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Titan+One&display=swap",
    "https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap",
    "https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap"
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
picture_parts = []
listOfIndicators = []

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='wrapper')
])

welcome_screen = html.Div([
    html.Div([
        html.P(id='title1', children="Pic"),
        html.P(id='title2', children="ture"),
        html.P(id='title3', children="  Puz"),
        html.P(id='title4', children="zle"),
    ], id='logo'),
    dcc.Link('Dalej', href='/select', id='link')
], id='welcomeScreen')

select_img = html.Div([
    html.Div([
        html.H1('Wczytaj obraz'),
        html.Div(id='arrow'),
        dcc.Upload(html.A('Kliknij tutaj'), id='load')
    ], id='loadArea'),
    html.Div(id='picture')
], id='game')


def divide_picture(img):
    height, width, _ = img.shape
    global unit_width
    unit_width = width//4
    global unit_height
    unit_height = height//4
    coordinatesX = [int(width/4*i) for i in range(5)]
    coordinatesY = [int(height/4*i) for i in range(5)]
    for i in range(4):
        for j in range(4):
            image = img[coordinatesY[i]:coordinatesY[i+1],
                        coordinatesX[j]:coordinatesX[j+1]]
            picture_parts.append(image)
    random.shuffle(picture_parts)


def position_indicators():
    for i in range(15):
        indicator = (i % 4, i//4)
        listOfIndicators.append(indicator)


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

    if contents != None:
        img = base64.b64decode(contents.split(",")[1])
        img = np.frombuffer(img, dtype=np.uint8)
        img = cv2.imdecode(img, flags=1)
        img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
        if screen.width > screen.height:
            if screen.width > 1000:
                img = imutils.resize(image=img, width=int(screen.width*0.6))
                divide_picture(img)
                position_indicators()
            elif (screen.width > 700 and screen.width < 1000):
                img = imutils.resize(image=img, width=int(screen.width*0.7))
            elif (screen.width > 400 and screen.width < 700):
                img = imutils.resize(image=img, width=int(screen.width*0.8))
            elif screen.width < 400:
                img = imutils.resize(image=img, width=int(screen.width*0.9))
        elif screen.width < screen.height:
            if screen.height > 1000:
                img = imutils.resize(image=img, height=int(screen.height*0.6))
            elif (screen.height > 700 and screen.height < 1000):
                img = imutils.resize(image=img, height=int(screen.height*0.7))
            elif (screen.height > 400 and screen.height < 700):
                img = imutils.resize(image=img, height=int(screen.height*0.8))
            elif screen.height < 400:
                img = imutils.resize(image=img, height=int(screen.height*0.9))
        return html.Div([html.Img(src=im.fromarray(picture_parts[i]), id=str(i), className="pictureParts", style={'position': 'absolute', 'left': listOfIndicators[i][0]*unit_width, 'top':listOfIndicators[i][1]*unit_height}) for i in range(15)], id='loadedPicture', style={'width': img.shape[1], 'height': img.shape[0]})


if __name__ == '__main__':
    app.run_server(debug=True)
