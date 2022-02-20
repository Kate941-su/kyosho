"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length = 255, blank = True)
    # ファイルのアップロード先を(documents/)にする。
    document = models.FileField(upload_to = 'documents/')
    uploaded_at = models.DateTimeField(auto_now_add = True)
