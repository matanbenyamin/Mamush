import cv2
import numpy as np
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"



im = cv2.imread('Picture1.png')
im = im[:, :, ::-1]

fig = px.imshow(im)
fig.show()



im = cv2.imread('logo_white.png')
im = im[:, :, ::-1]

im[im==0] = 255

import matplotlib.pyplot as plt
plt.imshow(im)


# get batcj number  fro,m string
s1 = 'jhkljhBatch01jlkj'
s2 = 'jhkljh_batch02jlkj'

#extract batch number
