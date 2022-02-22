# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:52:36 2022

@author: valle

フィルター親クラス
"""

import cv2
import numpy as np
from PIL import Image
import sys
sys.path.append('../')
from ..Utils.FilterFunction import *
from ..Utils.ResourceIOFunction import *

FILTER_NAME = "_dotArt"

class Filter():
    # コンストラクタ
    def __init__(self, imgPath):
        self.path = imgPath
        self.img = self.setImage(imgPath)

    # イメージを読み取る
    def setImage(self, path):
        return cv2.imread(path, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)

    # 保存ファイル名を取得する
#    def getFileName(self):
#        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)