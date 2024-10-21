# with open("ttxt.txt","w") as ff:
#     ff.write("Hello We are here")
# with open("ttxt.txt","r") as ttt:
#     tttt=ttt.read()
#     print(tttt)
# with open("ttxt.txt","a") as new:
#     new.write("Hello Again")
# with open("hhh.txt","r") as kk:
#     print(kk.read())
#     print(kk.read())

list=["helloedddededdedede\n","eeweewewewewewew\n","ewwewewewewewwe\n","ewewewewewewewewwewe\n"]
with open("hhh",'w') as ll:
    ll.writelines(list)
with open("hhh","r") as ee:
      dd=ee.readlines()
      print(dd)
