# This is problem to convert all the negative coordinates to a positive coordinates;
# The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
# We can add or delete any number from the coordinates ; however graph should not be changed;

# Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
# Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]
import random

u=[1,2,3,4,5,6,7,8,9]
list = [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
list1=[]
n=len(list)
#print(n)
count=0
#print(list[3][0])
for i in range (6):
    if list[i][0]<0 or list[i][1]<0:
        n1=random.randint(0,10)
        temp=list[i][0]-list[i][1]
        target=abs(temp)
        list1.insert(i,(n1,n1+target))
    
    else:
        list1.insert(i,(list[i][0],list[i][1]))
        
print("original list",list)      
print("changed list",list1)

        
# for x in list:
#     count+=1
#     if x[0]<0 or x[1]<0:
        
        
#         temp=x[0]-x[1]
#         target=abs(temp)
        
#         n1=random.randint(0,10)
        #list.insert(count-1,(n1,n1+target))
        
        

        
        
        # while (n1-n2) != target:
        #     for i in range(9):
        #         for j in range(9):
        #             n1=u[i]
        #             n2=u[j]
        #             if n2-n1==target:
        #                 break
                    
                
        # list.insert(0,(n1,n2))
        

    
            
        
        
        
        
    
        
        

# list1=[-1,3]
# print(math.dist([list[0],list[1]]))