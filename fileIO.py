import pickle
#impoort pickle madule
#create one object it could be ant thing
# data={1,2,3,4,5,6,7,
#       "Hello","well Come",
#       "Bye",
#       8,9,10}
data2=["Vinayak","MCA",27,"Hyderabad"]
# #Use With clause
# with open("Normal2.pickle","wb") as file_obj:
#     pickle.dump(data,file_obj)
#
# #I order to read again u need to open file in rb mode
with open("Normal2.pickle","rb") as file_obj:
#     fil2 = pickle.load(file_obj)
#     print(fil2)

#############LOADS AND DUMPS
# with open("Normal3.pickle","wb") as file2_obj:
    ob2=pickle.dumps(data2)
    print(ob2)
    hh=pickle.loads(ob2)
print(hh)



