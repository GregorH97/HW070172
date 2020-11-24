import os, yaml #importing libraries

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml"   #assuginig the file to a variable
vars = yaml.load(open(settingsFile))    #opening the file

###########################################################
# FUNCTIONS ###############################################
###########################################################

# analyze bibTeX data; identify what needs to be fixed

def bibAnalyze(bibTexFile): #starting a new function

    tempDic = {}    #creating a list

    with open(bibTexFile, "r", encoding="utf8") as f1:  #opening the file that has been defined in the function, with an encoding to be able to operate it on windows
        records = f1.read() #assigning the file to a variable
        records = records.split("\n@")  #splitting the variable into different sections, thereby creating a list

        for record in records[1:]: #a loop that processes all values in the list "records"
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():    #check wether the record has a PDF
                record = record.strip() #if so, then remove all spaces at the beginning and end
                record = record.split("\n")[:-1] #in the following, seperate the by line

                for r in record[1:]:    #again, loop through the newly split record
                    r = r.split("=")[0].strip() #and get those records again seperated at the = and take away the first symbol of the line

                    if r in tempDic: #we are checking wether our value is already in our temporary Dictionary
                        tempDic[r] += 1 #if not then we add it
                    else:
                        tempDic[r] = 1 #otherwise we leave it be

    results = [] #we create a new dictionary to return our results
    for k,v in tempDic.items(): #we are running a new loop with our list
        result = "%010d\t%s" % (v, k) #k and v will be displayed with 10 integers, seperated by a tab and converted into a string
        results.append(result)#the tuple we just created becomes part of the list

    results = sorted(results, reverse=True) #we reverse the order of the list
    results = "\n".join(results) #we join the seperate parts of the list together, but seperate them by a new line

    with open("bibtex_analysis.txt", "w", encoding="utf8") as f9: #we are now preparing to write our results into a new file
        f9.write(results)#we write iur results into a new file

bibAnalyze(vars['bib_all'])#we now run the program on the selected file