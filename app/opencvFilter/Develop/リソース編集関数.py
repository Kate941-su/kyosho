# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 00:07:47 2022

@author: valle
"""

import cv2
import numpy as np
from PIL import Image

# ファビコン作成
def makeFabicon(img, dstWidth):
    img = cv2.resize(img, (dstWidth, dstWidth))
    return img