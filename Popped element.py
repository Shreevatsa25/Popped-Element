num=[]
"""user input"""

numcount=int(input("how many numbers do you want to input?"))

for i in range(numcount):
    element= int(input("enter number:"))
    num.append(element)
    
userNum=[]

for i in num:
    if i not in userNum:
        userNum.append(i)
        
print(num)
print(userNum)

poppedElement=userNum.pop()
print("popped elment is :",poppedElement)
print(userNum)