import streamlit as st
from cgi import test
import re
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
import numpy as np
import cv2
import pandas as pd
import io
from model import *
import os
import glob
import cv2
import joblib
import matplotlib.pyplot as plt


# ---
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

def home():
    st.markdown('## Was ist Dr Acula?')
    st.markdown('Inspiriert vom berüchtigten Vampir - mit seiner eigenen Netflix Serie - Dracula, hat sich '
               'der Vampir Dr. Acula dazu entschieden sein Wissen über Blut zu veröffentlichen. Er kann '
               'eine sich oft wiederholende, aber auch wichtige Aufgabe, vom Zählen der Arten von Blutkörperchen übernehmen.')
    st.markdown('___')



    st.markdown('## Die Einstellungen ')
    st.markdown('#### Transformationen')
    st.markdown(
        '*Mit diesen Methoden kann das Ergebnis leicht überprüft werden. Der Datensatz kann mit den Ergebnissen auch erweitert werden.*')
    st.markdown('___')
    st.markdown('___Threshold___:')
    st.markdown('Beim Thresholding werden Vordergrundpixel vom Hintergrund seperiert. '
                ' Die Pixel, die zum Vordergrund gehören sind Weiß, die, die zum Hintergrund gehören sind Schwarz. [Mehr zum benutzten Verfahren](https://www.wikiwand.com/en/Otsu%27s_method)')
    st.image(Image.open('images/threshold_edge_mask.jpg'), caption='Thresholding für rote Blutkörperchen',
                width=400)
    st.markdown('___')# 
    st.markdown('___Hough Transform___:')
    st.markdown(
        'Diese Methode kann spezifische Formen erkennen. Da Blutkörperchen oft kreisförmig sind, wird hier Circle Hough Transform verwendet. '
        'Das Ergebnis kann für das Zählen einer Blutkörperchen Art benutzt werden. [Mehr zum benutzten Verfahren](https://sbme-tutorials.github.io/2021/cv/notes/4_week4.html)')
    st.image(Image.open('images/hough_transform.jpg'), caption='Hough Transform für rote Blutkörperchen',
                width=400)
    st.markdown('___')
    st.markdown('___Component labeling___:')
    st.markdown(
        'Dieser Algorithmus erkennt verbundene Objekte in einem binären Bild, also das Ergebnis der Segmentation.'
        'Component labeling kann auch für das Zählen benutzt werden. [Mehr zum benutzten Verfahren] (https://pyimagesearch.com/2021/02/22/opencv-connected-component-labeling-and-analysis/)')
    st.image(Image.open('images/component_labeling.jpg'), caption='Component labeling für rote Blutkörperchen',
                width=400)
    st.markdown('___')
    st.markdown('___Distance transform___:')
    st.markdown(
        'Diese Methode nimmt ein binäres Bild und gibt ein grayscale Bild zurück, das die Distanz zwischen den Pixeln repräsentiert. '
        'Je weiter ein Pixel vom Rand entfernt ist, desto heller wird er sein. [Mehr zum benutzten Verfahren](https://homepages.inf.ed.ac.uk/rbf/HIPR2/distance.htm)')
    st.image(Image.open('images/distance_transform.png'), caption='Distance transform für rote Blutkörperchen',
                 width=400)
