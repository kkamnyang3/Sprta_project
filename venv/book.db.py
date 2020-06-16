from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mydatabase
doc = {
    'name': name,
    'img_url': img_url,
    'recent': recent,
    'url': url,
    'like': 0,
    'active': 1
}
db.mycollection.insert_one(doc)
print('완료!', name)

# moviestar에서 긁어온거
# book data에 맞게 변형하기