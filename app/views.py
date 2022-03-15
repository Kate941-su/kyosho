#2022/02/22 kitaya kaito
import cv2
import shutil
import os
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.conf import settings
from ipware import get_client_ip
from .FilterManagement import FilterManagement
from .forms import DocumentForm
from .models import Document
from .randomUtil import getRandomString, getHashFromIpAddress
from .opencvFilter.Filters.FilterDotArt import FilterDotArt
from .opencvFilter.Filters.FilterMosaic import FilterMosaic
from .opencvFilter.Filters.FilterSubColor import FilterSubColor
from .opencvFilter.Filters.FilterThreshold import FilterThreshold
from .opencvFilter.Filters.FilterGauss import FilterGauss

RANDOM_WORD_COUNT = 10

# ホーム画面のview
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'巨匠',
            'message':'ペンディング',
            'year':datetime.now().year,
        }
    )

# 各フィルター画面のview
def viewFilter(request):
    assert isinstance(request, HttpRequest)
    # クライアントのipアドレスを取得
    client_addr, _ = get_client_ip(request)
    # ipアドレスからハッシュ値を取得
    ipHash = getHashFromIpAddress(client_addr)
    # 出力先ファイルのルートディレクトリ(ディレクトリがなかったら作成)
    mediaDir = "./media/"
    if (not os.path.exists(mediaDir + ipHash)):
        os.makedirs(mediaDir + ipHash)
    if request.method == 'POST':
        # フォームのひな型をforms.pyモジュールから作成する
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    # サブミットされたファイルデータ
    filedata = request.FILES.get("avatar")
    # 原画パス
    srcPath = mediaDir + ipHash + "/thumbnail-" + getRandomString(RANDOM_WORD_COUNT) + "-base.png"
    if ("create" in request.POST): # 画像作成のとき
        srcPath = mediaDir + ipHash + "/thumbnail-" + getRandomString(RANDOM_WORD_COUNT) + "-base.png"
    elif ("recreate" in request.POST): # 再加工のとき  
        # 相対パスに変換する必要あり   
        srcPath = "." + request.POST.get("recreate-srcPath")
    # 出力先パス
    dstPath = mediaDir + ipHash + "/temporary-" + getRandomString(RANDOM_WORD_COUNT) + ".png"
    # 元画像を取得(ファイルフォーマットは選べるようにする)
    # ファイルの有無をPOSTで判断
    hasFileData = type(filedata) != type(None)
    if ("create" in request.POST):
        if (hasFileData):
            if (len(filedata) !=0):
                with open(dstPath, "wb+") as f:
                    for chunk in filedata:
                        f.write(chunk)
                # dstを先に開いておいてsrcにコピーしている＝＝この行では同じ二枚のファイルを作成している
                shutil.copy(dstPath, srcPath)
    elif ("recreate" in request.POST):
        # 再加工の場合は元画像が存在するかでhasFileDataを判断
        hasFileData = os.path.exists(srcPath)
        if (hasFileData):
            shutil.copy(srcPath, dstPath)
    requestName = request.path
    useFilter = None
    retHtml = ""
    addDict = {}
    # リクエストに応じて適切なフィルターを適用する
    # 記述順序はFilterの番号順
    # パラメータをブラウザで保持したいのでパラメータ設定するものはaddDictを設定する
    if (requestName == "/dotArt/"): # 1. ドット絵風のとき
        useFilter = FilterDotArt(dstPath)
        if (hasFileData): # 元画像が存在するとき 
            dotNum = int(request.POST.get("dotNum"))
            colorNum = int(request.POST.get("colorNum"))
            useFilter.setMosaicValue(dotNum)
            useFilter.setColorNum(colorNum)
            useFilter.makePictureForMember()
        else :
            # home画面からフィルターを起動するときはまだパラメータが設定されていない
            # 従って元画像が存在しないときは、ここで初期値を設定する必要がある。
            dotNum = 70
            colorNum = 8
        addDict = {
            "dotNum" : dotNum,
            "colorNum" : colorNum
        }
        retHtml = "app/dotArt.html"
    elif (requestName == "/mosaic/"): # 2. モザイクのとき
        useFilter = FilterMosaic(dstPath)
        if (hasFileData): # ファイルデータが届いていないとき  
            mosaic = int(request.POST.get("モザイク"))
            useFilter.setMosaicValue(mosaic)
            useFilter.makePictureForMember()
        else:
            mosaic = 25
        addDict = {
            "mosaic" : mosaic
        }
        retHtml = "app/mosaic.html"
    elif (requestName == "/subColor/"): # 3. 減色のとき
        useFilter = FilterSubColor(dstPath)
        if (hasFileData): # ファイルデータが届いていないとき  
            colorNum = int(request.POST.get("colorNum"))
            useFilter.setColorNum(colorNum)
            useFilter.makePictureForMember()
        else:
            colorNum = 8
        addDict = {
            "colorNum" : colorNum
        }        
        retHtml = "app/subColor.html"
    elif (requestName == "/threshold/"): # 4. 二値化のとき
        useFilter = FilterThreshold(dstPath)
        if (hasFileData): # ファイルデータが届いていないとき  
            useFilter.makePictureForMember()
        retHtml = "app/threshold.html"
    elif (requestName == "/gauss/"): # 5. ガウスぼかしのとき
        useFilter = FilterGauss(dstPath)
        if (hasFileData): # ファイルデータが届いていないとき  
            deviation = int(request.POST.get("deviation"))
            kernel = int(request.POST.get("kernel"))
            useFilter.setDeviation(deviation)
            useFilter.setKernel(kernel)
            useFilter.makePictureForMember()
        else:
            deviation = 31
            kernel = 31
        addDict = {
            "deviation" : deviation,
            "kernel" : kernel,
        }
        retHtml = "app/gauss.html"
    if (hasFileData): # ファイルデータが届いていないとき
        cv2.imwrite(dstPath, useFilter.getImage())
    filterAlias = useFilter.getFilterAlias()
    fm = FilterManagement(useFilter.getFilterName())
    explain = fm.getExplain()
    retBaseDict = {
            'title': "画像加工アプリ～巨匠～",
            'year': datetime.now().year,
            'form' : form,
            'srcPath' : srcPath.lstrip("."),# ./mediaではだめ。/mediaにしないといけない
            'dstPath' : dstPath.lstrip("."),# ./mediaではだめ。/mediaにしないといけない
            'filterAlias' : filterAlias,
            'explain' : explain,
        }
    retBaseDict.update(addDict)
    return render(
        request,
        retHtml, # は変数名とテンプレート名をそろえること
        retBaseDict
    )

