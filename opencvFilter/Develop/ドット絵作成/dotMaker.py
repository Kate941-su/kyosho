# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:31:23 2022

@author: valle
"""

# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image

# 減色処理
def sub_color(src, K):
    Z = src.reshape((-1,3))    # 次元数を1落とす
    Z = np.float32(Z)    # float32型に変換
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)    # 基準の定義
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)    # K-means法で減色
    center = np.uint8(center)    # UINT8に変換
    res = center[label.flatten()]    # 配列の次元数と入力画像と同じに戻す
    return res.reshape((src.shape))

# モザイク処理
def mosaic(img, alpha):
    h, w, ch = img.shape    # 画像の高さ、幅、チャンネル数
    img = cv2.resize(img,(int(w*alpha), int(h*alpha)))    # 縮小→拡大でモザイク加工
    img = cv2.resize(img,(w, h), interpolation=cv2.INTER_NEAREST)
    return img

# ドット絵化
# @alpha : モザイク一個の大きさ
def pixelArt(img, alpha=2, K = 2):
    img = mosaic(img, alpha)    # モザイク処理
    white =  np.full((img.shape) , 1)# 透過png処理
    img = img * white
    return sub_color(img, K)    # 減色処理

# ファビコン作成
def makeFabicon(img, dstWidth):
    img = cv2.resize(img, (dstWidth, dstWidth))
    return img

# 透過処理
def makeTransparent(dst, alphaArray):
    dst[:, :, 3] = alphaArray
    return dst

#メイン処理
outPicName = "yureidoru"
fileType = ".png"
mozike = 0.05
colorNum = 8
img = cv2.imread(outPicName + fileType, cv2.IMREAD_UNCHANGED)# 入力画像を取得(α値も取得版)
dst = pixelArt(img[:, :, :3], mozike, colorNum)# ドット絵化
img[:, :, :3] = dst
cv2.imwrite(outPicName + "_dot_" + str(mozike) + fileType, img)# 結果を出力
isTransparent = True
IsFabicon = False
fabiconSizeArray = [(16, 16), (32, 32), (48, 48), (64, 64)]
if IsFabicon:
    dst = makeFabicon(dst, 144)
    img = Image.open(outPicName + "_dot_" + str(mozike) + fileType)
    img.save(outPicName + "_dot_" + str(mozike) + ".ico", sizes = fabiconSizeArray)