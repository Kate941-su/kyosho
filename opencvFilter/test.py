# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 09:45:21 2022

@author: valle
"""

# pythonモジュール
import cv2
import numpy as np
from PIL import Image

# 自作モジュール
from Filters.FilterDotArt import FilterDotArt
from Filters.FilterMosaic import FilterMosaic
from Filters.FilterSubColor import FilterSubColor
from Filters.FilterThreshold import FilterThreshold
from Utils.ResourceIOFunction import *
#import sys


path = "./Images/Lenna.JPG"
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)

testName = "subColor"

#ドット絵風
if testName == "dotArt":
    filterDP = FilterDotArt(path)
    mozike = 0.1
    colorNum = 10
    filterDP.setMozikeValue(mozike)
    filterDP.setColorNum(colorNum)
    dst = filterDP.dotArt(img)# ドット絵化
    dstName = filterDP.getFileName()
    cv2.imwrite(filterDP.getFileName(), img)# 結果を出力
    dst = makeFabicon(dst, 144, path = filterDP.getFileName())

# モザイク
if testName == "mosaic":
    filterMosaic = FilterMosaic(path)
    mosaic = 0.05
    filterMosaic.setMosaicValue(mosaic)
    dst = filterMosaic.executeMosaic(img)
    dstName = filterMosaic.getFileName()
    cv2.imwrite(filterMosaic.getFileName(), img)# 結果を出力

# 減色
if testName == "subColor":
    filterSubColor = FilterSubColor(path)
    colorNum = 3
    filterSubColor.setColorNum(colorNum)
    dst = filterSubColor.subColor(img)
    dstName = filterSubColor.getFileName()
    cv2.imwrite(filterSubColor.getFileName(), img)# 結果を出力

# 二値化
if testName == "threshold":
    filterThreshold = FilterThreshold(path)
    dst = filterThreshold.threshold(img)
    ret, th = filterThreshold.threshold(img)
    cv2.imwrite(filterThreshold.getFileName(), th)# 結果を出力
