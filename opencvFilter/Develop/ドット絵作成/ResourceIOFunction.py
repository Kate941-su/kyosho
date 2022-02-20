# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 00:07:47 2022

@author: valle
"""
# 例えばファビコンを作成する、動画を画像フレームに分ける、画像からgif、mp4を作るといった
# 何らかのリソースに対して入出力を行う関数


import cv2
import numpy as np
from PIL import Image
import os

# ファビコンに変換して画像を保存する
def makeFabicon(img, dstWidth, path):
    fabiconSizeArray = [(16, 16), (32, 32), (48, 48), (64, 64)]
    img = cv2.resize(img, (dstWidth, dstWidth))
    img = Image.open(path)
    img.save(getPathWithoutExt(path) + ".ico", sizes = fabiconSizeArray)

# ファイル拡張子を除いたパスを得る
def getPathWithoutExt(path):
    noExtendFileName = os.path.splitext(path)[0]
    dirName = os.path.dirname(path)
    if(dirName == ""):
        dirName = "."
    return dirName + "/" + noExtendFileName

#  パスからファイル拡張子を除いたファイル名を得る
def getFileNameWithoutExt(path):
    return os.path.splitext(path)[0]

# パスからファイル拡張子を得る
def getFileExt(path):
    return os.path.splitext(path)[1]