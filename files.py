#creating a file
%%writefile myfile.txt
This is my new file
This is the second line
This is the third line

myfile = open('myfile.txt')

pwd

myfile.read()

myfile.read()

myfile.seek(0)# resting the cursor back to zero inorder to read the file

myfile.read()

myfile.seek(0)

myfile.readlines()

#FILE LOCATIONS

pwd

myfile.close()

with open('myfile.txt') as my_new_file:         #no worrying about closing the file
     contents = my_new_file.read()

print(contents)

with open('myfile.txt',mode='r') as myfile:
    contents = myfile.read()

print(contents)

with open('myfile.txt',mode='w') as myfile:
    contents = myfile.read()

%%writefile mynewfile.txt
ONE ON FIRST
TWO ON SECOND
THREE ON THIRD


with open('mynewfile.txt', mode='r') as mynewfile:
       print(mynewfile.read())

with open('mynewfile.txt',mode='a')as mynewfile:
    mynewfile.write('FOUR ON FOURTH')

with open('right.txt',mode='w') as f:
    f.write('I created this new file')

with open('right.txt',mode='r') as f:
    print(f.read())

