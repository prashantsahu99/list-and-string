x=input("enter elements")
x = x.split()
t=""
for i in x:
	if i not in t:
		t=t+i+"*"
print(t[0:len(t)-1])		
