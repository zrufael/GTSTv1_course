print("wellcome to Baroks python lab!!!!")

name = input("what is your name? ")

#ZDO is my friend :)

if name == "ZDO":
   print(name + ", your are not allowed to see my lab! Hed kezi!!!")
else : 
   print(name + ", welcame to my python lab!!")


python_knowlage = input("What is ur level of understanding python?" + "\n Is it ' -2, -1 , 0 , 1 , 2, ...'? ")


if python_knowlage <= "0":
   print(name + ", sorry u must to learn basic skills of python to understand. ")
   exit()
else :
   print(name + " ,you are good to Go.")



# Python3 code to demonstrate working of
# Adding Tuple to List and vice - versa

# initializing list and tuple
test_list = [5, 6, 7]
test_tup = (9,10)

# printing original list
print("The original list is : " + str(test_list))

# Adding Tuple to List
test_list.extend(list(test_tup))
# printing result
print("The container after addition : " + str(test_list))

#*********************************************************

# initializing list and tuple
test_list = [1,2,3,4]
test_tup=(5,6)

# printing original tuple
print("The original tuple is : " + str(test_tup))

#Adding list to tuple
test_tup=list(test_tup)
test_tup.extend(test_list)
test_tup=tuple(test_tup)
# printing result
print("The container after addition : " + str(test_tup))
