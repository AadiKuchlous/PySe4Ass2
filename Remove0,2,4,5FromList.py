s = input("Enter values seperated by commas")
l = s.split(",")
l.remove(l[0])
l.remove(l[2])
l.remove(l[3])
l.remove(l[2])
print(l)
