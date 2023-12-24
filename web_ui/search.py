import json, pickle, os
import numpy as np

from vertexai.language_models import TextEmbeddingModel, ChatModel, InputOutputTextPair
from google.cloud import aiplatform
from google.oauth2 import service_account

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cres.json'
credentials = service_account.Credentials.from_service_account_file('cres.json')
aiplatform.init(credentials=credentials)
model = TextEmbeddingModel.from_pretrained("textembedding-gecko-multilingual@001")
chat_model = ChatModel.from_pretrained("chat-bison@002")
data=pickle.load(open('./data/embeddings.pkl','rb'))
article=pickle.load(open('./data/articles.pkl','rb'))

def get_chat(text, result):
    #article[result[0]]
    print(result[0])
    chat = chat_model.start_chat(
    context=f"あなたは検索システムに解釈を付与する役割を持っています。",
)
    return result[0]+"という記事がおすすめです。"+chat.send_message(f"{text}という要求に対してシステムが{result[0]}というタイトルの記事を返しました。その具体的な内容は{article[result[0]]}です。ユーザにこの記事のどこがおすすめが簡潔に説明してください。").text

def search(text, pattern="default"):
    if pattern =="default":
        return "これはテンプレの回答です。"
    elif pattern =='top':
        return f"『{data[0][0]}』がおすすめです。『{data[0][1]}』という記載がありました。"
    elif pattern=='embeddings':
        embedding = model.get_embeddings([text])[0].values
        output=sorted(data,key=lambda x: -np.dot(embedding,x[2])+np.linalg.norm(x[2]))
        return f"『{output[0][0]}』がおすすめです。『{output[0][1]}』という記載がありました。"
    elif pattern=='llm':
        embedding = model.get_embeddings([text])[0].values
        output=sorted(data,key=lambda x: -np.dot(embedding,x[2])+np.linalg.norm(x[2]))
        return get_chat(text, output[0])