# contactについてのview
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

# aboutについてのview
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

# テストのフォーム関数ビュー
def modelFormUpload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    else:
        form = DocumentForm()
    return render(request, 'app/modelFormUpload.html', {
        'form': form
    })
 



# 各フィルターのベースになる関数ベースビュー
"""
def home(request):
    assert isinstance(request, HttpRequest)
    post = request.POST
    if request.method == 'POST':
        # フォームのひな型をforms.pyモジュールから作成する
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    # DBのクエリセットを取得する。
    obj = Document.objects.all()
    # アップロードされた画像のデータを取得する。
    objLast = obj[len(obj) - 1]
    # ファイル名を取得する。
    #(改良の余地あり)
    objPath = "." + objLast.photo.url
    # パスを除いたファイル名を得る
    fileName = os.path.splitext(os.path.basename(objPath))[0]
    filedata = request.FILES.get("avatar")
    mediaDir = "./media/"
    temporaryPath = mediaDir + "temporary/temporary.png"
    dstPath = ""
    #変換用画像を作成する(ファイルフォーマットは選べるようにする)
    if (len(filedata) !=0):
        with open(temporaryPath, "wb+") as f:
            for chunk in filedata:
                f.write(chunk)
    if ("gray" in request.POST): # グレー変換のとき
        gray(temporaryPath)
        objLast.filterPhoto = "filter/gray/gray.jpg"
        dstPath = mediaDir + "filter/gray/gray.jpg"
    elif ("threshold" in request.POST): # 二値化のとき
        filterThreshold = FilterThreshold(temporaryPath)
        filterThreshold.makePictureForMember()
        outPath = "filter/threshold/threshold.jpg"
        dstPath = mediaDir + outPath
        cv2.imwrite(mediaDir + outPath, filterThreshold.getImage())
        objLast.filterPhoto = outPath
    elif ("mosaic" in request.POST): # モザイクの時
        filterMosaic = FilterMosaic(temporaryPath)
        filterMosaic.makePictureForMember()
        outPath = "filter/mosaic/mosaic.jpg"
        dstPath = mediaDir + outPath
        cv2.imwrite(mediaDir + outPath, filterMosaic.getImage())
        objLast.filterPhoto = outPath
    elif ("dotArt" in request.POST): # ドット絵風の時
        filterDotArt = FilterDotArt(temporaryPath)
        filterDotArt.makePictureForMember()
        outPath = "filter/dotArt/dotArt.jpg"
        dstPath = mediaDir + outPath
        cv2.imwrite(mediaDir + outPath, filterDotArt.getImage())
        objLast.filterPhoto = outPath
    elif ("subColor" in request.POST): # 減色の時
        filterSubColor = FilterSubColor(temporaryPath)
        filterSubColor.makePictureForMember()
        outPath = "filter/subColor/subColor.jpg"
        dstPath = mediaDir + outPath
        cv2.imwrite(mediaDir + outPath, filterSubColor.getImage())
        objLast.filterPhoto = outPath
    objLast.save()
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year': datetime.now().year + 3,
            'form' : form,
            'obj' : objLast,
            'dstPath' : dstPath,
        }
    )
"""


"""
def edit(request, num):    
    obj = Document.objects.get(id = num)
    if request.method == 'POST':
        if 'button_gray' in request.POST:
            gray(obj.photo.url)
            obj.gray = "gallery/gray.jpg" # モデルと対応している
            obj.save()
            return redirect('app:edit')
#            return redirect('app:index')
    params = {'data': obj}
    return render(request, 'app/edit.html', params)
#    return render(request, 'app/index.html', params)
"""

