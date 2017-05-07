#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from urllib.request import Request, urlopen
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

url_request = Request('https://gihyo.jp/dp', headers=headers)
f = urlopen(url_request)

encodding = f.info().get_content_charset(failobj="utf-8")
print('encodding',encodding,file=sys.stderr) # エンコーディングを芳醇エラー出力に出力する
text = f.read().decode(encodding) # 得られたエンコーディングを指定して文字列にデコードする
print(text) # デコードしたレスポンスボディを標準出力に出力する
