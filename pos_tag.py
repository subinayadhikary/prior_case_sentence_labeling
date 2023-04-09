import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#stop_words = set(stopwords.words('english'))
import csv
def tag(list1,list2):
    if(len(list1)==len(list2)):
        for i in range(len(list1)):
            if(list2[i]=='O'):
                list2[i]='Otag'
            print(list1[i][0],list1[i][1],list2[i])
        print(" ")

# Open file 
with open('tag_sequence_prf.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        for i in row:
            sent=i.split(';')[0]
            label=i.split(';')[1]
            k=label.split()
            wordsList=sent.split()
            #wordsList = nltk.word_tokenize(sent)
            tagged = nltk.pos_tag(wordsList)
            tag(tagged,k)
            #print(tagged)
       