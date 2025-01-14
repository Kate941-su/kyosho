# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:52:36 2022

@author: valle

フィルター親クラス(抽象クラス)
"""

import cv2
import numpy as np
from PIL import Image
import sys
from abc import ABCMeta, abstractmethod
from ..Utils.FilterFunction import *
from ..Utils.ResourceIOFunction import *

# おまじない
sys.path.append('../')
FILTER_NAME = "_"
FILTER_ALIAS = "_"
MATERIAL_PATH = "./material/"
class Filter(metaclass = ABCMeta):

    # 抽象メソッド ： メンバ用の絵を作成する
    @abstractmethod
    def makePictureForMember(self):
        print("you have to imlement concreate method!")

    # 保存ファイル名を取得する
    @abstractmethod
    def getFileName(self):
        return getFileNameWithoutExt(self.path) + FILTER_NAME + getFileExt(self.path)
    
    # フィルター名を取得する。
    @abstractmethod
    def getFilterName(self):
        return FILTER_NAME

    # フィルターのエイリアスを取得する。
    @abstractmethod
    def getFilterAlias(self):
        return FILTER_ALIAS

    # コンストラクタ
    def __init__(self, imgPath):
        self.path = imgPath
        self.img = self.setImage(imgPath)
        if (type(self.img) != type(None) and self.img.ndim != 3):
            self.img = convertFrom2DImageTo3DImage(self.img)
    # イメージを読み取る
    def setImage(self, path):
        return cv2.imread(path, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)
    
    # イメージを取得する
    def getImage(self):
        return self.img
    
    # 素材のパスを取得する
    def getMaterialPath(self):
        return MATERIAL_PATH
    
    # 原画のパスを取得する
    def getSrcPath(self):
        return self.path