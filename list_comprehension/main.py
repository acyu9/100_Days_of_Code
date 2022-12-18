with open("file1.txt") as file:
    file1 = file.readlines()
    #file1 = [int(num) for num in file1]
    #print(file1)

with open("file2.txt") as file:
    file2 = file.readlines()
    #file2 = [int(num) for num in file2] 

result = [int(num) for num in file1 if num in file2]
print(result)

# \n ignored when casting to int so no need to write it out separately