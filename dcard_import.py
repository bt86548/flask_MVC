import json

with open('./dcard.json','r',encoding='utf-8') as f:
    #讀取json檔案
    s = f.read()

#將s轉換為dict or list,json_data用list接收
json_data = json.loads(s)
print(type(json_data))
print(type(json_data[0]))