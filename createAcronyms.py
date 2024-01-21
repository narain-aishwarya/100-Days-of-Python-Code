nameTobeConverted = str(input("Enter the Name: "))
text = nameTobeConverted.split()
a = " "
for i in text:
    a = a+str(i[0]).upper
print(a)