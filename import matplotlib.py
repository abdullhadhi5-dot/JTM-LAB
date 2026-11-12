import matplotlib.pyplot as plt
n=int(input("how many students ?"))
students=[]
marks=[]
for i in range(n):
    name=input("enter a name :")
    mark=int(input("enter student mark :"))
    students.append(name)
    marks.append(mark)
plt.bar(students,marks)
plt.title("student marks")
plt.xlabel("student names")
plt.ylabel("mark")
plt.show()