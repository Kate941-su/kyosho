# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:31:23 2022

@author: valle

@ 日本語名：減色
"""

# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image
import sys
sys.path.append('../')
from .Filter import Filter 
from ..Utils.FilterFunction import *
from ..Utils.ResourceIOFunction import *

FILTER_NAME = "_subColor"

class FilterSubColor(Filter):
    def __init__(self, imgPath):
        super().__init__(imgPath)
        self.colorNum = 8
    # ドット絵化
    # @alpha : モザイク一個の大きさ
    def subColor(self, img):
        img[:, :, :3] = sub_color(img[:, :, :3], self.colorNum)# 減色
        return img    # 減色処理
    
    # 色数を設定する
    def setColorNum(self, colorNum):
        self.colorNum = colorNum
    
    # 保存ファイル名を取得する
    def getFileName(self):
        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)