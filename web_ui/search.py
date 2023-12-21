import json, pickle, os
import numpy as np

from vertexai.language_models import TextEmbeddingModel
from google.cloud import aiplatform
from google.oauth2 import service_account

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cres.json'
credentials = service_account.Credentials.from_service_account_file('cres.json')
aiplatform.init(credentials=credentials)
model = TextEmbeddingModel.from_pretrained("textembedding-gecko-multilingual@001")
data=pickle.load(open('./data/embeddings.pkl','rb'))

def search(text, pattern="default"):
    if pattern =="default":
        return "これはテンプレの回答です。"
    elif pattern =='top':
        return f"『{data[0][0]}』がおすすめです。『{data[0][1]}』という記載がありました。"
    elif pattern=='embeddings':
        embedding = model.get_embeddings([text])[0].values
        output=sorted(data,key=lambda x: -np.dot(embedding,x[2])+np.linalg.norm(x[2]))
        return f"『{output[0][0]}』がおすすめです。『{output[0][1]}』という記載がありました。"
