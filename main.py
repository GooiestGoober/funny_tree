big = int(input("How big tree???"))
for j in range(big,0,-1):
    print(" " * (big-j), end="")
    print("&" * (j*2-1))
