# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 20:22:13 2022

@author: valle
"""

# pythonモジュール
import cv2
import numpy as np
from PIL import Image

# 自作モジュール
from randomUtil import getRandomString, getHashFromIpAddress
from opencvFilter.Filters.FilterDotArt import FilterDotArt
from opencvFilter.Filters.FilterMosaic import FilterMosaic
from opencvFilter.Filters.FilterSubColor import FilterSubColor
from opencvFilter.Filters.FilterThreshold import FilterThreshold
from opencvFilter.Filters.FilterGauss import FilterGauss
from opencvFilter.Filters.FilterMedianFilter import FilterMedianFilter
from opencvFilter.Filters.FilterWBComic import FilterWBComic
from opencvFilter.Filters.FilterPencil import FilterPencil
from opencvFilter.Utils.ResourceIOFunction import *


path = "./testImages/sample_woman.png"
testName = "pencil"

# ドット絵風
if testName == "dotArt":
    filterDP = FilterDotArt(path)
    mozike = 25
    colorNum = 10
    name = filterDP.getFilterName()
    filterDP.setMosaicValue(mozike)
    filterDP.setColorNum(colorNum)
    filterDP.makePictureForMember()
    dstName = filterDP.getFileName()
    cv2.imwrite(filterDP.getFileName(), filterDP.getImage())# 結果を出力

# モザイク
if testName == "mosaic":
    filterMosaic = FilterMosaic(path)
    mosaic = 100
    filterMosaic.setMosaicValue(mosaic)
    filterMosaic.makePictureForMember()
    cv2.imwrite(filterMosaic.getFileName(), filterMosaic.getImage())# 結果を出力

# 減色
if testName == "subColor":
    filterSubColor = FilterSubColor(path)
    colorNum = 9
    filterSubColor.setColorNum(colorNum)
    filterSubColor.makePictureForMember()
    cv2.imwrite(filterSubColor.getFileName(), filterSubColor.getImage())# 結果を出力

# 二値化
if testName == "threshold":
    filterThreshold = FilterThreshold(path)
    filterThreshold.makePictureForMember()
    cv2.imwrite(filterThreshold.getFileName(), filterThreshold.getImage())# 結果を出力

#ガウスぼかし
if testName == "gauss":
    filterGauss = FilterGauss(path)
    name = filterGauss.getFilterName()
    deviation = 130
    kernel = 177
    filterGauss.setDeviation(deviation)
    filterGauss.setKernel(kernel)
    filterGauss.makePictureForMember()
    cv2.imwrite(filterGauss.getFileName(), filterGauss.getImage())# 結果を出力

# メディアンフィルター
if testName == "medianFilter":
    filterMedianFilter = FilterMedianFilter(path)
    filterMedianFilter.makePictureForMember()
    cv2.imwrite(filterMedianFilter.getFileName(), filterMedianFilter.getImage())# 結果を出力

# 漫画風(白黒)フィルター
if testName == "WBComic":
    filterWBComic = FilterWBComic(path)
    filterWBComic.makePictureForMember()
    cv2.imwrite(filterWBComic.getFileName(), filterWBComic.getImage())# 結果を出力
    
# 鉛筆風
if testName == "pencil":
    filterPencil = FilterPencil(path)
    filterPencil.makePictureForMember()
    cv2.imwrite(filterPencil.getFileName(), filterPencil.getImage())
    

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


    
    
    
    

