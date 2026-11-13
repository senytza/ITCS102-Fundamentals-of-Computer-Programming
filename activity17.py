# LIST

fruits = ["(0)MANDARIN", "(1)MANGO","(2)MELON", "(3)MULBERRY"]
print(fruits)
#LIST FUNCTIONS
# .append INSERTS TO LIST
fruits.append("(4)Mangosteen")
fruits.append("(5)MAYPOP")
print(fruits)
print(fruits[1]) #GETS THE 1 INDEX VALUE
fruits.insert(1,"(+1)MUSKMELON")
print(fruits)

#list slicing
print(fruits[0:3])
print(fruits[-5:])
print(fruits[: -3])
# print(fruits[-5,-1])
