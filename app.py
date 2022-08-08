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
    html.Div([
        html.Div([
            html.Div([
                html.P(id='title1', children="Pic"),
                html.P(id='title2', children="ture"),
                html.P(id='title3', children="  Puz"),
                html.P(id='title4', children="zle"),
            ], id='logo'),
            dcc.Link('Start', href='/select', id='link')
        ], id='welcomeScreen'),
        html.Div([
            html.Div([
                html.H1('Load the image'),
                html.Div(id='arrow'),
                dcc.Upload(html.A('click here'), id='load')
            ], id='loadArea'),
            html.Div(id='picture'),
        ], id='game')
    ], id='wrapper')
])


def divide_picture(img):
    height, width, _ = img.shape
    global unit_width
    unit_width = width//3
    global unit_height
    unit_height = height//3
    coordinatesX = [int(width/3*i) for i in range(4)]
    coordinatesY = [int(height/3*i) for i in range(4)]
    for i in range(3):
        for j in range(3):
            image = img[coordinatesY[i]:coordinatesY[i+1],
                        coordinatesX[j]:coordinatesX[j+1]]
            picture_parts.append(image)
    random.shuffle(picture_parts)


def position_indicators():
    for i in range(8):
        indicator = (i % 3, i//3)
        listOfIndicators.append(indicator)


@app.callback(
    Output('picture', 'children'),
    [Input('load', 'contents')]
)
def load_picture(contents):
    screen = get_monitors()[0]
    if len(listOfIndicators) > 0:
        listOfIndicators.clear()
        picture_parts.clear()
    if contents != None:

        img = base64.b64decode(contents.split(",")[1])
        img = np.frombuffer(img, dtype=np.uint8)
        img = cv2.imdecode(img, flags=1)
        img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
        imgPreview = imutils.resize(image=img, width=int(screen.width*0.15))
        if screen.width > screen.height:
            if screen.width > 1000:
                img = imutils.resize(image=img, width=int(screen.width*0.6))
                divide_picture(img)
                position_indicators()
            elif (screen.width > 700 and screen.width < 1000):
                img = imutils.resize(image=img, width=int(screen.width*0.7))
                divide_picture(img)
                position_indicators()
            elif (screen.width > 400 and screen.width < 700):
                img = imutils.resize(image=img, width=int(screen.width*0.8))
                divide_picture(img)
                position_indicators()
            elif screen.width < 400:
                img = imutils.resize(image=img, width=int(screen.width*0.9))
                divide_picture(img)
                position_indicators()
        elif screen.width < screen.height:
            if screen.height > 1000:
                img = imutils.resize(image=img, height=int(screen.height*0.6))
                divide_picture(img)
                position_indicators()
            elif (screen.height > 700 and screen.height < 1000):
                img = imutils.resize(image=img, height=int(screen.height*0.7))
                divide_picture(img)
                position_indicators()
            elif (screen.height > 400 and screen.height < 700):
                img = imutils.resize(image=img, height=int(screen.height*0.8))
                divide_picture(img)
                position_indicators()
            elif screen.height < 400:
                img = imutils.resize(image=img, height=int(screen.height*0.9))
                divide_picture(img)
                position_indicators()
        return [html.Div([html.Div([html.Img(src=im.fromarray(picture_parts[i]))], id=str(i), className="pictureParts", style={'position': 'absolute', 'left': listOfIndicators[i][0]*unit_width, 'top':listOfIndicators[i][1]*unit_height}) for i in range(8)], id='loadedPicture', style={'width': img.shape[1], 'height': img.shape[0]}), html.Details([html.Summary('Preview'), html.Img(src=im.fromarray(imgPreview))], id='view'), html.Button(id='newImg', children='Load new image')]


@app.callback(
    Output('load', 'contents'),
    [Input('newImg', 'n_clicks')]
)
def clearContent(btn):
    return


if __name__ == '__main__':
    app.run_server(debug=True)
