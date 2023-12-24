from flask import Flask, render_template, request
from flask import jsonify
from search import search


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    input_text = request.form['input_text']
    result = process_input(input_text)  # 入力に基づいて何らかの処理を行う
    return jsonify({'result': result})


def process_input(input_text):
    output_text=search(input_text,pattern='llm')
    return output_text

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
