import requests, json

token = 'secret_5R2jGvFVR1da9C59UcfPTA1pxMisRWoo7vuSpkDWWh1'

databaseID = 'dc0305243e14444caeb8aefaa249026d'

headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2022-06-28"
}

def readDatabase(databaseID, headers):
    readUrl = 'https://api.notion.com/v1/databases/' + databaseID

    res = requests.request("GET", readUrl, headers=headers)

    data = res.json()
    print(data)
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
        print("e")


def createPage():
    pass


def updatePage():
    pass

if __name__ == "__main__":
    readDatabase(databaseID, headers)
