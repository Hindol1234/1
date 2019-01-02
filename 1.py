
marks=int(input("Enter the marks:"))
grade=''
if marks>75:
   grade='o'
elif marks>60 and marks<=75:
   grade='A'       
elif marks>50 and marks<=60:
   grade='B'
elif marks>40 and marks<=50:
   grade='C'
else:
   grade='D'
print("GRADE=",grade)
input("Please input for exit:")
    
    
