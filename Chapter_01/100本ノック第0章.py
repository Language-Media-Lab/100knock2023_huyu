#00----------------------------------------------------
print(0)

mojiretsu = "strssed"
mojiretsu_reversed = ''.join(list(reversed(mojiretsu)))

print(mojiretsu_reversed)


#01----------------------------------------------------
print(1)

one = "パタトクカシーー"
one2 = ""        #空の文字列を初期化
for i in range(0,7,2):
    one2 += one[i]   #文字列の連結

print(one2)

#02----------------------------------------------------
print(2)

part1 = "パトカー"
part2 = "タクシー"
second = ""

for i in range(len(part1)):
    second += part1[i] + part2[i]

print(second)

#03----------------------------------------------------
print(3)

eibun = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

def split_string_by_space(input_string):
    # 空白で文字列を分割
    words = input_string.split()

    # 結果をリストに格納
    result_list = []
    for word in words:
        result_list.append(word)

    return result_list

def get_string_lengths(input_list):
    # 各文字列の長さを格納するリストを初期化
    lengths = []

    # 各文字列の長さを取得してリストに格納
    for word in input_list:
        lengths.append(len(word))

    return lengths

ans = get_string_lengths(split_string_by_space(eibun))
print(ans)


#eibun = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#eibun = eibun.replace(',','').replace('.','')
#print([len(w) for w in eibun.split()])


#04----------------------------------------------------
print(4)

def split_string_by_space(input_string):
    return input_string.split()

gennso = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

gennso_jisyo = {}

gennso_list = split_string_by_space(gennso.replace(".", ""))
print(gennso_list)

for i, word in enumerate(gennso_list, 1):
    if i == 1 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 15 or i == 16 or i == 19:
        #if i in [1,5,6,7,8]でもできる
        gennso_jisyo[i] = word[0]
    else:
        gennso_jisyo[i] = word[:2]

print(gennso_jisyo)


#05-------------------------------------------------

def generate_ngram(sequence, n):
    """
    与えられたシーケンスからn-gramを生成する関数
    """
    ngram_list = []
    
    #入力がリスト型であるか文字列型であるかの判別をisinstance関数で行う

    # 単語bi-gram
    if isinstance(sequence, str):
        words = sequence.split()  #split関数は引数指定なしで空白文字で区切るようになっている
        ngram_list.extend([(words[i], words[i + 1]) for i in range(len(words) - 1)])
    
    # 文字bi-gram
    elif isinstance(sequence, list):
        ngram_list.extend([(sequence[i], sequence[i + 1]) for i in range(len(sequence) - 1)])
    
    return ngram_list

# テスト文
text = "I am an NLPer"
print(5)

# 単語bi-gram
word_bigrams = generate_ngram(text, 2)
print("単語bi-gram:", word_bigrams)

# 文字bi-gram
char_bigrams = generate_ngram(list(text), 2)
print("文字bi-gram:", char_bigrams)


#06-------------------------------------------------

def generate_ngram2(sequence, n):
    """
    与えられたシーケンスからn-gramを生成する関数
    """
    ngram_list = []
    
    # 文字bi-gram
    if isinstance(sequence, str):
        sequence = sequence.replace(" ", "")  # 空白を除去
        ngram_list.extend([sequence[i:i + n] for i in range(len(sequence) - n + 1)])
    #ngram_listにi からn番目の隣接するn文字を抽出して格納していく

    return ngram_list

def union_of_lists(list1, list2):
    # リストからセットを作成し、和集合を取得
    set1 = set(list1)
    set2 = set(list2)
    union_set = set1.union(set2)

    # セットからリストに変換
    union_list = list(union_set)

    return union_list

def difference_of_lists(list1, list2):
    # リストからセットを作成し、差集合を取得
    set1 = set(list1)
    set2 = set(list2)
    difference_set = set1.difference(set2)

    # セットからリストに変換
    difference_list = list(difference_set)

    return difference_list

def intersection_of_lists(list1, list2):
    # リストからセットを作成し、積集合を取得
    set1 = set(list1)
    set2 = set(list2)
    intersection_set = set1.intersection(set2)

    # セットからリストに変換
    intersection_list = list(intersection_set)

    return intersection_list



mojiX = "paraparaparadise"
mojiY = "paragraph"

X = generate_ngram2(mojiX, 2)
Y = generate_ngram2(mojiY, 2)

wa = union_of_lists(X,Y)
sa = difference_of_lists(X, Y)
seki = intersection_of_lists(X, Y)

print(6)
print(wa)
print(sa)
print(seki)


#07--------------------------------------------------

def tenki(x,y,z):
    print(x,"時の",y,"は",z)
    return 0

print(7)
tenki(12,"気温",22.4)

#08--------------------------------------------------

def cipher(text):
    result = ""
    for char in text:
        if char.islower():#文字列が小文字かどうかを判定し小文字の場合にTrueを返す
            # 英小文字の場合、(219 - 文字コード)の文字に置換
            result += chr(219 - ord(char))#Unicodeコードポイントに対応する文字を返す
            #ordは指定された文字のUnicodeコードポイントを返す
        else:
            # その他の文字はそのまま出力
            result += char
    return result

# テスト用のメッセージ
message = "Hello, World!"

print(8)

# メッセージを暗号化
encrypted_message = cipher(message)
print("暗号化されたメッセージ:", encrypted_message)

# 暗号化されたメッセージを復号化
decrypted_message = cipher(encrypted_message)
print("復号化されたメッセージ:", decrypted_message)


#09--------------------------------------------------------

import random

def randomize_word(word):
    # 単語の2文字目から最後から2番目までの文字をリストに変換
    chars_to_shuffle = list(word[1:-1])

    # リストをランダムにシャッフル
    random.shuffle(chars_to_shuffle)

    # 元の単語の2文字目と最後から2番目を結合し、シャッフルした文字を挿入する
    randomized_word = word[0] + ''.join(chars_to_shuffle) + word[-1]

    return randomized_word

# テスト用の文章
tekisuto = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# 文章を単語ごとに分割
words = tekisuto.split()

result = []

# 各単語の2文字目から最後から2番目までの文字をランダムに入れ替える
for i, word in enumerate(words):
    if len(word) > 4:
        result.append(randomize_word(word))
    else:
        result.append(word)

# 結果を表示
print(9)
print("元の文章:", tekisuto)
print("入れ替えた単語:", ' '.join(result))






