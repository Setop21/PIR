test1filehandle = open("results10_06.txt", "r") 
test2filehandle=open("result2.txt","r") 
test3filehandle=open("test3.txt","w") 
test1list= test1filehandle.readlines() 
test2list=test2filehandle.readlines()
k=1
for i,j in zip(test1list,test2list): 
 if i !=j:
    test3filehandle.write("Line Number:" +str(k)+" ")
    test3filehandle.write(i.rstrip("n") + " "+ j)
    k=int(k)
    k=k+1;