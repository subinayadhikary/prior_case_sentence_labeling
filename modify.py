with open("/home/subinay/Documents/data/prior_case_retrieval/query_short_new.csv","w") as f1:
	with open("/home/subinay/Documents/data/prior_case_retrieval/query_short.csv","r") as f:
		for line in f:
			line = line.strip()
			line = line.replace('"',"")
			line = line.replace("'","")
			line=line.replace(",","")
			line=line.replace("(","")
			line=line.replace(")","")
			line=line.replace("[","")
			line=line.replace("]","")
			line=line.replace("@","")
			f1.write(line)
			f1.write("\n")
f1.close()
		
