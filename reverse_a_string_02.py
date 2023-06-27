
def reverse(a):
    if len(a) == 0:
        return a
    else:
        return reverse(a[1:]) + a[0]


a = "SagarTambatkar"

print("The original string is: ", end="")
print(a)

print("The reversed string is: ", end="")
print(reverse(a))

# The string is passed as an argument to a recursive function to reverse the string. In the function, the base condition is that if the length of the string is equal to 0,
# the string is returned. If not equal to 0,
# the reverse function is recursively called to slice the part of the string except the first character and concatenate the first character to the end of the sliced string. ‘