"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
# フォームモジュールから特定のクラスをインポートする
from .forms import DocumentForm
from .models import Document
import cv2
from django.conf import settings

# home関数ビュー
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
    obj = Document.objects.all()
    objLast = obj[len(obj) - 1]
    if ("gray" in request.POST):
        gray(objLast.photo.url)
        # フィールドの内容を書き換える。
        objLast.gray = "gray/gray.jpg" 
    objLast.save()
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year': datetime.now().year + 3,
            'form' : form,
            'obj' : objLast,
        }
    )

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

def gray(url):
    path = "." + url
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    try:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        return
    output = "./media/gray/gray.jpg"
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

