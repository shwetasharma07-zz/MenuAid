########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

#Fom StringIO import StringIO

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '7dd603b705df4c1790ba46d36d8a3458',
}



def ReadMenuItems():
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1/ocr", "{'Url': 'http://www.greenislecare.com/sample-menu.jpg'}", headers)
    response = conn.getresponse()

    data = response.read().decode('utf-8')
    conn.close()
    
    obj = json.loads(data)

    
    #print(obj["regions"][0]["lines"][0]  ['words'][0]['text'])
    #print(obj["regions"][0]["lines"][1]  ['words'][0]['text'], obj["regions"][0]["lines"][1]['words'][1]['text'])
    
    menuList = list()
    
    region = obj["regions"][0]["lines"]
    j = 0
    regionText = ""
    for line in region:
        ####ONE LINE###
        line = obj["regions"][0]['lines'][j]['words']
        i = 0
        lineText = ""
        for word in line:
            lineText +=(" "+line[i]['text'])
            i = i + 1
        print(lineText+";")
        menuList.append(lineText)
        ########
        j = j + 1







  #  secondLine = obj["regions"][0]["lines"][0]
    

   # for i in range(0, secondLine.size()-1):
 #       word = obj["regions"][0]["lines"][i]
 #       print(word)
    
    #print(line)
   # print(obj['regions'][0]['lines'][1]['words'][0]['text'])

    

ReadMenuItems()

####################################
