import pandas as pd

# groups = ['HIGHPI', 'CNFD','CNFDPI', 'INTL']
groups = {'HIGHPI':1, 'CNFD':2,'CNFDPI':3, 'INTL':4}
classwords_dict1 = {'Rate':{ 
                            'HIGHPI':['Credit Bureau'],
                            'CNFD':['Basel','Federal','Credit']
                        }
                  }
classwords_dict = {'Rate':['Credit Bureau','Basel','Federal','Credit']}
classwords_DF = pd.read_excel(r'/home/swamy/Desktop/DataOops.xls', sheet_name='Sheet1')
# print classwords_DF.head(3)

# colnames = ['Table Name','Column Name','Logical_Name','Data Type','Definition']

df2 = classwords_DF['Logical_name']


# df3 = classwords_DF[classwords_DF.Logical_Name.isin(classwords_list)]


matched_list = []
for i in df2:
    for j in classwords_dict.keys():
        if str(i).__contains__(j):
            matched_list.append(i)        


# print matched_list, len(matched_list)

# result = classwords_DF[classwords_DF.Logical_Name.isin(matched_list)]

# HIGHPI_Df = pd.DataFrame()
highpi_list = []
cnfd_list = []
intl_list = []

for i in groups:
    for key, value in classwords_dict1.items():
        if key == 'Rate':            
            if i == 'HIGHPI':                
                for jk in value[i]:                   
                    for kkk in matched_list:
                        if kkk.__contains__(jk):                            
                            highpi_list.append(kkk)
            elif i == 'CNFD':
                for jk in value[i]:                   
                    for kkk in matched_list:
                        if kkk.__contains__(jk):                            
                            cnfd_list.append(kkk)
            # elif i == 'CNFD':
            #     intl_list.append(kkk)



print "=========" *20
common_elements1 = list(set(cnfd_list) & set(highpi_list))
common_elements2 = list(set(cnfd_list).intersection(highpi_list))



# print common_elements2, common_elements1, "^^^^"

if groups['CNFD'] >  groups['HIGHPI'] :
    # print ("True")
    for i in common_elements1:
        if i in highpi_list:
            cnfd_list.remove(i)

else:
    print groups['CNFD'], "%^%^%"
    


highpi_result = classwords_DF[classwords_DF.Logical_name.isin(highpi_list)]


cnfd_result = classwords_DF[classwords_DF.Logical_name.isin(cnfd_list)]

pg_data_list = ["cnfd" for i in range(len(cnfd_list))]
print pg_data_list, "####"
cnfd_result['pg_group'] = pg_data_list

cnfd_excel = cnfd_result.to_excel('/home/swamy/Desktop/cnfd.xls', sheet_name="Sheet1")


highpi_excel = highpi_result.to_excel('/home/swamy/Desktop/highpi.xls', sheet_name="Sheet1")


print (cnfd_result)

print type(cnfd_result)

# print "*****"*30
# print (highpi_result)
# print "After result"
# print intl_list, "((((((((((("


# list1 = [11, 5, 17, 18, 23, 50]  
# list1 = [ elem for elem in list1 if elem % 2 != 0]
# print list1
