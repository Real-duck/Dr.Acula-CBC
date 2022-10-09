from cgi import test
import re
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
import numpy as np
import cv2

def load_image(image_file):
    img = Image.open(image_file)
    # resize image to 2592x1944
    image = img.resize((2592, 1944))
    # 24 bit color depth
    image = image.convert('RGB')
    image.save("images/tmp.jpg")
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    return image
def remove_artifacts(img):
    image = cv2.imread(img)
    # crop 100 px from left and top
    image = image[100:, 100:]
    # crop 50 px bottom
    image = image[:-50, :]
    # crop 110 px right
    image = image[:, :-110]
    # overwrite image
    cv2.imwrite(img, image)
