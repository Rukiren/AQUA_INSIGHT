import json

## Python 字典
python_dict = {
  'Name': "Jack",
  'Score': 99
}

## 存成JSON File
with open("python2json.json", 'w') as f:
  json.dump(python_dict, f)