# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:30:34 2022

@ author: valle

@ 日本語名:ガウスぼかし
"""

# 既存パッケージ
import cv2
import numpy as np
import sys
from PIL import Image
from .Filter import Filter 
from Utils.FilterFunction import *
from Utils.ResourceIOFunction import *

# おまじない
sys.path.append('../')
FILTER_NAME = "_gauss"

class FilterGauss(Filter):
    
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
        self.gauss = 10

    # メンバ用の絵を作成する
    def makeDotArtForMember(self): #makeGaussForMember?
        self.img = self.subColor(self.img) #何のメソッド？

    # フィルター名を取得する。
    def getFilterName(self):
        return FILTER_NAME

    # ぼかし処理をする
    def executeGauss(self, img):
        img[:, :, :3] = GaussianBlur(img[:, :, :3], (3, 3), self.gauss)    # モザイク処理
        return img    # 減色処理
    
    # ガウス値σを設定する
    def setGaussValue(self, gauss):
        self.gauss = gauss
    
    # 保存ファイル名を取得する
    def getFileName(self):
        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)
