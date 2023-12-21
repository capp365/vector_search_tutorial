# vector_search_tutorial

テキスト埋め込みを用いた検索を触ってみたい。


## 各種数字

### Text Embeddings

 - [Vertex AI における生成 AI の料金](https://cloud.google.com/vertex-ai/docs/generative-ai/pricing?hl=ja)

テキスト埋め込みを得るのに1000文字あたり、

 - 入力: $0.0001 (オンライン)、$0.00008 (バッチ)
 - 出力: 無料

とのことなので、対象の文字数カウントしたら118645文字なので単純計算0.0001 (ドル) ✖️119 (千文字)=0.0119（ドル）でいいってことなのかな？
(ダッシュボード見る限りPaLM Text Bison Input/Output - Predictions使ってる気がする)
