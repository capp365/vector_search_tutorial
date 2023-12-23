import json, os
import numpy as np
from datetime import datetime

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cres.json'

from vertexai.language_models import TextEmbeddingModel
from google.cloud import aiplatform
from google.oauth2 import service_account
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cres.json'

credentials = service_account.Credentials.from_service_account_file('cres.json')

aiplatform.init(credentials=credentials)



model = TextEmbeddingModel.from_pretrained("textembedding-gecko-multilingual@001")

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # JSONLファイルの各行をPythonの辞書に変換
            json_line = json.loads(line.strip())
            data.append(json_line)
    return data

# JSONLファイルのパスを指定
file_path = './data/output3.jsonl'

# ファイル読み込み
data = read_jsonl(file_path)
mini_data=[i for i in data if "2023/" in json.dumps(i)]
print(len(data))

print(len(mini_data))
print(json.dumps(mini_data[2023], ensure_ascii=False).replace('"','').replace(' ',''))
#embeddings = model.get_embeddings([json.dumps(i) for i in mini_data])
#embeddings = [i.values for i in embeddings]

#import pickle
#pickle.dump([i[0]|{"embedding":i[1]} for i in zip(mini_data, embeddings)],open("./horse_embeddings.pkl",'wb'))


#pickle.dump(mini_data,open('mini_json.pkl','wb'))
#print([i for i in data[10]])
#print([i for i in data[10]['成績'][0]])
#print(embeddings[0])