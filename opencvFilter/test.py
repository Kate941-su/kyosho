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


path = "./Images/Lenna_threshold.jpg"

img = cv2.imread(path, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)
if (img.ndim != 3):
    dummy = np.zeros((len(img), len(img[0]), 4))
    for i in range(3):
        dummy[:, :, i] = img
    nonAlpha = np.full((len(img), len(img[0])), 255)
    dummy[:, :, 3] = nonAlpha
    img = dummy

testName = "gauss"

# ドット絵風
if testName == "dotArt":
    filterDP = FilterDotArt(path)
    mozike = 0.05
    colorNum = 10
    name = filterDP.getFilterName()
    filterDP.setMozikeValue(mozike)
    filterDP.setColorNum(colorNum)
    filterDP.makeDotArtForMember()
    dst = filterDP.dotArt(img)# ドット絵化
    dstName = filterDP.getFileName()
    cv2.imwrite(filterDP.getFileName(), filterDP.getImage())# 結果を出力
#    dst = makeFabicon(dst, 32, path = filterDP.getFileName())

# ガウスぼかし
if testName == "gauss":
    filterGauss = FilterGauss(path)
    name = filterGauss.getFilterName()
    gauss = 10
    filterGauss.setGaussValue(gauss)
    dst = filterGauss.executeGauss(img)
    dstName = filterGauss.getFileName()
    cv2.imwrite(filterGauss.getFileName(), img)# 結果を出力
    
# モザイク
if testName == "mosaic":
    filterMosaic = FilterMosaic(path)
    name = filterMosaic.getFilterName()
    mosaic = 0.05
    filterMosaic.setMosaicValue(mosaic)
    dst = filterMosaic.executeMosaic(img)
    dstName = filterMosaic.getFileName()
    cv2.imwrite(filterMosaic.getFileName(), img)# 結果を出力

# 減色
if testName == "subColor":
    filterSubColor = FilterSubColor(path)
    colorNum = 9
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

#何もしない
else:
    None
"""
def outter(func):
    def inner(num):
        try:
            return func(num)
        except ZeroDivisionError:
            print("error has occured!")
            return
    return inner

def oldFunc(num):
    return 5 / num

newFunc = outter(oldFunc)

print(newFunc(0))
"""


    
    
    
    

