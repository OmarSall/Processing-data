# myfile = open("fruits.txt")
# #print(myfile.read())
# content = myfile.read()

# myfile.close()

# print(content)
# #print(content)

#############################################

# with open("files/fruits.txt") as myfile:
#     content = myfile.read()

# print(content)

# with open("files/vegetables3.txt", 'w') as myfile:
#     content = myfile.write("Tomato\nOnion\nCucumber")
#     myfile.write("\nGarlic")

# print(content)

#Read the text and print out the first 90 characters

# with open("bear.txt", 'r') as myfile:
#     content = myfile.read()

# print(content[:90])

# define a funciton that returns nr of occurences of character
# def fun(character, filepath = "bear.txt"):
#     file = open(filepath)
#     content = file.read()
#     return content.count(character)

# with open("bear.txt", "r") as myfile:
#     content = myfile.read()
#     first_90 = content[:90]

# with open("first.txt",'w') as file:
#     file.write(first_90)


# with open("files/vegetables3.txt","a") as myfile:
#     myfile.write("\nOkra")

# with open("bear1.txt", "r") as myfile:
#      content = myfile.read()
     
# with open("bear2.txt",'a+') as file:
#      file.write(content)

# with open("data.txt",'a+') as myfile:
#     myfile.seek(0)
#     content = myfile.read()
#     myfile.seek(0)
#     myfile.write(content)
#     myfile.write(content)