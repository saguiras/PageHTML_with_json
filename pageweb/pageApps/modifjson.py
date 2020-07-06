import json
from math import *

with open("C:/Users/julien/Documents/dentiste/pageweb/pageApps/static/pageApps/40623553813XP.json","r") as j:
  data = json.load(j)

def disease_intersection_tooth(data, item, newjson):

            x_disease = data[item]['pos']["x"];
            w_disease = data[item]['pos']["width"] + x_disease;
            y_disease = data[item]['pos']["y"];
            h_disease = data[item]['pos']["height"] + y_disease;

            x_disease_center = (x_disease + w_disease) / 2;
            y_disease_center = (y_disease + h_disease) / 2;

            for i in range(len(newjson)) :
                type = newjson[i]['type']
                
                
                if type == "anatomy" :
                    x_tooth = newjson[i]['pos']["x"];
                    w_tooth = newjson[i]['pos']["width"] + x_tooth;
                    y_tooth = newjson[i]['pos']["y"];
                    h_tooth = newjson[i]['pos']["height"] + y_tooth;

                    x_tooth_center = (x_tooth + w_tooth) / 2;
                    y_tooth_center = (y_tooth + h_tooth) / 2;


                    distance = sqrt(pow((x_tooth_center - x_disease_center), 2) + pow((y_tooth_center - y_disease_center), 2))

                    if i == 0:
                        bestdistance = distance
                        tooth = newjson[i]['subType'];
                    elif distance < bestdistance :
                        bestdistance = distance;
                        tooth = newjson[i]['subType'];
                    

            return tooth;

def modif_json(data) :
   newjson = []
   
   for item in range(len(data)) :
        type = data[item]['type']
        subType = data[item]['subType']

        if type == "anatomy" :
             newjson.insert(item,data[item])
             newjson[item]['disease'] = {}

        if type == "disease" :
                    if subType == "85" :
                        func = lambda x: newjson[x]['type'] == "d85"
                        i = index(newjson,func)
                        if i == None :
                            newjson.append({ "type": "d85","subType": "1" })
                        else :
                            newjson[i]['subType'] = str(1 + int(newjson[i]['subType']))

                    if subType == "10" :
                        tooth = disease_intersection_tooth(data, item, newjson)
                        func = lambda x: newjson[x]['type'] == "anatomy"  and newjson[x]['subType'] == tooth
                        i = index(newjson,func)
                        if 'caries' in newjson[i]['disease'] :
                            newjson[i]['disease']['caries'] += 1
                        else :
                            newjson[i]['disease']['caries'] = 1

                    if subType == "50" :
                        tooth = disease_intersection_tooth(data, item, newjson)
                        func = lambda x: newjson[x]['type'] == "anatomy"  and newjson[x]['subType'] == tooth
                        i = index(newjson,func)
                        if 'd50' in newjson[i]['disease'] :
                            newjson[i]['disease']['d50'] += 1
                        else :
                            newjson[i]['disease']['d50'] = 1
        
                       
   return newjson

def index(data,func):
    for i in range(len(data)):
        if func(i) :
            return i
    return None


modif_json(data)


