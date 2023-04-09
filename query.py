import csv
import os
from bs4 import BeautifulSoup
Tag=[]
def query(str,qid):
    with open("/home/subinay/Documents/data/Tag_prediction_model/clean_random_200_doc/"+str,"r") as f1:
         content = f1.read();
    result = " ".join(line.strip() for line in content.splitlines())
    line=line.replace(";","")
    with open("/home/subinay/Documents/data/sentence_tag/Annotated_Anjana_200/"+str,"r") as f2:
        content = f2.read();
    result = " ".join(line.strip() for line in content.splitlines())
    soup = BeautifulSoup(result,'html.parser')
    tags = [tag.name for tag in soup.find_all()]
    tags1=set(tags)
    with open("/home/subinay/Documents/data/sentence_tag/Annotated_Bipasha_200/"+str,"r") as f2:
        content = f2.read();
    result = " ".join(line.strip() for line in content.splitlines())
    soup = BeautifulSoup(result,'html.parser')
    tags = [tag.name for tag in soup.find_all()]
    tags2=set(tags)
    myset = tags1 | tags2
    k=[qid,str,line[0:500],myset]
    Tag.append(k)
    qid=qid+1
dir="/home/subinay/Documents/data/Tag_prediction_model/clean_random_200_doc/"
files=os.listdir(dir)
file1=[]
qid=0
for f in files:
    qid=qid+1
    query(f,qid)
with open('/home/subinay/Documents/data/prior_case_retrieval/query_short.csv', 'w', newline='') as file:
    fieldnames = ['qid','docid','text','tag']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,delimiter=';')
    writer.writerows(Tag)
                      
