"""
Definition of forms.
"""

from django import forms
# モデルモジュールからDocumentクラスをインポートする
from .models import Document
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

# ログイン画面のフォームを扱うクラス
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
                                   
# 画像をポストするフォーム扱うクラス
class DocumentForm(forms.ModelForm):
    #nameをrequired = Falseにする
    def __init__(self, *args, **kwd):
        super(DocumentForm, self).__init__(*args, **kwd)
        self.fields["photo"].required = True
    class Meta:
        model = Document
        fields = ('description', 'photo', )