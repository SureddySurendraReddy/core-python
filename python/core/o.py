from functools import reduce
#l=[[1,2],[3,4],[5,6]]
#r=list(map(lambda x:x+5,l))
#print(r)



#6th q
# v="AEIOUaeiou"
# st=list(filter(lambda x:x not in v, input()))
# print(st)

# 7 th question
# l=['x','y','z','a','b','c']
# st=reduce(lambda x,y: x+y,l)
# print(st)

# # 8 th question
# l=[10,250,30,40,510]
# k=list(map(lambda x:id(x),l))
# print(k)

# #2nd question
# a=[1,2,3,4]
# b=[10,20,30,40]
# k=list(map(lambda x,y:x+y,a,b))
# print(k)

# 3rd q
# nums=[12,15,7,18,20,25,21]
# l=list(filter(lambda x:(x%3==0)^(x%5==0),nums))
# print(l)

# 4th q
# l=[[1,2],[3,4],[5,6]]
# result=list(map(lambda x:x.append(10),l))
# print(result,l,sep='\n')

#pdf2 q2 sum of corresponding elements

#a=[1,2,3,4]
#b=[10,20,30,40]
#s=list(map(lambda x,y:a+b,a,b))
#print(s)

#q3 divisible 3 or 5

#n=[12,15,7,18,20,21,25]
#r=list(filter(lambda x:x%3==0 or x%5==0,n))
#print(r)

#q4 compute the um and initial value st with 10

#n=[1,2,3,4]
#d=reduce(lambda x,y:x+y,n,10)
#print(d)

#q5

#n=[[1,2],[3,4],[5,6]]
#r=list(map(lambda x:x.append(10),n))
#print("r",r)
#print("n",n)

#methods
class profile:
    def __init__(self,username):
        self.followers=0
        self.username=username
    def follow(self):
        print("someone followed you")
        self.followers+=1
    def update_username(self,new):
        self.username=new
p1=profile("s.surendra_07")
p1.follow()
print(p1.followers)
p1.update_username("vijaya")
print(p1.username)