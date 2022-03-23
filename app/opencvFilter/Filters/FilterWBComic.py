# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:26:34 2022

@author: Kitaya
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
FILTER_NAME = "_WBComic"
FILTER_ALIAS = "漫画風(白黒)"

class FilterWBComic(Filter):
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)

    # abstractmethod
    # メンバ用の絵を作成する
    def makePictureForMember(self):
        materialPath = super().getMaterialPath()
        screen = cv2.imread(materialPath + "tone4.png")
        self.img = self.makeWBComic(self.img, screen)

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
        
    #ぼかしの強さを設定する
    def setBlurSize(self, blurSize):
        self.blurSize = blurSize
        
    # 漫画風(白黒)を作成する
    def makeWBComic(self, src, screen, th1=60, th2=150):
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  
        # スクリーントーン画像を入力画像と同じ大きさにリサイズ
        screen = cv2.resize(screen,(gray.shape[1],gray.shape[0]))  
        # Cannyアルゴリズムで輪郭検出し、色反転
        edge = 255 - cv2.Canny(gray, 80, 120)  
        # 三値化
        gray[gray <= th1] = 0
        gray[gray >= th2] = 255
        # np.whereは全要素に対して実行
        gray[ np.where((gray > th1) & (gray < th2)) ] = screen[ np.where((gray > th1)&(gray < th2)) ]
        # 三値画像と輪郭画像を合成(bitwise_andはsrcとmaskの各画素の論理積)
        return cv2.bitwise_and(gray, edge)