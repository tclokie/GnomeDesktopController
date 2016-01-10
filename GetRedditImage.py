import json, urllib.request

def getJsonData(sub="EarthPorn", sort="hot"):
    hdr = { 'User-Agent' : 'I like to grab wallpapers for desktop backgrounds on GNOME.' }
    req = urllib.request.Request("https://www.reddit.com/r/"+sub+"/"+sort+"/.json", headers=hdr)

    jsonBytes = urllib.request.urlopen(req)
    jsonStr = jsonBytes.read()
    return json.loads(jsonStr.decode())


data = getJsonData()

print(data['data']['children'][0]['data']['preview']['images'][0]['source']['url'])

