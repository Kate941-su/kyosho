# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 18:28:04 2022

@author: spectre
"""

# -*- coding: utf-8 -*-


# 既存パッケージ
import cv2
import numpy as np
import sys
from PIL import Image
from .Filter import Filter 
from ..Utils.FilterFunction import *
from ..Utils.ResourceIOFunction import *

# おまじない
sys.path.append('../')
FILTER_NAME = "_edge"
FILTER_ALIAS = "エッジ検出"

class FilterEdge(Filter):
    
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
        self.deviation = 3
        self.kernel = 3

    # メンバ用の絵を作成する
    def makePictureForMember(self):
        self.img = self.executeEdge(self.img)

    # フィルター名を取得する。
    def getFilterName(self):
        return FILTER_NAME

    # フィルターのエイリアスを取得する。
    def getFilterAlias(self):
        return FILTER_ALIAS

    # エッジ検出処理をする
    #@cv2.CV_32F = 32ビット浮動小数点数
    def executeEdge(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #グレースケールに変換
        img = cv2.GaussianBlur(img, (self.kernel, self.kernel), self.deviation)#ガウスぼかしでノイズ除去
        img = cv2.Laplacian(img, cv2.CV_32F) #エッジ検出
        return img
    
    # σ値を設定する(標準偏差)
    def setDeviation(self, deviation):
        self.deviation = deviation
        
    # カーネル値を設定する
    def setKernel(self, kernel):
        self.kernel = kernel
        
    # 保存ファイル名を取得する
    def getFileName(self):
        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)



