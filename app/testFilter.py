# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 20:22:13 2022

@author: valle
"""

# pythonモジュール
import cv2
import numpy as np
import os
from PIL import Image
import sys

# 自作モジュール
from randomUtil import getRandomString, getHashFromIpAddress
from opencvFilter.Filters.FilterDotArt import FilterDotArt
from opencvFilter.Filters.FilterMosaic import FilterMosaic
from opencvFilter.Filters.FilterSubColor import FilterSubColor
from opencvFilter.Filters.FilterThreshold import FilterThreshold
from opencvFilter.Filters.FilterGauss import FilterGauss
from opencvFilter.Filters.FilterEdge import FilterEdge
from opencvFilter.Filters.FilterMedianFilter import FilterMedianFilter
from opencvFilter.Filters.FilterWBComic import FilterWBComic
from opencvFilter.Filters.FilterPencil import FilterPencil
from opencvFilter.Filters.FilterAIAnimeArt import FilterAIAnimeArt
from opencvFilter.Filters.FilterCreatingColoringBook import FilterCreatingColoringBook
from opencvFilter.Filters.FilterStylization import FilterStylization
from opencvFilter.Filters.FilterGrayScale import FilterGrayScale
from opencvFilter.Utils.ResourceIOFunction import *
# テストするフィルターの種類
# ""                          : 0,  # なし
# "dotArt"                    : 1,  # ドット絵風
# "mosaic"                    : 2,  # モザイク
# "subColor"                  : 3,  # 減色
# "threshold"                 : 4,  # 二値化
# "edge"                      : 5,  # エッジ検出
# "gauss"                     : 6,  # ガウスぼかし
# "medianFilter"              : 7,  # メディアンフィルター
# "WBComic"                   : 8,  # 漫画風(白黒)
# "pencil"                    : 9,  # 鉛筆風
# "AIAnimeArt"                : 10, # AIアニメ風
# "creatingColoringBook"      : 11, # 塗り絵化
# "stylization"               : 12, # 水彩画風
# "grayScale"                 : 13, # グレースケール
picName = "shimada.jpg"
if "debugpy" in sys.modules:
    path = "./app/testImages/" + picName
else:
    path = "./testImages/" + picName
testName = "AIAnimeArt"

# 1ドット絵風
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

# 2モザイク
elif testName == "mosaic":
    filterMosaic = FilterMosaic(path)
    mosaic = 20
    filterMosaic.setMosaicValue(mosaic)
    filterMosaic.makePictureForMember()
    cv2.imwrite(filterMosaic.getFileName(), filterMosaic.getImage())# 結果を出力

# 3減色
elif testName == "subColor":
    filterSubColor = FilterSubColor(path)
    colorNum = 9
    filterSubColor.setColorNum(colorNum)
    filterSubColor.makePictureForMember()
    cv2.imwrite(filterSubColor.getFileName(), filterSubColor.getImage())# 結果を出力

# 4二値化
elif testName == "threshold":
    filterThreshold = FilterThreshold(path)
    filterThreshold.makePictureForMember()
    cv2.imwrite(filterThreshold.getFileName(), filterThreshold.getImage())# 結果を出力

# 5ガウスぼかし
elif testName == "gauss":
    filterGauss = FilterGauss(path)
    name = filterGauss.getFilterName()
    deviation = 130
    kernel = 177
    filterGauss.setDeviation(deviation)
    filterGauss.setKernel(kernel)
    filterGauss.makePictureForMember()
    cv2.imwrite(filterGauss.getFileName(), filterGauss.getImage())# 結果を出力
    
# 6エッジ検出
elif testName == "edge":
    filterEdge = FilterEdge(path)
    name = filterEdge.getFilterName()
    deviation = 1
    kernel = 1
    filterEdge.setDeviation(deviation)
    filterEdge.setKernel(kernel)
    filterEdge.makePictureForMember()
    cv2.imwrite(filterEdge.getFileName(), filterEdge.getImage())# 結果を出力
    
# 7メディアンフィルター
elif testName == "medianFilter":
    filterMedianFilter = FilterMedianFilter(path)
    filterMedianFilter.makePictureForMember()
    cv2.imwrite(filterMedianFilter.getFileName(), filterMedianFilter.getImage())# 結果を出力

# 8漫画風(白黒)フィルター
elif testName == "WBComic":
    filterWBComic = FilterWBComic(path)
    filterWBComic.makePictureForMember()
    cv2.imwrite(filterWBComic.getFileName(), filterWBComic.getImage())# 結果を出力
    
# 9鉛筆風
elif testName == "pencil":
    filterPencil = FilterPencil(path)
    filterPencil.makePictureForMember()
    cv2.imwrite(filterPencil.getFileName(), filterPencil.getImage())

# 10AIアニメ風
elif testName == "AIAnimeArt":
    filterAIAnimeArt = FilterAIAnimeArt(path)
    # アニメ調1
    # 顔加工v1
    # 顔加工v2
    # パプリカ
    filterAIAnimeArt.setEditMode(2)
    filterAIAnimeArt.makePictureForMember()
    cv2.imwrite(filterAIAnimeArt.getFileName(), filterAIAnimeArt.getImage())
    
# 11塗り絵化
elif testName == "creatingColoringBook":
    filterCreatingColoringBook = FilterCreatingColoringBook(path)
    filterCreatingColoringBook.makePictureForMember()
    cv2.imwrite(filterCreatingColoringBook.getFileName(), 
                    filterCreatingColoringBook.getImage())

# 12水彩画風
elif testName == "stylization":
    filterStylization = FilterStylization(path)
    filterStylization.setSmoothness(100)
    filterStylization.setBleeding(0.5)
    filterStylization.makePictureForMember()
    cv2.imwrite(filterStylization.getFileName(), filterStylization.getImage())

# 13グレースケール
elif testName == "grayScale":
    filterGrayScale = FilterGrayScale(path)
    filterGrayScale.makePictureForMember()
    cv2.imwrite(filterGrayScale.getFileName(), filterGrayScale.getImage())

#何もしない
else:
    assert(False)


    
    
    
    

