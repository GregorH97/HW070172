import re
import yaml

"""
1. load bibtex file
    - bibliography should be curated in Zotero (one can program cleaning procedures into the script, but this is not as reliable);
    - loading bibtex data, keep only those records that have PDFs;
    - some processing might be necessary (like picking one file out of two and more)
2. convert into other formats
    - csv
    - json
    - yml
"""

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml" 
settings = yaml.load(open(settingsFile))
bibKeys = yaml.load(open("zotero_biblatex_keys.yml"))

###########################################################
# FUNCTIONS ###############################################
###########################################################

# load bibTex Data into a dictionary
def bibLoad(bibTexFile):#we define a new funtion

    bibDic = {}#we create a new list

    with open(bibTexFile, "r", encoding="utf8") as f1:#we open the new file with utf8 to make it possible to open on windows
        records = f1.read().split("\n@")#we are again seperating our records record by record, thereby creating a list

        for record in records[1:]:#we are looping record through the list we just created, starting with the second entry in the list
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():#open just the records with pdf in them

                record = record.strip().split("\n")[:-1]#remove all spaces at the beginning and end and again seperate the records by lines, the \n stands on the end of the string

                rType = record[0].split("{")[0].strip() #again remove all the spaces and split them by bracets, to seperate the Type of the record
                rCite = record[0].split("{")[1].strip().replace(",", "")#remove all spaces and commas, and again seperate the records by brackets, to find out the Citeation

                bibDic[rCite] = {}#we create a new list
                bibDic[rCite]["rCite"] = rCite#we add our citations to the list
                bibDic[rCite]["rType"] = rType#we add the types to the list to, in a way to make tuples out of both of them

                for r in record[1:]:#we are now further disecting our record, starting at the second value in the string
                    key = r.split("=")[0].strip()#we are splitting by = and define the key to be the string in front of the =
                    val = r.split("=")[1].strip()#we are doing the same, just defining the value to be the thing behind the =
                    val = re.sub("^\{|\},?", "", val)#we use regular expressions to replace all the not needed letters with nothing (deleting them)

                    fixedKey = bibKeys[key]#out of the opened file we now are looking for the placement of key, to assign this value to fixedKey

                    bibDic[rCite][fixedKey] = val#The touple of rCite and fixedKey within the library of BibDic is now assigned the value val


    print("="*80)#the following lines are there to give a graphic output and show the number of records
    print("NUMBER OF RECORDS IN BIBLIGORAPHY: %d" % len(bibDic))
    print("="*80)
    return(bibDic)

###########################################################
# CONVERSION FUNCTIONS ####################################
###########################################################

import json
def convertToJSON(bibTexFile):#we start a new function
    data = bibLoad(bibTexFile)#import the data
    with open(bibTexFile.replace(".bib", ".json"), 'w', encoding='utf8') as f9:#we are replacing the bib marker with a json marker and open the file
        json.dump(data, f9, sort_keys=True, indent=4, ensure_ascii=False)#the file is converted into json


import yaml
def convertToYAML(bibTexFile):
    data = bibLoad(bibTexFile)#a new function is defined and the data is loaded
    with open(bibTexFile.replace(".bib", ".yaml"), 'w', encoding='utf8') as f9:#again the same steps are undertaken as whith the json files
        yaml.dump(data, f9)

# CSV is the trickest because bibTeX is not symmetrical
def convertToCSV(bibTexFile):
    data = bibLoad(bibTexFile)#a new function is defined and the data is loaded
    # let's handpick fields that we want to save: citeKey, type, author, title, date
    headerList = ['citeKey', 'type', 'author', 'title', 'date'] #a list is created to seperate the lines
    header = "\t".join(headerList)#we are now joining the items of headerlist into a new string, seperated by tabulators

    dataNew = [header]#a new variable is defined to make a list out of our previous item

    for k,v in data.items():#we are again creating a loop with two values, to create tuples
        citeKey = k#citekey is given an ascending value in each loop

        if 'rType' in v:#in the following if-else-cycles we are checking wether the data is complete and wether all the data that we need is given, if there is not the sufficient
            rType = v['rType']#data that we need we let the program replace the value with an NA, this is because in CSV data type all the info has to be given.
        else:
            rType = "NA"

        if 'author' in v:
            author = v['author']
        else:
            author = "NA"

        if 'title' in v:
            title = v['title']
        else:
            title = "NA"

        if 'date' in v:
            date = v['date']
        else:
            date = "NA"

        tempVal = "\t".join([citeKey, rType, author, title, date])#we ceate a new value, where we join all the values we created into a new string, seperated by tabs
        dataNew.append(tempVal)#in the end we add those strings into the list which we have defined at the beginning, where also the header is

    finalData = "\n".join(dataNew)#we are now creating a new string where we store all the data from DataNew and seperate the by tabs
    with open(bibTexFile.replace(".bib", ".csv"), 'w', encoding='utf8') as f9:#we are again perparing the final steps of conversion, just as we did in the previous functions
        f9.write(finalData)#we write the final data into our file


###########################################################
# RUN EVERYTHING ##########################################
###########################################################

print(settings["bib_all"])

#convertToJSON(settings["bib_all"])
#convertToYAML(settings["bib_all"])
#convertToCSV(settings["bib_all"])


print("Done!")