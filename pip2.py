#  Himani kapadia
#  20CE041

# dictionary practica

#a
T={1:'HI',2:'HIMANI',3:'HOW',4:'ARE',5:'YOU'}
a=7
if a in T:
    print('KEY IS PRESENT')
else:
    print('KEY IS NOT PEWSENT')

#B
T1={1:'HI',2:'HIMANI'}
T2={3:'HOW',4:'ARE',5:'YOU'}
T3=T1.copy()    #copy() for copying t1's element in t3
T3.update(T2)   #update() for updateing t3 by adding t2's element
print(T3)

#C
A={1:500,2:800,3:600,4:400}
print(sum(A.values())) # sum for sumantion of given number

#D
T={1:'HII',2:'HIMANI',3:'HOW',4:'ARE'}
T.update({4:'YOU'})
print(T)

#E
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)

#TUPLE practical

#A
T1=(1,2,3)
T2=('A','B','C')
T3=('HIMANI','JIYA','JAY')
print(T1)
print(T2)
print(T3)

#B
T=[100,200,300,400,500]
print(T[2])

#C
T=(1,2,3,4)
T=T+(5,)
print(T)

#D
T =('H','I','M','A','N','I')
T=''.join(T) #join() for combain all charactar and make it string 
print(T)

#E
T =('H','I','M','A','N','I')
print(len(T)) #len() use to find how many number of element in the array

#SET practical

#A
T:set[str]=(['A','B','C','E'])
print('SET: ',T)
T.clear()     #clear() for deleting all element from set
print('clear: ',T)

#B
T={'HIMANI','JIYA','JAY','PRANAY','SAMARTH'}
T.remove('SAMARTH')  #remove() use to remove particular element
print(T)

#C
T1={1,2,3,4,5}
T2={3,4,6,7}
print('INTERSECTION',str(T1 & T2))
print('UNION: ',str(T1 | T2))
print('DIFFERANCE OF SET',str(T1-T2))
print('DIFFERANCE OF SET',str(T2-T1))

#D
T={1,2,3,4,5}
print(T)
print(max(T))   # max() to find maximam value element 
print(min(T))   #min() to find minimam value element

#E
list1=[1,2,'ABC','XYZ']
Tuple1=(3,4,'ABC','XYZ')
Dictionary1={1:5,2:6,3:'ABC',4:'XYZ'}
arr1=set(list1)
arr2=set(Tuple1)
arr3=set(Dictionary1.values())
arr=arr1.intersection(arr2)    #intersection() use to find commant elemnt in set 
result=arr3.intersection(arr)
counts=len(result)
print(result)
print('count of most commant element is: ',str(counts))