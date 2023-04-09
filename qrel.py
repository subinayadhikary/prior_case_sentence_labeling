from bs4 import BeautifulSoup
from collections import defaultdict
import os
import json
dict={}
def search(str):
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
    dict[str]=myset
    # tag_text = {}
    # tag_text =defaultdict(list)
    # for tag in tags:
    #     for a in soup.find_all(tag):
    #         tag_text[a.text].append(tag)
    #         #tag_text[a.text]=tag
    # dict[str]=tag_text
dir="/home/subinay/Documents/data/sentence_tag/Annotated_Bipasha_200/"
files=os.listdir(dir)
file1=[]
for f in files:
    #print(f)
    search(f)
qid=0
for k,v in dict.items():
    qid=qid+1
    for k1,v1 in dict.items():
        if set(v) & set(v1):
            print(qid," ",0," ",k1," ",1)
        else:
            print(qid," ",0," ",k1," ",0)

