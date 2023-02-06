def pattern(n):
    for i in range (0, n):
        for j in range (0, i+1):
            print("*", end=" ")
        print("\n")
        

pattern(6)

input("Press any key on keyboard and press enter to exit")
