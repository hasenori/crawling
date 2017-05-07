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
bytes_contents = f.read() # bytes型のレスポンスボディを一旦変数に格納する

# charsetはHTMLの最初のほうに書かれていると期待出来るので、
# レスポンスボディの先頭1024バイトをASCII文字列としてデコードする
scanned_text = bytes_contents[:1024].decode('ascii',errors='replace')

#デコードした文字列から正規表現でcharsetの値を抜き出す
match = re.search(r'charset=["\']?([\w-]+)',scanned_text)
if match:
    encodding = match.group()
else:
    encodding = 'utf-8' # charsetが明治されていない場合はUTF-8とする

print('encodding',encodding,file=sys.stderr) # 得られたエンコーディングを標準エラー出力に出力する

text = f.read().decode(encodding)
print(text) # レスポンスボディを標準出力に出力する

