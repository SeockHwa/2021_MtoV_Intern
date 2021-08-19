import torch
from PIL import Image
from IPython.display import display
import cv2
import matplotlib.pyplot as plt

from fastseg import MobileV3Large
from fastseg.image import colorize, blend

print(torch.__version__)

# Model Load
# model = MobileV3Large.from_pretrained().cuda().eval()
model = MobileV3Large.from_pretrained().eval()

# Input Image
img = cv2.imread('image/output_front.jpg')
plt.figure("img")
plt.imshow(img)

# Labeled Image (segmentaion)
labels = model.predict_one(img)
plt.figure("label")
plt.imshow(labels)

# Colorized Image 
colorized = colorize(labels)
plt.figure("colorized")
plt.imshow(colorized) 

# Composited Iamge
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img=Image.fromarray(img)
composited = blend(img, colorized)
plt.figure("composited")
plt.imshow(composited) 
plt.show()