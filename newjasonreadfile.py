import json

with open('readfile.json') as json_data:
    data = json.load(json_data)

    for r in data['Biodata']:
    fo = open(r['id']+"_"+r['name']+".txt","wb")
    fo.write(r['name'] + "   " + r['email'] + "    " +r['city'])
    fo.close()
    print(data)
    
