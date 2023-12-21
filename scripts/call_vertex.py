from vertexai.language_models import TextEmbeddingModel
from google.cloud import aiplatform
import os
#palm.configure()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cres.json'
aiplatform.init()

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