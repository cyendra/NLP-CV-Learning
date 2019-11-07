import json
import os
import pickle
def json_extract(msg):
    rs = []
    for po in msg:
        rs.extend(po['paragraphs'])
    return rs
def load_poet(file_path = '../chinese-poetry/json'):
    rs = []
    for filename in os.listdir(file_path):
        if filename.startswith('poet'):
            with open(os.path.join(file_path, filename)) as f:
                rs.extend(json_extract(json.loads(f.read())))
    return rs
rs=load_poet()
out = []
for x in rs:
    out.append(Converter('zh-hans').convert(x))
with open("../NLP-CV-Learning/data/poet", 'wb') as f:
    pickle.dump(out, f)

with open("../NLP-CV-Learning/data/poet.txt", 'w') as f:
    for x in out:
        f.write(x + '\n')
    