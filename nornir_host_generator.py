import csv
from ruamel.yaml import YAML

yaml = YAML()

#yaml formatting
yaml.indent(mapping=4,sequence=6,offset=4)
yaml.explicit_start = True

#csv row to dictionary to yaml file
with open("/Users/mike/Desktop/nornir/hosts.csv","r",\
    encoding="utf-8-sig") as csv_file:
    with open("/Users/mike/Desktop/nornir/hosts.yaml", "a+") as file:
        dict_reader = csv.DictReader(csv_file)
        for row in enumerate(dict_reader):   
            new_row = {}
            headers = list(row[1].keys())
            new_row[row[1][headers[0]]] = {
                headers[1]:row[1][headers[1]],
                headers[2]:[row[1][headers[2]]]
            }
            if row[0] == 0:
                yaml.dump(new_row,file)
            else:
                yaml.explicit_start = False
                file.write("\n")
                yaml.dump(new_row,file)


        


        


    
