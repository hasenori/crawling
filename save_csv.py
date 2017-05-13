#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv

#ファイルを書き込み用に開く。newline=""として改行コードの自動変換を抑制する。
with open('top_cites.csv', 'w', newline='') as f:
    writer = csv.writer(f) # csv.writerはファイルオブジェクトを引数に指定する
    writer.writerow(['rank','city','population']) #1行目のヘッダーに出力する
    writer.writerow([
        [1,'上海',24150000],
        [2,'カラチ',23150000],
        [3,'北京',22150000],
        [4,'天津',21150000]
    ])
