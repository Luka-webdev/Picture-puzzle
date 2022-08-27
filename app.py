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

# import of external fonts

external_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Titan+One&display=swap",
    "https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap",
    "https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap"
]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
picture_parts = []
listOfIndicators = []

startWidth = 450
startHeight = 300

# application structure

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.P(id='title1', children="Pic"),
                html.P(id='title2', children="ture"),
                html.P(id='title3', children="  Puz"),
                html.P(id='title4', children="zle"),
            ], id='logo'),
            html.Div(id='closeArrow'),
        ], id='welcomeScreen'),
        html.Div([
            html.P(children=[html.B(
                "HELLO !!!"), html.Br(), "At the beginning, please select the maximum area on which the photo will be displayed using the sliders."], id="msg"),
            dcc.Slider(0, 2, 0.1, value=1, marks=None, tooltip={
                       'placement': 'bottom'}, id="widthSize"),
            dcc.Slider(0, 2, 0.1, value=1, marks=None, vertical=True, tooltip={
                       'placement': 'right'}, verticalHeight=300, id="heightSize"),
            html.Div(style={'width': startWidth,
                     'height': startHeight}, id="pictureDimension"),
            dcc.Link('Ready', href='/select', id='link')
        ], id='setDimension'),
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

# the user indicates the maximum area that the photo will occupy


@app.callback(
    Output('pictureDimension', 'style'),
    [Input('widthSize', 'value'),
     Input('heightSize', 'value'), ]
)
def change_dimension(val1, val2):
    global newWidth
    newWidth = int(startWidth*val1)
    global newHeight
    newHeight = int(startHeight*val2)
    return {'width': newWidth, 'height': newHeight}


# dividing the image into 9 parts


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

# create a list of indicators used in determining the top and left properties of each part of the image


def position_indicators():
    for i in range(8):
        indicator = (i % 3, i//3)
        listOfIndicators.append(indicator)

# a function to check divisibility by three, used in determining the final dimensions of the sheet


def check_divide(arg):
    if arg % 3 != 0:
        while arg % 3 != 0:
            arg = arg+1
    return arg

# upload content


@app.callback(
    Output('picture', 'children'),
    [Input('load', 'contents')]
)
def load_picture(contents):
    if len(listOfIndicators) > 0:
        listOfIndicators.clear()
        picture_parts.clear()
    if contents != None:

        img = base64.b64decode(contents.split(",")[1])
        img = np.frombuffer(img, dtype=np.uint8)
        img = cv2.imdecode(img, flags=1)
        img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
        imgPreview = imutils.resize(image=img, width=int(newWidth*0.3))
        if(img.shape[1] >= img.shape[0]):
            biggerDimension = check_divide(newWidth)
            img = imutils.resize(
                image=img, width=biggerDimension)
            secondDimension = check_divide(img.shape[0])
            img = cv2.resize(
                img, (biggerDimension, secondDimension))
            divide_picture(img)
            position_indicators()

        elif(img.shape[1] < img.shape[0]):
            biggerDimension = check_divide(newHeight)
            img = imutils.resize(
                image=img, height=biggerDimension)
            secondDimension = check_divide(img.shape[1])
            img = cv2.resize(
                img, (secondDimension, biggerDimension))
            divide_picture(img)
            position_indicators()
        return [html.Div([html.Div([html.Img(src=im.fromarray(picture_parts[i]))], id=str(i), className="pictureParts", style={'position': 'absolute', 'left': listOfIndicators[i][0]*unit_width, 'top':listOfIndicators[i][1]*unit_height}) for i in range(8)], id='loadedPicture', style={'width': img.shape[1], 'height': img.shape[0]}), html.Details([html.Summary('Preview'), html.Img(src=im.fromarray(imgPreview))], id='view'), html.Button(id='newImg', children='Load new image')]

# remove the content


@app.callback(
    Output('load', 'contents'),
    [Input('newImg', 'n_clicks')]
)
def clearContent(btn):
    try:
        return
    except:
        return html.Div([html.B('SORRY :('), html.P(
            'I have a problem. Refresh your browser to try again.')], id='fail')


if __name__ == '__main__':
    app.run_server(debug=True)
