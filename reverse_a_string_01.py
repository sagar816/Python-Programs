a = "SagarTambatkar"
str = ""
for i in a:
    str = i + str


print("The original string is: ", end='')
print(a)

print("The reversed string is: ", end='')
print(str)

# In this example, we call a function to reverse a string, which iterates to every element and intelligently joins each character in the beginning so as to obtain the reversed string.
