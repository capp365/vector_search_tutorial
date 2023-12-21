import json
from bs4 import BeautifulSoup
import os
import google.generativeai as palm
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cres.json'
palm.configure()

model = "models/embedding-gecko-001"



def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'lxml')
    text = ''

    # 特定のタグで改行を挿入
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        tag_text = tag.get_text(strip=True)
        # ピリオド「。」で分割し、改行を追加
        sentences = tag_text.split('。')
        text += '。\n'.join(sentences) + '\n'

    # 各行をリストとして分割
    lines = text.split('\n')

    # 空行を除去
    lines = [line for line in lines if line.strip()]

    return lines

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
count=0
output=[]
for item in data:
    if item['status']=="Publish":
        lines=extract_text_from_html(item["body"])
        if "extended_body" in item:
            lines +=extract_text_from_html(item["extended_body"])
        # 出力
        for line in lines:
            count+=len(line)
            while(True):
                try:
                    embedding = palm.generate_embeddings(model=model, text=line)
                    print(item['title'],line)
                    output.append((item['title'],line,embedding))
                    break
                except:
                    pass


print(count)

import pickle
pickle.dump(output,open('./data/embeddings.pkl','wb'))