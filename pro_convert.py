import csv
import json
import yaml
import xmltodict
import pprint
import dicttoxml
import io
import xml
from xml.etree import ElementTree, ElementInclude
##verifier si fichier pris en compte
#
def verification_file(chem):
    file=chem
    chem=chem.split(".")
    ext=chem[-1]
    all_exten=["csv","yml","yaml","json","xml"]
    my_dict=[]
    if ext in all_exten:
        #convertion dub fichier csv en un dictionnaire
            if ext == "csv":
                with open(file, "r") as data:
                    my_file = csv.DictReader(data)
                    for row in my_file:
                        my_dict.append(row)
                return (my_dict)
            # convertion dub fichier json en un dictionnaire
            elif ext=="json":
                with open(file, "r") as data:
                    my_dict = json.load(data)
                return (my_dict)
            # convertion dub fichier yaml en un dictionnaire
            elif ext == "yaml" or ext == "yml":
                with open(file) as data:
                    my_dict = yaml.load(data,Loader=yaml.FullLoader)
                return (my_dict)
            # convertion dub fichier xml en un dictionnaire
            elif ext == "xml":
                with open(file, "r") as xml_obj:
                    # coverting the xml data to Python dictionary
                    my_dict = xmltodict.parse(xml_obj.read())
                    # closing the file
                    #xml_obj.close()
                    my_dict = pprint.pprint(my_dict, indent=2)

                return my_dict

#print (verification_file(chem))
#convertion dun  dinction en csv
#a=verification_file(chem)
#print(a)
def conv_dic_to_json(chem):
    #a=verification_file(chem)
    json_object = json.dumps(chem, indent=4)
    print(json_object)
#print(conv_dic_to_json( chem))
def conv_dic_to_yaml(chem):
    #a=verification_file(chem)
    yam_file=yaml.dump(chem)
    return (yam_file)

#print(conv_dic_to_xml(chem))
def conv_dic_to_xml(chem):
    #a=verification_file()
    xml = dicttoxml.dicttoxml(chem)

    return (xml)

#print(conv_dic_to_csv(chem))
def conv_dic_to_csv(my_dic):
    #a=verification_file(chem)
    for i in range(len(my_dic)) :
        elm=my_dic[i]
        keys=list(elm.keys())
    with open('names.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for data in my_dic:
            writer.writerow(data)
        print(writer)
