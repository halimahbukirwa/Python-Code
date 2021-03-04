#Lists
mylist = [1,2,3,4]

mylist = ["STRING", 100, 6.88]

mylist = ['one', 'two', 'three']

print(mylist)

another_list = ['four', 'five', 'six']

newlist = mylist + another_list

print(newlist)

len(newlist)   #length value

print(newlist[1])   #indexing

print(newlist[:-1])

print(newlist[0:3])   #slicing

print(newlist)

newlist[0] = 'ONE CAP'  #reassigning is possible unlike in strings

print(newlist)

newlist.append('seven') #append method

print(newlist)

newlist.pop()

print(newlist)

popped_item = newlist.pop()

print(popped_item)

newlist.pop(0) #pop method with an index passed in

print(newlist)

#sort and reserve list

new_list = ['a','k','u','j','y','q']
num_list = [1, 7, 3, 6, 5, 3]

new_list.sort()   #.sort method

print(new_list)

num_list.sort()    # it is sorted in place, nothing is returned

print(num_list)

num_list.reverse()    #.reserve method
print(num_list)

