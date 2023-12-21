import os
import google.generativeai as palm
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cres.json'
palm.configure()

model = "models/embedding-gecko-001"
text = "Your text here"
embedding = palm.generate_embeddings(model=model, text=text)
print(embedding)
models = [m for m in palm.list_models()]
#model = models[0].name
print([i.name for i in models])