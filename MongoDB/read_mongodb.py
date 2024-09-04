from pymongo.mongo_client import MongoClient
import pymongo

try:
    uri = "mongodb+srv://user:pass@cluster0.ngazyzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    database = client["CeDB"]
    collection = database["PicoW"]
    result = collection.find_one({ "DeviceID" : 102 })
    print(result)
    client.close()
    
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

