import json

while(True):    
    try:
        fileName = input("Enter file name : ")
        with open(fileName) as f:
            data = json.load(f)
        break
    except Exception as e:
        print("Invalid file Name.File not present in current directory.")
        continue

def getJsonData(key,value):
    if(isinstance(value,(str,bool,int)) or value is None):
        tempDict = {}
        data_dict = {"description":"","type":"string","example":value}
        tempDict[key] = data_dict
        return tempDict
    if(isinstance(value,dict)):
        tempDict = {}
        data_dict = {"type":"object","properties":{}}
        for key2,value2 in value.items():
            data_dict['properties'].update(getJsonData(key2,value2))
        tempDict[key] = data_dict
        return tempDict
    if(isinstance(value,list)):
        tempDict = {}
        data_dict = {"type":"array","items":{"oneOf":[]}}
        for val in value:
            data_dict2 = {"type":"object","properties":{}}
            data_dict["items"]["oneOf"].append(data_dict2)
            for key2,value2 in val.items():
                data_dict2["properties"].update(getJsonData(key2,value2))         
        tempDict[key] = data_dict
        return tempDict

result = {"type":"object","properties":{}}
for key,value in data.items():
    result["properties"].update(getJsonData(key,value))
        
with open(fileName.split('.')[0]+'_schema.json', 'w') as fp:
    json.dump(result, fp)

print(fileName.split('.')[0]+'_schema.json'+' file generated successfully')
