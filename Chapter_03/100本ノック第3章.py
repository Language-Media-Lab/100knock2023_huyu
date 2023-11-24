#20-----------------------------------------------
print(20)

import pandas as pd
wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
print (uk)

#21-----------------------------------------------
print(21)

import pandas as pd
import re

#reはPythonの正規表現モジュールで文字列に対するパターンマッチングや検索、置換などの操作を
#提供している。正規表現はテキストデータ内で特定のパターンを見つけたり置換したりするのに役立つ


pattern = re.compile('Category')
wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    if re.search(pattern, line):
#re.search(pattern,string)は文字列内でパターンと一致する最初の箇所を検索する
        print (line)


#22------------------------------------------------
print(22)

import pandas as pd
import re
wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    if re.search(pattern, line):
        line = line.replace('[[','').replace('Category:','').replace(']]','').replace('|*','').replace('|元','')
        print (line)

#23------------------------------------------------------
print(23)

import pandas as pd
import re
pattern = re.compile('^=+.*=+$') # 1回以上の=で始まり、1回以上の=で終わる文字列
wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    if re.search(pattern, line):
        level = line.count('=') // 2 - 1
        print(line.replace('=',''), level )


#24------------------------------------------------------
print(24)

import pandas as pd
import re
pattern = re.compile('File|ファイル:(.+?)\|')
#「File」または「ファイル:」の後に何らかの文字列（(.+?)）が続き、それが「|」で終わるパターンを探します。
#(.+?)は何らかの1文字以上の文字列を示しており、?は直前の文字列が最小回数で合致することを示しています（これをlazy quantifierといいます）。
#したがって、このコードは「File」とか「ファイル:」で始まり、「|」で終わる何らかの文字列を取り出すためのパターンを定義しています。その際、取り出す文字列の両端の「File」、「ファイル:」、「|」は含まれません。

wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    r = re.findall(pattern, line)
    if r:
        print (r[0])

#25------------------------------------------------------
print(25)

import pandas as pd
import re
pattern = re.compile('\|(.+?)\s=\s*(.+)')
#DataFrameに変換、Linesは複数の行に対して読み込むときに利用する
#'|'の後に一つ以上の任意の文字が続き、その後に空白が0個以上、等号、空白が0個以上、一つ以上の任意の文字が続くパターンを見つけるためのコード

wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
ls = uk[0].split('\n')
d = {}
for line in ls:
    r = re.search(pattern, line)
    if r:
        d[r[1]]=r[2]
print (d)

#26--------------------------------------------------------
print(26)

import pandas as pd
import re
pattern = re.compile('\|(.+?)\s=\s*(.+)')
p_emp = re.compile('\'{2,}(.+?)\'{2,}')
#2つ以上の連続するシングルクォーテーションで挟まれた部分をマッチングパターンとしてコンパイルしています。具体的には、強調表現を示すためのシングルクォーテーション 2,3,5回のパターンを見つけてきます。
wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
ls = uk[0].split('\n')
d = {}
for line in ls:
    r = re.search(pattern, line)
    if r:
        d[r[1]]=r[2]
    r = re.sub(p_emp,'\\1', line)
#上記で用意したパターン（p_emp）を指定して、`line`の中のそれにマッチする部分を置換しています。置換する文字列として`'\\1'`が指定されているので、マッチしたパターンのうち正規表現内でグループ化されている部分（この場合は強調マークで挟まれた部分）をそのままの文字列として残しつつ、強調マーク（シングルクォーテーション）の部分が削除されます。

    print (r)
print (d)

#27----------------------------------------------------------
print(27)

import pandas as pd
import re
pattern = re.compile('\|(.+?)\s=\s*(.+)')
p_emp = re.compile('\'{2,}(.+?)\'{2,}')
p_link = re.compile('\[\[(.+?)\]\]')
#`[[`と`]]`で挟まれた部分をマッチングパターンとしてコンパイルしています。具体的には、ウィキペディアなどのマークアップ言語で使われるリンクを示すパターンを見つけてきます。

wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
lines = uk[0]
lines = re.sub(p_emp,'\\1', lines)
lines = re.sub(p_link,'\\1', lines)
ls = lines.split('\n')
d = {}
for line in ls:
    r = re.search(pattern, line)
    if r:
        d[r[1]]=r[2]
print (d)


#28-------------------------------------------------------------
print(28)

import pandas as pd
import re
pattern = re.compile('\|(.+?)\s=\s*(.+)')
p_emp = re.compile('\'{2,}(.+?)\'{2,}')
p_link = re.compile('\[\[(.+?)\]\]')
p_refbr = re.compile('<[br|ref][^>]*?>.+?<\/[br|ref][^>]*?>')
#`<br>`または`<ref>`で始まり、`</br>`または`</ref>`で終わる部分をマッチングパターンとしてコンパイルしています。具体的には、HTMLやXMLなどのマークアップ言語で使われる改行（br）や参照（ref）を示すタグを見つけてきます。

wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
lines = uk[0]
lines = re.sub(p_emp,'\\1', lines)
lines = re.sub(p_link,'\\1', lines)
lines = re.sub(p_refbr,'', lines)
ls = lines.split('\n')
d = {}
for line in ls:
    r = re.search(pattern, line)
    if r:
        d[r[1]]=r[2]
print (d)

#29-----------------------------------------------------------------------
print(29)

import pandas as pd
import re
import requests
pattern = re.compile('\|(.+?)\s=\s*(.+)')
wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
ls = uk[0].split('\n')
d = {}
for line in ls:
    r = re.search(pattern, line)
    if r:
        d[r[1]]=r[2]
        
S = requests.Session()
URL = "https://commons.wikimedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "File:" + d['国旗画像'],
    "prop": "imageinfo",
    "iiprop":"url"
}
R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']
for k, v in PAGES.items():
    print (v['imageinfo'][0]['url'])

