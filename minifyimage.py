import requests,json

def tinify(url):
    file = requests.get(url, stream=True)
    payload = file.raw
    headers = {
    'accept': "application/json",
    'content-type': "image/png",
    'origin': 'https://tinypng.com',
    'referer': 'https://tinypng.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    urll = "https://tinypng.com/web/shrink"
    response = requests.request("POST", urll, data=payload, headers=headers)
    x=json.loads(response.text)
    x["output"]["url"]=x["output"]["url"]+"/"+url.split("/")[-1]
    return json.dumps(x)
