import json, csv

def parse_mt_export(file_path):
    output=[]
    with open(file_path, 'r') as file:
        articles = file.read().split('--------\n')
        for article in articles:
            if article.strip() == '':
                continue
            article_data = parse_article(article)
            output.append(article_data)
    return output

def parse_article(article):
    sections = article.split('-----\n')
    metadata = {}
    for section in sections:
        lines = section.split('\n')
        if lines[0] in ['BODY:', 'EXTENDED BODY:', 'EXCERPT:']:
            metadata[lines[0][:-1].replace(' ', '_').lower()] = '\n'.join(lines[1:])
        else:
            for line in lines:
                if line and ': ' in line:
                    key, value = line.split(': ', 1)
                    metadata[key.lower().replace(' ', '_')] = value
    return metadata

# ファイルパスを指定してください
file_path = './data/hatena.txt'



# JSONLファイルにデータを書き込み
with open(file_path.replace(".txt",".jsonl"), 'w', encoding='utf-8') as file:
    for item in parse_mt_export(file_path):
        json_line = json.dumps(item)
        file.write(json_line + '\n')
