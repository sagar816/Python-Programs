a = "SagarTambatkar"


def reverse(string):
    str = [string[i] for i in range(len(string)-1, -1, -1)]
    return "".join(str)


print("The original string is: ", end="")
print(a)

print("The reversed string is: ", end="")
print(reverse(a))


# List comprehension creates the list of elements of a string in reverse order and then its elements are joined using join(). And reversed order string is formed.

# Time complexity: O(n)
# Auxiliary Space: O(1)

