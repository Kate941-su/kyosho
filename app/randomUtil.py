# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:25:40 2022

@author: valle
"""
import random
import string
import hashlib

# ランダム文字列を得る
# @wordCount : 出力文字数
def getRandomString(wordCount):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(wordCount)]
   return ''.join(randlst)

# ipアドレスからハッシュ値を取得する
# @ipAddress : request.META.get("REMOTE_ADDR")から受け取ったものをそのまま入れてもよい(ピリオドつきでもよい)
def getHashFromIpAddress(ipAddress):
    # ipv4用ピリオドを除く
    ipNopil = ipAddress.replace(".", "")
    # ipv6用ピリオドを除く
    ipNopil = ipNopil.replace(":", "")
    return hashlib.md5(ipNopil.encode()).hexdigest()