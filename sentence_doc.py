import os
import json
import re
path1="/home/subinay/Documents/data/Tag_prediction_model/clean_random_200_doc/"
file_path="/home/subinay/Documents/data/sentence_tag/Annotated_Anjana_200/"
file_path1="/home/subinay/Documents/data/sentence_tag/Annotated_Bipasha_200/"
json_data=open("/home/subinay/Documents/data/sentence_tag/annotated_anjana_200.json")
json_data1=open("/home/subinay/Documents/data/sentence_tag/annotated_bipasha_200.json")
jdata = json.load(json_data)     
jdata1=json.load(json_data1)
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr|P.Ws|etc|viz|No|Pt|ss|Cr|P|C|W|no|Ss|Nos|nos|Rs)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|P.Ws.)"
digits = "([0-9])"
def split_into_sentences(text):  
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    #sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

def find_index(str):  # to split the document in to sentenecs
    with open("/home/subinay/Documents/data/Tag_prediction_model/clean_random_200_doc/"+str,"r")as f1:
        content = f1.read();
    result = " ".join(line.strip() for line in content.splitlines())
    sentence=split_into_sentences(result)
    with open("/home/subinay/Documents/data/sequence_labeling/sentence_doc/"+str,"w")as f2:
        for i in range(len(sentence)):
            line=sentence[i].replace("\\","")
            line=line.replace(" ,","")
            line=line.replace(".","")
            if(len(line)>5):
                f2.write(line)
                f2.write("\n")
    f2.close()

    
dir="/home/subinay/Documents/data/sentence_tag/Annotated_Bipasha_200/"
files=os.listdir(dir)
for f in files:
    find_index(f)
