from pymongo import *

# connection to the mongo server
client = MongoClient('10.56.133.13',27017)
# selecting the db
db = client['sneha']
# selecting the collection
col = db['flipkart']

def main():
    # reading the collection
    for doc in col.find({}):
        # print(doc['link'])
        print(doc['brand'])

if __name__ == '__main__':
    main()
