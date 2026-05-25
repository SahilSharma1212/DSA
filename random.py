# a =[2,3,4,5,6]
# print(a[::-1])

# first we create a string
fruit = "mango"
# now we find the length of the string
len(fruit)
# this line just calculates the legth, aur bas vo nikal ke de deta hai, it dosent print anything yet
# printing the length
print("length of the fruit: ", len(fruit))
# good girl now we perform slicing
# mango -> mang (this means, we want the characters 1 to 4) m, a, n, g right ?
# good but first element starts from 0 right ?
# and 4th index would be 3 ? m- 0, a -1, n -2, g -3 good
# now lets se slicing from 0 - 3
fruit[0:3] # this just calculated the value, print karne ke liye print likhna hoga right ?
# good, now dekho
# we print now 
print(fruit[0:3])
# see, we got only 3 but we wanted 4 right ?
# BIKAUJ in maths you have the concept of ranges, inclusive and non inclusive haina
# toh jab bhi ham slicing vagera karte hai, left limit or lower limit is always inclusive, isliye 0 vala index print hua tha, but the right limit is non inclusive, isliye hame jab bhi let say 10 elements print karne hote hai, so we increase the right limit by 1, because non inclusive hai toh last vala number chhut jayega
print(fruit[0:4])
# ho gaya print wuhuuuuu
# ab aur aage dekho
print("letters to upper case: ", fruit.upper())
# now we try to find a if a specific letter is in the given string
# there is no "r" in mango
print(fruit.find("r"))
# -1 index is used or printed, jab koi cheez nahi milti, ya exist nahi karti
# now lets try to find something that is present
print(fruit.find("a"))

# 1 means True, 0 means False, and -1 means dosen't exist
# samjhe ghonchu ?
# good

