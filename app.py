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
        if(img.shape[1] >= img.shape[0]):
            dimensionToCompare = screen.width
            biggerDimension = check_divide(int(dimensionToCompare*0.6))
            img = imutils.resize(
                image=img, width=biggerDimension)
            secondDimension = check_divide(img.shape[0])
            img = cv2.resize(
                img, (biggerDimension, secondDimension))
            divide_picture(img)
            position_indicators()

        elif(img.shape[1] < img.shape[0]):
            dimensionToCompare = screen.height
            biggerDimension = check_divide(int(dimensionToCompare*0.7))
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
    return


if __name__ == '__main__':
    app.run_server(debug=True)
