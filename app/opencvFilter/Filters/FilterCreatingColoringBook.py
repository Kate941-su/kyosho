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
FILTER_NAME = "_creatingColoringBook"
FILTER_ALIAS = "塗り絵化"

class FilterCreatingColoringBook(Filter):
    
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
        
    # abstractmethod
    # メンバ用の絵を作成する
    def makePictureForMember(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        #3. 膨張処理
        neiborhood = np.ones((5, 5), dtype=np.uint8)
        dilated = cv2.dilate(self.img, neiborhood, iterations=1)
        diff = cv2.absdiff(dilated, self.img)
        self.img = 255 - diff

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



    