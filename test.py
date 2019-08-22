# v = """
# 1
# 333
# 2
# 14
# 3
# 45
# 4
# 78
# 5
# 71
# 6
# 7"""
# # print(v)
# # print(type(v))
# v_list = []
# new_line_count = 0
# for i in v:
# 	#print i
	
# 	if i=="\n":
# 		new_line_count+=1
# 		pass
# 	else:
# 		print (i)
# 	if (new_line_count%2 !=0):
#  		v_list.append(i)
#  		#pass
# 	#else:
# 	# new_line_count%2==0:
# 	#v_list.append(i)
# newl=[x for x in v_list if x!="\n"]


# print("new lines -------",new_line_count)
# print(v_list,"::::::")
# print (newl)


n1="""147122143454756787219324104311"""
l=[]
c=1
for i in n1:
	if c==int(i):
		print i,"000"
		c+=1
		l.append(i)
#print l,"{{{{{{{{{"

