#すでに作成されているイメージの中から、どのイメージを使うかを指定する。
FROM python:3.7
#環境変数を設定する
ENV PYTHONUNBUFFERED 1
#RUN コマンドを実行する
RUN mkdir /code
#ワーキングディレクトリ(カレント)を指定する
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#ホストPC ( Mac ) のプロジェクトルート ( Dockerfile が配置されている階層 )以下の
#全てのディレクトリ/ファイルが、後ほど生成されるコンテナへとコピーされます。
COPY . /code/

EXPOSE 8000