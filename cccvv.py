import csv
# data=[['name','age','occupation'],['rana',35,'doctor'],['rama',45,'Teacher']]
# with open('new.csv','w') as file:
#     write=csv.writer(file)
data=[{'Name':'Rana','Age':35,'occupation':'Doctor'},
      {'Name':'Rashni','Age':20,'occupation':'Teacher'},
      {'Name':'Sita','Age':28,'occupation':'Lawyer'},]
fieldname=['Name','Age','Occupation']
with open('new.csv','w') as file:
    w=csv.DictWriter(file,fieldnames=fieldname)
    w.writeheader()
    for i in data:
        w.writerow(i)

