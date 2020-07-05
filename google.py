
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")
query = "uçak bileti"
list1=[]
list2=[]
number=-3
for j in search(query, num=15, stop=80, pause=2):
	a=str(number)+"."+j
	number+=1
	list1.append(a)
for i in list(filter(lambda k: ("ucuzauc") in k,list1)):
	list2.append(i)
print(*list2,sep="\n")
# print(list(filter(lambda k: ("keyword") in k,list1)))
# print(*list1,sep="\n")

