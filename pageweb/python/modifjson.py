import json
from math import *
from itertools import chain

with open("C:/Users/julien/Documents/dentiste/pageweb/pageApps/static/pageApps/40623553813XP.json","r") as j:
  data = json.load(j)

def disease_intersection_tooth(data, item):
            bestdistance = 20000;
            tooth = "0";
            x_disease = data[item]['pos']["x"];
            w_disease = data[item]['pos']["width"] + x_disease;
            y_disease = data[item]['pos']["y"];
            h_disease = data[item]['pos']["height"] + y_disease;

            x_disease_center = (x_disease + w_disease) / 2;
            y_disease_center = (y_disease + h_disease) / 2;

            for i in range(len(data)) :
                type = data[i]['type']
                
                
                if type == "anatomy" :
                    x_tooth = data[i]['pos']["x"];
                    w_tooth = data[i]['pos']["width"] + x_tooth;
                    y_tooth = data[i]['pos']["y"];
                    h_tooth = data[i]['pos']["height"] + y_tooth;

                    x_tooth_center = (x_tooth + w_tooth) / 2;
                    y_tooth_center = (y_tooth + h_tooth) / 2;


                    distance = sqrt(pow((x_tooth_center - x_disease_center), 2) + pow((y_tooth_center - y_disease_center), 2))

                    if distance < bestdistance :
                        bestdistance = distance;
                        tooth = data[i]['subType'];
                    

            return tooth;

def modif_json(data) :
   data.append({ "type": "d85","subType": "0" })
   item = 0
   lenght = len(data)
   while item < lenght:
        type = data[item]['type']
        subType = data[item]['subType']
        if type == "anatomy" :
             data[item]['caries'] = 0
             data[item]['d50'] = 0
        if type == "disease" :
                    if subType == "85" :
                        for i in range(len(data)):
                            if data[i]['type'] == "d85" :
                                d85 = int(data[i]['subType'])
                                data[i]['subType'] = str(1 + d85)
                    if subType == "10" :
                        tooth = disease_intersection_tooth(data, item)

                        for Tooth in range(len(data)):
                            if data[Tooth]['type'] == "anatomy"  and data[Tooth]['subType'] == tooth :
                                data[Tooth]['caries'] += 1
                       

                    if subType == "50" :
                        tooth = disease_intersection_tooth(data, item)

                        for Tooth in range(len(data)):
                            if data[Tooth]['type'] == "anatomy"  and data[Tooth]['subType'] == tooth :
                                data[Tooth]['d50'] += 1
                    
        if type != "anatomy" :
                    del data[item]
                    item -= 1
                    lenght -= 1
                    

        item += 1
                       
   print(data)


modif_json(data)


