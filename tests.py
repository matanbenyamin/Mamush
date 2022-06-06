import cv2
import numpy as np
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"



im = cv2.imread('Picture1.png')
im = im[:, :, ::-1]

fig = px.imshow(im)
fig.show()

