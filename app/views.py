#2021/02/22 kitaya kaito
import cv2
import os
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.conf import settings
from .forms import DocumentForm
from .models import Document
from .opencvFilter.Filters.FilterDotArt import FilterDotArt
from .opencvFilter.Filters.FilterMosaic import FilterMosaic
from .opencvFilter.Filters.FilterSubColor import FilterSubColor
from .opencvFilter.Filters.FilterThreshold import FilterThreshold


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

def viewFilter(request):
    assert isinstance(request, HttpRequest)
    post = request.POST
    if request.method == 'POST':
        # フォームのひな型をforms.pyモジュールから作成する
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    # サブミットされたファイルデータ
    filedata = request.FILES.get("avatar")
    mediaDir = "./media/"
    # 出力先パス
    temporaryPath = mediaDir + "temporary/temporary.png"
    dstPath = ""
    outPath = ""
    #元画像を取得(ファイルフォーマットは選べるようにする)
    if (type(filedata) != type(None)):
        if (len(filedata) !=0):
            with open(temporaryPath, "wb+") as f:
                for chunk in filedata:
                    f.write(chunk)
    requestName = request.path
    useFilter = None
    retHtml = ""
    # リクエストに応じて適切なフィルターを適用する
    if (requestName == "/subColor/"): # 減色のとき
        useFilter = FilterSubColor(temporaryPath)
        if (type(filedata) != type(None)): # ファイルデータが届いていないとき  
            useFilter.makePictureForMember()
        retHtml = "app/subColor.html"
    elif (requestName == "/mosaic/"): # モザイクのとき
        useFilter = FilterMosaic(temporaryPath)
        if (type(filedata) != type(None)): # ファイルデータが届いていないとき  
            useFilter.makePictureForMember()
        retHtml = "app/mosaic.html"
    elif (requestName == "/threshold/"): # 二値化のとき
        useFilter = FilterThreshold(temporaryPath)
        if (type(filedata) != type(None)): # ファイルデータが届いていないとき  
            useFilter.makePictureForMember()
        retHtml = "app/threshold.html"
    elif (requestName == "/dotArt/"): # ドット絵風のとき
        useFilter = FilterDotArt(temporaryPath)
        if (type(filedata) != type(None)): # ファイルデータが届いていないとき  
            useFilter.makePictureForMember()
        retHtml = "app/dotArt.html"
        if (type(filedata) != type(None)): # ファイルデータが届いていないとき
            cv2.imwrite(temporaryPath, useFilter.getImage())
    filterName = useFilter.getFilterName()
    return render(
        request,
        retHtml,
        {
            'title':'Home Page',
            'year': datetime.now().year,
            'form' : form,
            'dstPath' : "/media/temporary/temporary.png",
            'filterName' : filterName
        }
    )



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
def gray(url):
    img = cv2.imread(url, cv2.IMREAD_UNCHANGED)
    try:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        return
    output = "./media/filter/gray/gray.jpg"
    cv2.imwrite(output, img_gray)

# contact関数ビュー
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

# about関数ビュー
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
        # フォームを
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    else:
        form = DocumentForm()
    return render(request, 'app/modelFormUpload.html', {
        'form': form
    })



"""
1 : ボタンが押されたら、元画像の保存場所を取得する
2 : gray関数内で元画像を読み込み、グレースケール変換する
3 : “gray.jpg”と言う名前でグレー画像を保存する
4 : グレー画像の場所を指定、save()でレコードの更新を行う
"""

