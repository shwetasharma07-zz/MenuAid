########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

#Fom StringIO import StringIO

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '7dd603b705df4c1790ba46d36d8a3458',
}

#http://www.greenislecare.com/sample-menu.jpg

def readMenuItems(URL):
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1/ocr", "{'Url': "+URL+"}", headers)
    response = conn.getresponse()

    data = response.read().decode('utf-8')
    conn.close()
    
    obj = json.loads(data)

    
    #print(obj["regions"][0]["lines"][0]  ['words'][0]['text'])
    #print(obj["regions"][0]["lines"][1]  ['words'][0]['text'], obj["regions"][0]["lines"][1]['words'][1]['text'])
    
    menuList = list()
    k=0
    menu = obj['regions']
    for region in menu:
    
        region = obj["regions"][k]["lines"]
        j = 0
    
        for line in region:
            ####ONE LINE###
            line = obj["regions"][k]['lines'][j]['words']
            i = 0
            lineText = ""
            for word in line:
                lineText +=(" "+str(line[i]['text']).lower())
                i = i + 1
            #print(lineText)
            
            ########
            j = j + 1
            menuList.append(lineText)
        k = k + 1
        #menuList.append(lineText)
    
    return menuList


