#-----------------INPUT-------------------
a=list(input(""))
oper=["+","-","x","X","*","/"]
num=["1","2","3","4","5","6","7","8","9","0"]
n1=""
n2=""
op=""
for i in a:
    if i in oper:
        op=i
    if i in num:
        if op == "":
            n1=n1+i
        else:
            n2=n2+i
n1,n2=int(n1),int(n2)
#-----------------PROCESSING-------------------
if op=="+":
    ans=n1+n2
elif op=="-":
    ans =n1-n2
elif op=="/":
    ans =n1/n2
else:
    ans=n1*n2
#-----------------OUTPUT-------------------
print(n1,op,n2,"=",ans)
