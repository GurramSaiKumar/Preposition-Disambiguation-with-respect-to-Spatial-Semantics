years_dict = dict()
with open("tr_data.txt","r") as op1:
  for l in op1:
    tok=l.split()
    if tok[0] in years_dict:
        # append the new number to the existing array at this slot
        years_dict[tok[0]].append(tok[1])
    else:
        # create a new array in this slot
        years_dict[tok[0]] = [tok[1]]


temp=dict()
with open("tr_temp_cl.txt","r") as op2:
	for t in op2:
		toke=t.split()
		if int(toke[1])+1 in temp:
			temp[int(toke[1])+1].append(toke[0])
		else:
			temp[int(toke[1])+1] = [toke[0]]

l=len(years_dict)

df=open("tr_values_attr.txt","w")
count=1
while l:
	if str(count) in years_dict:
		for i in years_dict[str(count)]:
			if count in temp:
				list=[]
				list=temp[count]
				if i in list:
					print("1", file=df)
				else:
					print("0", file=df)
			else:
				print("0", file=df)
		count=count+1
		l=l-1
	else:
		count=count+1





	
# while l:
# 	if count in years_dict:
# 		for i in years_dict[str(count)]:
# 		    if count in temp:
# 			    list=[]
# 			    list=temp[count]
# 			    if i in list:
# 				    print("1", file=df)
# 			    else:
# 					print("0", file=df)
# 			else:
# 				print("0", file=df)
# 		count=count+1
# 		l=l-1
# 	else:
# 		print("0", file=df)
# 		count=count+1
# 		# l=l-1

	

	# 	list=[]
	# 	list=temp[count]
	# 	if i in list:
	# 		print("1", file = df)
	# 	else:
	# 		print("0", file=df)
	# count=count+1
	# l=l-1



	
	
	
		
	
		
    
    