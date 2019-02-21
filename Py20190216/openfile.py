FILENAME = "test.txt"
file = open("test.txt","r")
all_data = file.readlines()
print all_data
file.close()

print("Lines: ", len(all_data))
for Line in all_data:
    print(Line.strip())


