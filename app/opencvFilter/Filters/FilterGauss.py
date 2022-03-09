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
FILTER_NAME = "_gauss"
FILTER_ALIAS = "ガウスぼかし"

class FilterGauss(Filter):
    
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
        self.deviation = 3
        self.kernel = 3

    # メンバ用の絵を作成する
    def makePictureForMember(self):
        self.img = self.executeGauss(self.img)

    # フィルター名を取得する。
    def getFilterName(self):
        return FILTER_NAME

    # フィルターのエイリアスを取得する。
    def getFilterAlias(self):
        return FILTER_ALIAS

    # ガウスぼかし処理をする
    def executeGauss(self, img):
        img = cv2.GaussianBlur(img, (self.kernel, self.kernel), self.deviation)
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



