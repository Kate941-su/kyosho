#すでに作成されているイメージの中から、どのイメージを使うかを指定する。
FROM python:3.8
#環境変数を設定する
ENV PYTHONUNBUFFERED 1
#RUN コマンドを実行する
RUN mkdir /code
#ワーキングディレクトリ(カレント)を指定する
WORKDIR /code

COPY requirements.txt /code/
RUN apt update && apt-get upgrade -y
#RUN apt-get install -y libgl1-mesa-dev
#RUN pip install opencv-contrib-python
RUN pip install -r requirements.txt
#ホストPC ( Mac ) のプロジェクトルート ( Dockerfile が配置されている階層 )以下の
#全てのディレクトリ/ファイルが、後ほど生成されるコンテナへとコピーされます。
COPY . /code/

EXPOSE 8000