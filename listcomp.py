l1=[1,3,4,2]
l2=[1,4,9,5]
l3=[x for x in l1 if x in l2]
l4=[i for i in l1 if i not in l2]
l5=[j for j in l2 if j not in l1]
l3.extend(l4)
l3.extend(l5) 
print(l3)

