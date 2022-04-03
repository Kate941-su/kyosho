# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 17:45:06 2022

@author: KaitoKitaya
"""
# 既存パッケージ
import cv2
import numpy as np
import sys
from PIL import Image
import os
import torch
from torchvision.transforms.functional import to_tensor, to_pil_image
from .model import Generator
from .Filter import Filter 
from ..Utils.FilterFunction import *
from ..Utils.ResourceIOFunction import *

# おまじない
sys.path.append('../')
FILTER_NAME = "_AIAnimation"
FILTER_ALIAS = "AIアニメ風"

class FilterAIAnimeArt(Filter):
    # コンストラクタ
    def __init__(self, imgPath):
        super().__init__(imgPath)
        #編集モード
        self.editMode = 0
        
    # abstractmethod
    # メンバ用の絵を作成する
    def makePictureForMember(self):
        self.img = self.executeAIAnimeArt()
        
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
        
    # 編集モードを選択する
    def setEditMode(self, editMode):
        self.editMode = editMode

    # numpyイメージをPILイメージにコンバートする
    def convertImage(self, x32 = False):
        pilImg = Image.fromarray(self.img)
        pilImg = pilImg.convert("RGB")
        if x32:
            def to_32s(x):
                return 256 if x < 256 else x - x % 32
            w, h = pilImg.size
            pilImg = pilImg.resize((to_32s(w), to_32s(h)))
        return pilImg
        
    # AIアニメ風を実行する
    def executeAIAnimeArt(self):
        torch.backends.cudnn.enabled = False
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True
        device = "cpu"
        net = Generator()
        checkPointList = [
            "./weights/celeba_distill.pt",
            "./weights/face_paint_512_v1.pt",
            "./weights/face_paint_512_v2.pt",
            "./weights/paprika.pt",
        ]
        checkPoint = checkPointList[self.editMode]
        net.load_state_dict(torch.load(checkPoint, map_location="cpu"))
        net.to(device).eval()
        image = self.convertImage(False)#ここは微妙(32bitメモリのことか？)
        with torch.no_grad():
            image = to_tensor(image).unsqueeze(0) * 2 - 1
            out = net(image.to(device), False).cpu()# args.upsample_alignはわからない
            out = out.squeeze(0).clip(-1, 1) * 0.5 + 0.5
            out = to_pil_image(out)
            outImageName = "result_"
            if self.editMode == 0:
                outImageName += "celeba_"
            elif self.editMode == 1:
                outImageName += "facePaint1_"
            elif self.editMode == 2:
                outImageName += "facePaint2_"
            elif self.editMode == 3:
                outImageName += "paprika_"
            else :
                assert(False)
        return np.array(out)

    #PILイメージに変換する
#    def loadImage(imagePath, x32 = False):
#        img = Image.open(imagePath).convert("RGB")
#        if x32:
#            def to_32s(x):
#                return 256 if x < 256 else x - x % 32
#            w, h = img.size
#            img = img.resize((to_32s(w), to_32s(h)))
#        return img

    """
    # AIアニメ風変換コア処理
    def testKyosho(self, aImagePath):
        torch.backends.cudnn.enabled = False
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True
        device = "cpu"
        net = Generator()
        checkPointList = [
            "./weights/celeba_distill.pt",
            "./weights/face_paint_512_v1.pt",
            "./weights/face_paint_512_v2.pt",
            "./weights/paprika.pt",
        ]
        # アニメ風GANの種類の変更
        checkPointNum = 1
        checkPoint = checkPointList[checkPointNum]
        net.load_state_dict(torch.load(checkPoint, map_location="cpu"))
        net.to(device).eval()
        dstDir = "./dstImgs/"
        os.makedirs(dstDir, exist_ok=True)
        imageName = aImagePath
        image = self.loadImage(imageName, False)#ここは微妙(32bitメモリのことか？)
        with torch.no_grad():
            image = to_tensor(image).unsqueeze(0) * 2 - 1
            out = net(image.to(device), False).cpu()# args.upsample_alignはわからない
            out = out.squeeze(0).clip(-1, 1) * 0.5 + 0.5
            out = to_pil_image(out)
            outImageName = "result_"
            if checkPointNum == 0:
                outImageName += "celeba_"
            elif checkPointNum == 1:
                outImageName += "facePaint1_"
            elif checkPointNum == 2:
                outImageName += "facePaint2_"
            elif checkPointNum == 3:
                outImageName += "paprika_"
            else :
                assert(False)
#        out.save(os.path.join(dstDir, outImageName + imageName))
        return np.array(out)
    #testKyosho("junna_up.jpg")
    """    

    





    