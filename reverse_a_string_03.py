s = "SagarTambatkar"


def reverse(string):
    str = string[::-1]
    return str


print("The original string is ", end="")
print(s)

print("The reverse string is ", end="")
print(reverse(s))

# Extended slice offers to put a “step” field as [start, stop, step], and giving no field as start and stop indicates default to 0 and string length respectively, and “-1” denotes starting from the end and stop at the start, hence reversing a string. 

# Time complexity: O(n) 
# Auxiliary Space: O(1) 