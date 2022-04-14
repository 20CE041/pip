n = int(input()) 
mylist = [] 
cnt = 0 

for i in range(n):
    str1 = input() 
    mylist.append(str1) 

myset = list(set(mylist)) 
print(myset)
print(len(myset)) 

for j in range(len(myset)):
    cnt = mylist.count(myset[j])
    print(cnt, end = " ") 