# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 00:04:34 2022

@author: valle
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:31:23 2022

@author: valle
"""

# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image
import FilterFunction as FF
import ResourceIOFunction as RIF

FILTER_NAME = "_dotArt"

class FilterDotArt():
    def __init__(self, imgPath):
        self.path = imgPath
        self.mozike = 0.05
        self.colorNum = 8
        self.img = self.setImage(imgPath)
    # ドット絵化
    # @alpha : モザイク一個の大きさ
    def dotArt(self, img):
        img[:, :, :3] = FF.mosaic(img[:, :, :3], self.mozike)    # モザイク処理
        img[:, :, :3] = FF.sub_color(img[:, :, :3], self.colorNum)
        return img    # 減色処理
    
    # モザイク値を設定する(0から1)
    def setMozikeValue(self, mozike):
        self.mozike = mozike

    # 色数を設定する
    def setColorNum(self, colorNum):
        self.colorNum = colorNum
    
    # イメージを読み取る
    def setImage(self, path):
        return cv2.imread(path, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)
    
    # 透過度を反映する
    def writeAlpha(self, imgAlpha):
        None

    # 保存ファイル名を取得する
    def getFileName(self):
        return RIF.getFileNameWithoutExt(self.path) + FILTER_NAME + RIF.getFileExt(self.path)
    
#メイン処理
path = "ramuparudo.png"
filterDP = FilterDotArt(path)
mozike = 1
colorNum = 4
filterDP.setMozikeValue(mozike)
filterDP.setColorNum(colorNum)
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)
dst = filterDP.dotArt(img)# ドット絵化
dstName = filterDP.getFileName()
cv2.imwrite(filterDP.getFileName(), img)# 結果を出力
dst = RIF.makeFabicon(dst, 144, path = filterDP.getFileName())
