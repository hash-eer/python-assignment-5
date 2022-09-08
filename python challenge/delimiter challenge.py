# A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

# Examples
# The following are examples of balanced delimiter strings:

# ()[]{}
# ([{}])
# ([]{})
# The following are examples of invalid strings:
# ([)]
# ([]
# [])
# ([})
# Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:

# Input:
# ([{}])
# Output:
# True

class Answer:
    
    def checkparam(self,str):
        check={')':'(','}':'{',"]":"["}
        list=[]
        
        for i in str:
            if i in check.values():
                list.append(i)
            elif list and check[i]==list[-1]:
                list.pop()
            else:
                return False
        return list==[]
    

            
str=input("enter the brackets:")
result=Answer().checkparam(str)
print(result)
