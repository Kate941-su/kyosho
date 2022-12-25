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
FILTER_NAME = "_stylization"
FILTER_ALIAS = "水彩画風"

class FilterStylization(Filter):
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
        # なめらかさ(0 - 100)
        self.smoothness = 60
        # 色のにじみ度合い(0 - 1)
        self.bleeding = 0.5
    # abstractmethod
    # メンバ用の絵を作成する
    def makePictureForMember(self):
        self.img = cv2.stylization(self.img, sigma_s = self.smoothness, 
                                                    sigma_r = self.bleeding)

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
    
    # なめらかさを設定する
    def setSmoothness(self, smoothness):
        self.smoothness = smoothness

    # にじみ度合いを設定する
    def setBleeding(self, bleeding):
        self.bleeding = bleeding * 0.01
