from vertexai.language_models import ChatModel, InputOutputTextPair
from google.cloud import aiplatform
from google.cloud import aiplatform_v1
from google.oauth2 import service_account
from vertexai.language_models import TextEmbeddingModel
from google.cloud.aiplatform import gapic
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cres.json'

credentials = service_account.Credentials.from_service_account_file('cres.json')

aiplatform.init(credentials=credentials)
chat_model = ChatModel.from_pretrained("chat-bison@002")

chat = chat_model.start_chat(
    # Optional parameters, such ase top_p, top_k, temperature, max_output_tokens,
    # aren't specified in this example
    context="僕はブログの妖精！最高の回答をするよ",
    examples=[
        InputOutputTextPair(
            input_text="記事を渡せばそのレビューをしてくれる？",
            output_text="まかせて",
        ),
        InputOutputTextPair(
            input_text="どんな記事でも？",
            output_text="あまりよくない記事はダメだよ",
        ),
    ],
)

print(chat.send_message("その前に好きな食べ物を教えて").text)