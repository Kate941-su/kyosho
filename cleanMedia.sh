#!/bin/bash
# mediaディレクトリ内をクリーンアップするバッチファイル（本番環境：Linux用）
# タスクスケジューラで定期的にクリーンアップを行う必要がある(一日に一回？？, anacrontabで管理するか？?, 頻度もアクセス数と相談)
rmdir -r ./media
mkdir media