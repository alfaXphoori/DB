from pymongo.mongo_client import MongoClient
import pymongo

try:
    uri = "mongodb+srv://user:pass@cluster0.ngazyzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    database = client["CeDB"]
    collection = database["PicoW"]
    result = collection.insert_one({ 
            "DeviceID" : 102,
            "Temperature": 33.33 
            })
    print(result.acknowledged)
    client.close()
    
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

