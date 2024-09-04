import requests
import json
url = "https://ap-southeast-1.aws.data.mongodb-api.com/app/data-exhexou/endpoint/data/v1/action/insertOne"

payload = json.dumps({
    "collection": "PicoW",
    "database": "CeDB",
    "dataSource": "Cluster0",
    "document": {
        "DeviceID": 103,
        "Humidity" : 60
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 's7qXRUNAk7DVDWLkPfPeI4cOzhWsGVqDoRNV4Kqsynpkkx0zHVbxuul4BPJPfLD8',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)