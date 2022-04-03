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
FILTER_NAME = "_grayScale"
FILTER_ALIAS = "グレースケール"

class FilterGrayScale(Filter):
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
    # abstractmethod
    # メンバ用の絵を作成する
    def makePictureForMember(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

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
    