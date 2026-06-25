#students marks manager
student=int(input("no of students:"))
marks=list(map(int,input("Enter all marks: ").split()))
print(marks)
largest=marks[0]
for i in marks:
    if i>largest:
        largest=i
print("maximum marks=",largest) 
smallest=marks[0]
for i in marks:
    if i<smallest:
        samllest=1
print("minimum marks=",smallest)
total=0
for i in marks:
    total=total+i
average=total/len(marks)
print("average marks=",average)  