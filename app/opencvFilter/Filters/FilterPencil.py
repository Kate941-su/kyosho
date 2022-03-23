# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:15:34 2022

@author: valle
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 17:45:06 2022

@author: KaitoKitaya
"""

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
FILTER_NAME = "_pencil"
FILTER_ALIAS = "鉛筆風"

class FilterPencil(Filter):
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
        #おすすめサイズ
        self.blurSize = 3
    # abstractmethod
    # メンバ用の絵を作成する
    def makePictureForMember(self):
        self.img = self.executePencil(self.img)

    # abstractmethod
    # フィルター名を取得する。
    def getFilterName(self):
        return FILTER_NAME

    # abstractmethod
    # フィルターのエイリアスを取得する。
    def getFilterAlias(self):
        return FILTER_ALIAS

    # abstractmethod
    # 保存ファイル名を取得する
    def getFileName(self):
        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)
        
    # 鉛筆画風を実行する
    def executePencil(self, img):
        greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        invertImg = cv2.bitwise_not(greyImg)
        kernelSize = 199
        blurImg=cv2.GaussianBlur(invertImg, (kernelSize, kernelSize),0)
        invblurImg=cv2.bitwise_not(blurImg)
        sketchImg=cv2.divide(greyImg, invblurImg, scale=256.0)
        return sketchImg





    