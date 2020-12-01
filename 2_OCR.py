import os, re
import pdf2image, pytesseract
import PyPDF2, json, yaml
import functions

#Variables

settingsFile = "./settings.yml"
settings = yaml.load(open(settingsFile))
memexPath = settings["path_to_memex"]

#Clean the PDF

def removeCommentsFromPDF(pathToPdf):
    with open(pathToPdf, 'rb') as pdf_obj:
        pdf = PyPDF2.PdfFileReader(pdf_obj)
        out = PyPDF2.PdfFileWriter()
        for page in pdf.pages:
            out.addPage(page)
            out.removeLinks()
        tempPDF = pathToPdf.replace(".pdf", "_TEMP.pdf")
        with open(tempPDF, 'wb') as f: 
            out.write(f)
    return(tempPDF)

#Finding the right language

def langfinder(file):
    langs = ["en", "eng", "english", "de", "deu", "deutsch", "gernman", "pol", "polish", "polski", "uk", "ukr", "ukrainian", "ru", "rus", "russian"]
    lang = "eng"
    for i in range(len(langs)):
        if re.search(langs[i], file) == True:
            if langs[i] == "eng" or "en" or "english":
                lang = "eng"
            elif langs[i] == "de" or "deu" or "deutsch" or "german":
                lang = "deu"
            elif langs[i] == "pol" or "polish" or "polski":
                lang = "pol"
            elif langs[i] == "ukr" or "uk" or "ukrainian":
                lang = "ukr"
            elif langs[i] == "ru" or "rus" or "russian":
                lang = "rus"
        return lang

#OCR-ing the PDF

def ocrPublication(pathToMemex, citationKey, language):
    publPath = functions.generatePublPath(pathToMemex, citationKey)
    pdfFile  = os.path.join(publPath, citationKey + ".pdf")
    jsonFile = os.path.join(publPath, citationKey + ".json")
    saveToPath = os.path.join(publPath, "pages")

    pdfFileTemp = removeCommentsFromPDF(pdfFile)

    if not os.path.isfile(jsonFile):
        if not os.path.exists(saveToPath):
            os.makedirs(saveToPath)
        
        print("\t>>> OCR-ing: %s" % citationKey)

        textResults = {}
        images = pdf2image.convert_from_path(pdfFileTemp)
        pageTotal = len(images)
        pageCount = 1
        for image in images:
            image = image.convert('1')
            finalPath = os.path.join(saveToPath, "%04d.png" % pageCount)
            image.save(finalPath, optimize=True, quality=10)

            text = pytesseract.image_to_string(image, lang=language)
            textResults["%04d" % pageCount] = text

            print("\t\t%04d/%04d pages" % (pageCount, pageTotal))
            pageCount += 1

        with open(jsonFile, 'w', encoding='utf8') as f9:
            json.dump(textResults, f9, sort_keys=True, indent=4, ensure_ascii=False)
    
    else:
        print("\t>>> %s has already been OCR-ed..." % citationKey)

    os.remove(pdfFileTemp)

#Processing the PDF

def Processing():
    publPath = functions.generatePublPath(pathToMemex, citationKey)
    cleanpdf = removeCommentsFromPDF(publPath)
    lang = langfinder(publPath)
    ocr = ocrPublication(publPath, citationKey, lang)
    shutil.copyfile(ocr, publPath)

bibData = functions.loadBib(settings["bib_all"])

def main(bibData):  
    for k, v in bibData.items():
        processBibRecord(memexPath, v)

main()