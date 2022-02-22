# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:31:23 2022

@author: valle

@ 日本語名：ドット絵風
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

FILTER_NAME = "_dotArt"

class FilterDotArt(Filter):
    def __init__(self, imgPath):
#        self.path = imgPath
#        self.img = self.setImage(imgPath)
        super().__init__(imgPath)
        self.mozike = 0.05
        self.colorNum = 8
    # ドット絵化
    # @alpha : モザイク一個の大きさ
    def dotArt(self, img):
        img[:, :, :3] = mosaic(img[:, :, :3], self.mozike)    # モザイク処理
        img[:, :, :3] = sub_color(img[:, :, :3], self.colorNum)
        return img    # 減色処理
    
    # モザイク値を設定する(0から1)
    def setMozikeValue(self, mozike):
        self.mozike = mozike

    # 色数を設定する
    def setColorNum(self, colorNum):
        self.colorNum = colorNum
    
    # イメージを読み取る
#    def setImage(self, path):
#        return cv2.imread(path, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)
    
    # 透過度を反映する
    def writeAlpha(self, imgAlpha):
        None

    # 保存ファイル名を取得する
    def getFileName(self):
        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)
