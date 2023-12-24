import json
from bs4 import BeautifulSoup
import os

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'lxml')
    text = ''

    # 特定のタグで改行を挿入
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        text = tag.get_text(strip=True)
        
    return text

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # JSON文字列を辞書に変換
            data.append(json.loads(line))
    return data


# HTMLファイルのパスを指定
file_path = './data/hatena.jsonl'
data=read_jsonl(file_path)

# 読み込んだデータを表示
output={}
for item in data:
    if item['status']=="Publish":
        text=extract_text_from_html(item["body"])
        if "extended_body" in item:
            text +=extract_text_from_html(item["extended_body"])
        output[item['title']]=text
        print(item['title'])

import pickle
pickle.dump(output,open('./data/articles.pkl','wb'))