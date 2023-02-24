# 画像加工アプリ～巨匠～
- 画像ファイルをアップロードすることで、様々なエフェクトをつけることができるWebアプリ
- AIライブラリを導入して人の顔をアニメ風に編集することも可能
- ほかにも様々な加工が可能

# ビルドの仕方
- プロジェクトルートがDjangoWebProject1(以降root)。プロジェクトの設定（DBやwebサーバー等）がされているディレクトリがroot/DjangoWebProject1内にある。root/mange.pyはDBの更新、サーバーの起動を担う
- python mangate.py runserverでlocalhost::8000が立ち上がる。
- root/app内にアプリケーション側のファイルが入っている。
- フィルターはroot/app/opencvFilter/Filtersに入っている → Developは自由に使ってよいFiltersには英語名で完成したものを入れる。
- webで動かす前にテストしたいときはroot/opencvFilter/Filter内にFilter○○.pyを配置してtest.pyに記述してテストを行う。

# 仮想環境
- kyoshoenvをactivateすることで一発で環境が整う（はず）。
- kyoshoenvの環境内のpip installされているものはrequirements.txtに記載されている。下のパッケージを仮想環境にインストールする必要がある。
- Vscodeのデバッグモードでactivateからサーバーの立ち上げまで行ってくれる。Vscodeでrootディレクトリを開いてf5を押せばよい
