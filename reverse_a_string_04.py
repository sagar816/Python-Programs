a = "SagarTambatkar"


def reverse(string):
    str = "".join(reversed(string))
    return str


print("The og string is:", end="")
print(a)

print("The rvr string is: ", end="")
print(reverse(a))
