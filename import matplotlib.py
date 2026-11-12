import matplotlib.pyplot as plt
students = ["hadhi","rifa","jasim","mayooka"]
mark = [50,60,40,50]
plt.bar(students,mark)
plt.title("student marks")
plt.xlabel("student names")
plt.ylabel("mark")
plt.show()