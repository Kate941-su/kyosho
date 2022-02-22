from django.db import models
# 画像のアップロードに関するモデルクラス
class Document(models.Model):
    # コメント記入欄
    description = models.CharField(max_length = 255, blank = True)
    # ファイルのアップロード先を(documents/)にする。
    document = models.FileField(upload_to = 'documents/')
    # 写真をアップロードする
    photo = models.ImageField(upload_to='gallery/', default='SOME STRING')
    # アップロードした時刻
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # ImageFiled->画像をデータベースで扱うためのクラス
    filterPhoto = models.ImageField(default='Not Set') # グレースケール返還後の画像

