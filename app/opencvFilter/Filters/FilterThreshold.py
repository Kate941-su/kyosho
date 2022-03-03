# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:31:23 2022

@author: valle

@ 日本語名：二値化(大津の二値化)
"""

# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
from PIL import Image
from .Filter import Filter 
from ..Utils.FilterFunction import *
from ..Utils.ResourceIOFunction import *

# おまじない
sys.path.append('../')
FILTER_NAME = "_threshold"
FILTER_ALIAS = "二値化"
class FilterThreshold(Filter):

    #　コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
        self.colorNum = 8

    # フィルター名を取得する。
    def getFilterName(self):
        return FILTER_NAME

    # フィルターのエイリアスを取得する。
    def getFilterAlias(self):
        return FILTER_ALIAS

    # メンバ用の絵を作成する
    def makePictureForMember(self):
        dummy , self.img = self.threshold(self.img)
        
    # 二値化する
    # @ret : 二値化の閾値
    def threshold(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)# グレースケール変換
        ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)# 大津の二値化        
        return ret, th

    # 保存ファイル名を取得する
    def getFileName(self):
        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)

    
