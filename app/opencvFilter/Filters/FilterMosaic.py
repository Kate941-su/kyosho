# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:30:34 2022

@ author: valle

@ 日本語名:モザイク
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
FILTER_NAME = "_mosaic"
FILTER_ALIAS = "モザイク"

class FilterMosaic(Filter):
    
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
        self.mosaic = 0.05

    # メンバ用の絵を作成する
    def makePictureForMember(self):
        self.img = self.executeMosaic(self.img)

    # フィルター名を取得する。
    def getFilterName(self):
        return FILTER_NAME

    # フィルターのエイリアスを取得する。
    def getFilterAlias(self):
        return FILTER_ALIAS

    # モザイクをパーセントからmosaic値に変換する
    # 100パーセントでmosaic=0.01、0パーセントでmosaic=1
    # 線形でモザイク度合いを変化させる。
    def convertPercentToMosaicValue(self, percent):
        assert percent != 0
        return 1 / percent 

    # モザイク処理をする
    def executeMosaic(self, img):
        img[:, :, :3] = mosaic(img[:, :, :3], self.mosaic)    # モザイク処理
        return img   
    
    # モザイク値を設定する(0から1)
    def setMosaicValue(self, mosaic):
        self.mosaic = self.convertPercentToMosaicValue(mosaic)
    
    # 保存ファイル名を取得する
    def getFileName(self):
        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)
