# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:25:40 2022

@author: valle
"""
import random
import string

# ランダム文字列を得る
# @wordCount : 出力文字数
def getRandomString(wordCount):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(wordCount)]
   return ''.join(randlst)

print(getRandomString(16))
