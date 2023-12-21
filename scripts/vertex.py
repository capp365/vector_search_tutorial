from google.cloud import aiplatform
from google.cloud import aiplatform_v1
from google.oauth2 import service_account
from vertexai.language_models import TextEmbeddingModel
from google.cloud.aiplatform import gapic
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cres.json'

credentials = service_account.Credentials.from_service_account_file('cres.json')

aiplatform.init(credentials=credentials)

def text_embedding() -> list:
    """Text embedding with a Large Language Model."""
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")

    embeddings = model.get_embeddings(["What is life?"])
    for embedding in embeddings:
        vector = embedding.values
        print(f"Length of Embedding Vector: {len(vector)}")
    return vector

if __name__ == "__main__":
    text_embedding()