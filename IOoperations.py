import pickle
# f=open("Normal.text","w")
# # g=f.read()
#
# g=f.write("Hello Well Come back")
#
#
# f.close()
# m=open("Normal.text","r")
# n=m.read()
# print(n)
# with open("N2.py","a") as y:
#     y.write("This is new line\n")
#pickle  Module

# li=["One","Two","Three",4,5,6]
# f_obj=pickle.dumps(li)
# print("File Objets=>", f_obj)
# unpic=pickle.loads(f_obj)
# print("unpickling+>",unpic)
# hh="first.pickle"
# obj=[1,2,3,4,5,6,7]
# pickle.dump(obj,open("first.pickle","wb"))
# jj=open(hh,"rb")
# ss=pickle.load(jj)
# print(ss)
#randam access using Tell() AND Seek() Method
# with open("Normal.text","r") as obj:
    # print("current position is :",obj.tell())
    # content=obj.read(5)
    # print("current position is :", obj.tell())
    # content = obj.read(10)
    # print("current position is :", obj.tell())
    #Seek() Method We can move the pointer in a file
    # ob1=obj.seek(6)
    # print(ob1)
    # ob2=obj.read()
    # print(ob2)
    # ob3=obj.tell()
    # print(ob3)
    # obj4=obj.seek(1)
    # print(obj4)






