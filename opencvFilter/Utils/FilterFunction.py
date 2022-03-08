# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 00:05:42 2022

@author: valle
"""
#フィルターに使われた技法を一括管理する
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


# 　グレースケールの画像を3チャンネル化して返す
def convertFrom2DImageTo3DImage(img):
    img3D = np.zeros((len(img), len(img[0]), 4))
    for i in range(3):
        img3D[:, :, i] = img
    nonAlpha = np.full((len(img), len(img[0])), 255)
    img3D[:, :, 3] = nonAlpha
    return img3D