a = "SagarTambatkar"


def reverse(string):
    str = "".join(reversed(string))
    return str


print("The og string is:", end="")
print(a)

print("The rvr string is: ", end="")
print(reverse(a))

# The reversed() returns the reversed iterator of the given string and then its elements are joined empty string separated using join(). And reversed order string is formed. 

# Time complexity: O(n) 
# Auxiliary Space: O(n) 

