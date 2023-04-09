with open("/home/subinay/Documents/data/sequence_labeling/tag_sequence_prf.csv","w") as f1:
	with open("/home/subinay/Documents/data/sequence_labeling/tag_sequence.txt","r") as f:
		for line in f:
			line = line.strip()
			line = line.replace('"',"")
			line = line.replace("'","")
			line=line.replace(",","")
			line=line.replace(".","")
			line=line.replace("(","")
			line=line.replace(")","")
			line=line.replace("[","")
			line=line.replace("]","")
			line=line.replace("@","")
			if len(line.split(";")[0]) <= 5:
				continue
			f1.write(line)
			f1.write("\n")
f1.close()
		
