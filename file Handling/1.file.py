file = []
for i in range(2):
    file.append(input("Enter Name: "))
print(file)

file = open("Demo file.txt", mode='w')
file.write("We have create a text file .")
file.close()