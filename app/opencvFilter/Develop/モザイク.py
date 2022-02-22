# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:30:34 2022

@ author: valle

@ 日本語名:モザイク
"""

import cv2
import numpy as np
from PIL import Image
import sys
sys.path.append('../')
from Utils.FilterFunction import *
from Utils.ResourceIOFunction import *

FILTER_NAME = "_mosaic"

class FilterMosaic():
    def __init__(self, imgPath):
        self.path = imgPath
        self.mosaic = 0.05
        self.img = self.setImage(imgPath)

    # モザイク処理をする
    # @alpha : モザイク一個の大きさ
    def executeMosaic(self, img):
        img[:, :, :3] = mosaic(img[:, :, :3], self.mosaic)    # モザイク処理
        return img    # 減色処理
    
    # モザイク値を設定する(0から1)
    def setMosaicValue(self, mosaic):
        self.mosaic = mosaic
    
    # イメージを読み取る
    def setImage(self, path):
        return cv2.imread(path, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)
    
    # 保存ファイル名を取得する
    def getFileName(self):
        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)
    

#ドット絵風
path = "yureidoru.png"
mosaicFilter = FilterMosaic(path)
mosaicFilter.setMosaicValue(0.05)
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)
dst = mosaicFilter.executeMosaic(img)# ドット絵化
dstName = mosaicFilter.getFileName()
cv2.imwrite(mosaicFilter.getFileName(), img)# 結果を出力
dst = makeFabicon(dst, 144, path = mosaicFilter.getFileName())