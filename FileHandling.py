#1 R Mode
# file=open("File.text","r")
# data=file.read()
# print(data)
# file.close()

#2. W Mode
# file=open("File.text","w")
# file.write("Welcome to Shorat...!")
# file.close()

#3. Append Mode
# file=open("File.text","a")
# file.write("\nWelcome to Python...!")
# file.close()

#4 X Mode

# file=open("XFile.txt","x")
# file.write("Welcome to Shorat...!")
# file.close()

#Readline

# file=open("File.text","r")
# data=file.readline()
# print(data)

#Readlines

# file=open("File.text","r")
# data=file.readlines()
# print(data)
# file.close()

# with open("File.text","r") as file:
# data=file.read()
# print(data)
# file.close()


#r+ 

file=open("File.text","r+")
data=file.read()
print(data)

