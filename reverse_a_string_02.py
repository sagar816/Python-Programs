
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
